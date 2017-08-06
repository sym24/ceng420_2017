import random
#from statistics import stdev
from copy import deepcopy
from chromosome import Chromosome

class Population(object):
	def __init__(self, population_size, max_genes, max_conds, crossover_rate=0.7, \
		mutate_rate=0.9, insert_rate_c=0.6, delete_rate_c=0.4, insert_rate_g=0.7, rand_child=0,\
		delete_rate_g=0.7, recomb_rate_g=0.9, parent_count=3, lifetime=-1, pop_limit=-1, seed=0):
		self.chromosomes = []
		self.__max_genes = max_genes
		self.__max_conds = max_conds
		self.__crossover = crossover_rate
		self.__mutate_rate = mutate_rate
		self.__insert_rate_chr = insert_rate_c
		self.__delete_rate_chr = delete_rate_c
		self.__insert_rate_gen = insert_rate_g
		self.__delete_rate_gen = delete_rate_g
		self.__recomb_rate_gen = recomb_rate_g
		self.__lifetime = lifetime
		self.__population_limit = pop_limit
		self.__parent_count = parent_count
		self.__rand_child = rand_child
		self.generate_chromosomes(population_size, seed)
	
	def generate_chromosomes(self, population_size, seed):
		'''
		Randomly generate a new population.
		'''
		random.seed(seed)
		for i in range(population_size):
			chromosome = Chromosome()
			chromosome.generate_genes(self.__max_genes, self.__max_conds, random.random())
			self.chromosomes.append(chromosome)
			
	def calculate_fitness(self, hands, seed):
		'''
		Calculates the fitness of all chromosomes in population by making them try and
		classify the hands provided.
		'''
		# Compute the fitness
		for chromosome in self.chromosomes:
			chromosome.classify_hands(hands)
			chromosome.age += 1 
			
	def apply_mutations(self, chromosomes, seed):
		'''
		Apply mutations to given chromosomes. 
		
		There are 2 kinds of chromosome-level mutations:
		1) Randomly delete genes from chromosome
		2) Randomly insert genes to chromosome
		
		There are 4 kinds of gene-level mutations:
		1) Randomly delete conditions from gene
		2) Randomly insert conditions to gene
		3) Randomly change the parameters in a condition
		4) Randomly change the class of the gene
		'''
		random.seed(seed)
		# mutate chromosome
		for chromosome in chromosomes:# Apply deletion mutations
			if random.random() <= self.__mutate_rate:
				chromosome.deletion(self.__delete_rate_chr, random.random())
				
			# Apply insertion mutations
			if random.random() <= self.__mutate_rate:
				chromosome.insertion(self.__max_conds, self.__insert_rate_chr, random.random())
				
			for gene in chromosome.genes:
				# Apply recombination mutations
				if random.random() <= self.__mutate_rate:
					gene.recombination(self.__recomb_rate_gen, random.random())
					
				# Apply deletion mutations
				if random.random() <= self.__mutate_rate:
					gene.deletion(self.__delete_rate_gen, random.random())
					
				# Apply class mutation
				if random.random() <= self.__mutate_rate:
					gene.mutate_class(self.__mutate_rate, random.random())
				
				# Apply insertion mutations
				if random.random() <= self.__mutate_rate:
					gene.insertion(self.__insert_rate_gen, random.random())
					
	def roulette_selection(self, choices, seed):
		''' 
		Randomly select parents with probability proportional to the fitness.
		'''
		random.seed(seed)
		
		# Calculate total fitness
		fitness_total = 0
		for chromosome in self.chromosomes:
			fitness_total += int(chromosome.fitness + 0.5)
			
		# Choose parents
		parent_chromosomes = []
		for i in range(self.__parent_count):
			roulette_pointer = random.randint(1, fitness_total)
			
			# Find the chromosome for parent
			roulette_position = 0
			for chromosome_idx in range(len(choices)):
				roulette_position += int(choices[chromosome_idx].fitness + 0.5)
				if roulette_pointer <= roulette_position:
					selection = choices.pop(chromosome_idx)
					parent_chromosomes.append(selection)
					fitness_total -= int(selection.fitness + 0.5)
					break
					
		return parent_chromosomes
		
	def rank_selection(self, choices, seed):
		''' 
		Randomly select parents with probability proportional to the order of choices
		when sorted based on fitness.
		'''
		random.seed(seed)
		
		# Sort choices in ascending order by fitness
		choices.sort(key=lambda chromosome: chromosome.fitness)
		
		# Find wheel limit (n*(n-1)/2)
		wheel_limit = len(choices) * (len(choices) - 1) / 2
		
		# Choose parents
		parent_chromosomes = []
		for i in range(self.__parent_count):
			wheel_pointer = random.randint(1, wheel_limit)
			
			# Find the parent chromosome
			wheel_position = 0
			for chromosome_idx in range(len(choices)):
				wheel_position += chromosome_idx
				if wheel_pointer <= wheel_position:
					wheel_limit -= len(choices)
					selection = choices.pop(chromosome_idx)
					parent_chromosomes.append(selection)
					break
					
		return parent_chromosomes
		
	def random_selection(self, choices, seed):
		''' Randomly select parents with equal probability for each parent. '''
		random.seed(seed)
		
		# Choose parents
		parent_chromosomes = []
		for i in range(self.__parent_count):
			parent_idx = random.randint(0, len(choices) - 1)
			# Fix genes
			for gene in choices[parent_idx].genes:
				gene.rewire_gene(seed)
			parent_chromosomes.append(choices.pop(parent_idx))
			
		return parent_chromosomes
		
	def parent_selection(self, choices, seed):
		'''
		The parent selection method is chosen at random.
		There are 3 methods of parents selection:
		1) Rank Selection (44.44% chance)
		2) Roulette Selection (44.44% chance)
		3) Random Selection (11.11% chance)
		'''
		#std = stdev([chromosome.fitness for chromosome in choices])
		random.seed(seed)
		method = random.randint(1,9)
		if method <= 4:
			return self.rank_selection(choices, random.random())
		elif method <= 8:
			return self.roulette_selection(choices, random.random())
		else:
			return self.random_selection(choices, random.random())
		
					
	def crossover(self, seed):
		'''
		Apply crossover to generate the new generation of the population. Steps:
		1) Select parents (a parent can only be selected once)
		2) Use the genes of parent to breed new children (genes randomly assigned to children)
		3) Mutate children (multiple kinds of mutations)
		4) Remove any children without genes
		5) Remove any genes without alleles/conditions
		6) Trim the population as needed
		7) Add children to population
		'''
	
		random.seed(seed)
		
		children_count = int(len(self.chromosomes) * self.__crossover)
		children_count -= children_count % self.__parent_count
		children = []
		
		print "Breeding %s children." % children_count
		
		# Loop through all crossover events to breed new children
		choices = deepcopy(self.chromosomes)
		for crossover_event in range( children_count / self.__parent_count ):
			# Select parents (this will return a copy of parents)
			parents = self.parent_selection(choices, random.random())
			
			# Initialize new children for current crossover event
			new_children = []
			new_children += [Chromosome() for x in range(self.__parent_count)]
			
			# Loop through all parents
			for parent in parents:
				# Loop through all genes in current parent
				for i in range(len(parent.genes)):
					# Randomly select parent gene to pass on to random child
					pop_idx = random.randint(0, len(parent.genes) - 1)
					child_idx = random.randint(0, len(new_children) - 1)
					
					# Add parent gene to child
					new_children[child_idx].genes.append(parent.genes.pop(pop_idx))
					
			# Delete copies of parents so they can't be chosen again
			del parents
			children += new_children
			
		# Mutate children
		print "Mutating children"
		self.apply_mutations(children, random.random())
		
		# Remove any genes of size 0, and remove duplicate conditions
		for child in children:
			child.genes = [gene for gene in child.genes if len(gene.conditions) > 0]
			for gene in child.genes:
				gene.conditions = list(set(gene.conditions))
		
		# Remove any children of size 0
		children = [child for child in children if len(child.genes) > 0]
		
		# Add any random children to the mix
		for i in range(self.__rand_child):
			child = Chromosome()
			child.generate_genes(self.__max_genes, self.__max_conds, random.random())
			children.append(child)
		
		# Sort population by fitness
		self.chromosomes.sort(key=lambda chromosome: (chromosome.fitness, chromosome.fitness))
		
		# If there's too many in the population, kill the least fit
		if self.__population_limit > 0 and self.__population_limit < len(self.chromosomes):
			del self.chromosomes[0:(len(self.chromosomes) - self.__population_limit)]
		
		# Add children to population
		if self.__lifetime < 0:
			# Replace the least fit with the children
			del self.chromosomes[0:len(children)]
			self.chromosomes = children + self.chromosomes
		else:
			# Kill half of the least fit
			#del self.chromosomes[0:int(len(children)/2)]		
		
			# Add children
			self.chromosomes = children + self.chromosomes
		
			# Kill off the elderly
			idx = 0
			for i in range(len(self.chromosomes)):
				if self.chromosomes[idx].age > self.__lifetime:
					del self.chromosomes[idx]
					idx -= 1
				idx += 1
					