import os
import pandas as pd 
import random as rd
from math import ceil
from chromosome import Chromosome
from hand import Hand
from population import Population

Trainpath = 'train.csv'
pwd = os.getcwd()
print(pwd)

print "Loading training data..."
df = pd.read_csv(Trainpath)
hands = []
for index, row in df.iterrows():
    hands.append(Hand(row))
print "Data loaded."

print "Initializing 10 populations, one for each class..."
rd.seed(0)
populations = []
population_size = 20
max_genes = 100
max_conds = 20
for i in range(10):
	populations.append(Population(population_size, max_genes, max_conds, crossover_rate=0.5, insert_rate_c=0.5, insert_rate_g=0.3, lifetime=-1, \
		recomb_rate_g=0.8, delete_rate_c = 0.5, delete_rate_g = 0.3, mutate_rate=0.8, pop_limit=-1, \
		parent_count = 2, seed=rd.random()))
print "Populations initialized."

percent = 20.0
generation_count = 0

hands_classes = []
for hand_class in range(10):
	hands_classes.append([hand for hand in hands if hand.labelled_class == hand_class])
	
try:
	for i in range(10):
		generation = 0
		best_fit = 0
		keep_going = True
		while keep_going:
			print "Starting generation %s of population %s." % (generation, i)

			print "Randomly selecting %s percent of hands for training..." % percent
			train = []
			for c_hands in hands_classes:
				if (len(hands) * percent / 100.0) < len(c_hands):
					rd.shuffle(c_hands)
					train += c_hands[:int(len(c_hands)*percent / 100.0)]
				else:
					train += c_hands

			'''
			if (len(hands) * percent / 100.0) < len(hands_classes[i]):
				print "Randomly selecting %s percent of hands for training..." % percent
				rd.shuffle(hands_classes[i])
				train = hands_classes[i][:int(len(hands_classes[i])*percent / 100.0)]
			else:
				train = hands_classes[i]
			'''

			print "Calculating fitness of population..."
			populations[i].calculate_fitness(train, rd.random())
			print "Fitness computation complete."
		
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

			max_classified = max(chromosome.correctly_classified for chromosome in populations[i].chromosomes)
			print "Classified %s of %s correctly." % (max_classified, len(train))
			print "Accuracy: %.2f percent." % (100.0 * float(max_classified) / float(len(train)))
			
			keep_going = False
			for hand in train:
				if hand.labelled_class == i and hand.fitness != 1:
					keep_going = True
					break

			best_fit = max(chromosome.fitness for chromosome in populations[i].chromosomes)

			print "Applying crossover to population..."
			populations[i].crossover(rd.random())
			print "Crossover complete."
			
			print "Trimming chromosomes to remove genes not part of this class..."
			while True:
				for chromosome in populations[i].chromosomes:
					chromosome.genes = [gene for gene in chromosome.genes if gene.hand_class == i]
				
				populations[i].chromosomes = [chromosome for chromosome in populations[i].chromosomes if len(chromosome.genes) > 0]
				
				if len(populations[i].chromosomes) < population_size:
					for j in range(population_size - len(populations[i].chromosomes)):
						new = Chromosome()
						new.generate_genes(max_genes, max_conds, rd.random())
						populations[i].chromosomes.append(new)
				else:
					break
						
			
except KeyboardInterrupt:
	pass
	
print "Computing final solution..."
final_solution = Chromosome()
for hand_class in range(10):
	populations[hand_class].chromosomes.sort(key=lambda chromosome: chromosome.fitness)
	best_chromosome = populations[hand_class].chromosomes[-1]
	for gene in best_chromosome.genes:
		if gene.hand_class == hand_class:
			final_solution.genes.append(gene)
print "Final solution computed."
		
# Classify data
print "Classifying all data..."
final_solution.classify_hands(hands)
print "Data classified"
print "Accuracy: %s/%s = %.2f percent" % (final_solution.correctly_classified, len(hands), \
	100.0 * float(final_solution.correctly_classified) / float(len(hands)))
	
# Save chromosome function to file
print "Saving classifier to file classifier.py..."
with open('classifier.py', 'w') as output:
	output.write("# Classification accuracy: %.2f\n" % (100.0 * float(final_solution.correctly_classified) / float(len(hands))))
	output.write("%s" % final_solution)
