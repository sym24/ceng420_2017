# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 12:14:10 2017

@author: Yiming
"""

import os
import pandas as pd 
import random as rd
from math import ceil
from hand import Hand
from population import Population
from classify_hands import get_best_chromosome

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

print "Initializing population..."
pop = Population(20, 100, 20, crossover_rate=0.5, insert_rate_c=0.5, insert_rate_g=0.3, lifetime=-1, \
	recomb_rate_g=0.8, delete_rate_c = 0.5, delete_rate_g = 0.3, mutate_rate=0.8, pop_limit=-1, \
	rand_child = 2, parent_count = 2)
print "Population initialized."

var = ""
while var.lower() not in ["y","n","yes","no"]:
	var = raw_input("Add current best to population? (y/n) ")
	if var.lower() in ["y","yes"]:
		pop.chromosomes[0] = get_best_chromosome()

percent = 20.0
generation_count = 0

hands_classes = []
for hand_class in range(10):
	hands_classes.append([hand for hand in hands if hand.labelled_class == hand_class])
#print hands_classes

try:

	while True:
		generation_count += 1
		print "Starting Generation %s." % generation_count

		print "Randomly selecting %s percent of hands for training..." % percent
		train = []
		for c_hands in hands_classes:
			if (len(hands) * percent / 100.0) < len(c_hands):
				rd.shuffle(c_hands)
				train += c_hands[:int(len(c_hands)*percent / 100.0)]
			else:
				train += c_hands

		print "Calculating fitness of population..."
		pop.calculate_fitness(train, rd.random())
		print "Fitness computation complete."

		for chromosome in pop.chromosomes:
			cond_sum = 0
			mut_res_sum = 0
			max_mut_res = max(gene.mutation_resistance for gene in chromosome.genes)
			min_mut_res = min(gene.mutation_resistance for gene in chromosome.genes)
			for gene in chromosome.genes:
				cond_sum += len(gene.conditions)
				mut_res_sum += gene.mutation_resistance
			print "Chromosome fitness:%s, gene_cnt:%s, avg_cond:%s, age:%s" % \
				(chromosome.fitness, len(chromosome.genes), cond_sum / len(chromosome.genes), \
					chromosome.age)

		#max_fit = max(chromosome.fitness * len(chromosome.genes) for chromosome in pop.chromosomes)
		#max_fit = max(chromosome.fitness for chromosome in pop.chromosomes)
		max_fit = max(chromosome.correctly_classified for chromosome in pop.chromosomes)
		print "Correct Classifications: %s/%s = %.2f percent" % (max_fit, len(train), (100.0 * float(max_fit) / float(len(train))))
		
		pop.chromosomes.sort(key=lambda chromosome: chromosome.fitness)
		best = pop.chromosomes[-1]
		for idx in range(10):
			print "Class %s: %s/%s=%.2f" % (idx, best.class_fitness[idx], best.class_count[idx], \
				100.0 * float(best.class_fitness[idx]) / float(best.class_count[idx]))
		

		print "Applying crossover to population..."
		pop.crossover(rd.random())
		print "Crossover complete."
		
except KeyboardInterrupt:

	# Find and the best solution
	print "\nFinding best solution..."
	pop.chromosomes.sort(key=lambda chromosome: chromosome.fitness)
	best = pop.chromosomes[-1]
	
	# Classify data
	print "Classifying test data..."
	best.classify_hands(hands)
	print "Data classified"
	print "Accuracy: %s/%s = %s percent" % (best.correctly_classified, len(hands), \
		100.0 * float(best.correctly_classified) / float(len(hands)))
		
	# Save chromosome function to file
	print "Saving classifier to file classifier.py..."
	with open('classifier.py', 'w') as output:
		output.write("%s" % best)
	
	
