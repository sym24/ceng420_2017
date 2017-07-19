# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 12:14:10 2017

@author: Yiming
"""

import os
import pandas as pd 
import random as rd
from hand import Hand
from population import Population

Filepath = 'train.csv'
pwd = os.getcwd()
print(pwd)

print "Loading training data..."
df = pd.read_csv(Filepath)
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

percent = 25.0
generation_count = 0

while True:
	generation_count += 1
	print "Starting Generation %s." % generation_count

	print "Randomly selecting %s percent of hands for training..." % percent
	rd.shuffle(hands)
	train = hands[:int(len(hands)*percent / 100.0)]

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
	print "Max fitness: %s/%s = %.2f percent" % (max_fit, len(train), (100.0 * float(max_fit) / float(len(train))))

	print "Applying crossover to population..."
	pop.crossover(rd.random())
	print "Crossover complete."
