import os
import pandas as pd 
import random as rd
from math import ceil
from hand import Hand
from jinja2 import Environment, FileSystemLoader
from population import Population
from classify_hands import get_best_chromosome
from classify_hands import join_dirs
from chromosome import Chromosome

Trainpath = 'train.csv'
Testpath = 'test.csv'
pwd = os.getcwd()
print(pwd)

print "Loading training data..."
df = pd.read_csv(Trainpath)
hands = []
for index, row in df.iterrows():
    hands.append(Hand(row))
    train_data = row[:]
    #print(train_data)
print "Data loaded."

print "Initializing 10 populations, one for each class..."
rd.seed(0)
populations = []
population_size = 10
max_genes = 20
max_conds = 10
for i in range(10):
	populations.append(Population(population_size, max_genes, max_conds, crossover_rate=0.5, insert_rate_c=0.5, insert_rate_g=0.3, \
		recomb_rate_g=0.8, delete_rate_c = 0.6, delete_rate_g = 0.3, mutate_rate=0.6, rand_child=1, \
		parent_count=2, one_vs_all=i, seed=rd.random()))
print "Populations initialized."

hands_classes = []
for hand_class in range(10):
	hands_classes.append([hand for hand in hands if hand.labelled_class == hand_class])

percent = 15.0


for i in range(10):
	generation = 0
	best_fit = 0
	try:
		while True:
			print "Starting generation %s of population %s." % (generation, i)

			print "Randomly selecting %s percent of hands for training..." % percent
			train = []
			for c_hands in hands_classes:
				if (len(hands) * percent / 100.0) < len(c_hands):
					rd.shuffle(c_hands)
					train += c_hands[:int(len(hands)*percent / 100.0)]
				else:
					train += c_hands

			print "Calculating fitness of population..."
			populations[i].calculate_fitness(train, rd.random())
			print "Fitness computation complete."
	
			populations[i].chromosomes.sort(key=lambda chromosome: chromosome.fitness)
			for chromosome in populations[i].chromosomes:
				cond_sum = 0
				mut_res_sum = 0
				max_mut_res = max(gene.mutation_resistance for gene in chromosome.genes)
				min_mut_res = min(gene.mutation_resistance for gene in chromosome.genes)
				for gene in chromosome.genes:
					cond_sum += len(gene.conditions)
					mut_res_sum += gene.mutation_resistance
				print "Chromosome fitness:%s, gene_cnt:%s, avg_cond:%s, age:%s" % \
					(chromosome.fitness, len(chromosome.genes), cond_sum / len(chromosome.genes), chromosome.age)
				
			best = populations[i].chromosomes[-1]
			for idx in range(10):
				print "Class %s: %d/%d=%.2f" % (idx, best.class_fitness[idx], best.class_count[idx], \
					100.0 * float(best.class_fitness[idx]) / float(best.class_count[idx]))

			max_classified = max(chromosome.correctly_classified for chromosome in populations[i].chromosomes)
			print "Classified %s of %s correctly." % (max_classified, len(train))
			print "Accuracy: %.2f percent." % (100.0 * float(max_classified) / float(len(train)))

			best_fit = max(chromosome.fitness for chromosome in populations[i].chromosomes)
			if best_fit == 1400.0:
				break

			print "Applying crossover to population..."
			populations[i].crossover(rd.random())
			print "Crossover complete."
			generation += 1		
				
	except KeyboardInterrupt:
		print "Moving on to next class."
	
print "Computing final solution..."
final_solution = Chromosome()
for hand_class in range(10):
	populations[hand_class].chromosomes.sort(key=lambda chromosome: chromosome.fitness)
	best_chromosome = populations[hand_class].chromosomes[-1]
	final_solution.genes += best_chromosome.genes
print "Final solution computed."
		
# Classify data
print "Classifying all data..."
final_solution.classify_hands(hands)
print "Data classified"
print "Accuracy: %s/%s = %.2f percent" % (final_solution.correctly_classified, len(hands), \
	100.0 * float(final_solution.correctly_classified) / float(len(hands)))
	
# Save chromosome function to file
print "Saving classifier to file classifier.py..."
path = join_dirs(pwd, 'templates')
print path
template = Environment(loader=FileSystemLoader(path)).get_template('classifier_template.py')
with open('classifier.py', 'w') as output:
	context = {
		'chromosome':final_solution
	}
	output.write(template.render(context))