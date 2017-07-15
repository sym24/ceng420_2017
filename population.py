import random
from chromosome import Chromosome

class Population(object):
	def __init__(self, crossover_rate=0.5, recomb_rate=0.5, insert_rate_c=0.2, delete_rate_c=0.19, \
	insert_rate_g=0.2, delete_rate_g=0.19, population_size, max_genes, max_conds, seed=0):
		self.chromosomes = []
		generate_chromosomes(population_size, max_genes, max_conds, seed)
	
	def generate_chromosomes(self, population_size, max_genes, max_conds, seed)
		random.seed(seed)
		for i in range(population_size):
			self.chromosomes.append(Chromosome(max_genes, max_conds, random.random())