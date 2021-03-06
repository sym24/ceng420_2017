import random
from gene import Gene
		
class Chromosome(object):
	def __init__(self):
		self.genes = []
		self.default_class = -1
		self.class_fitness = [0 for i in range(10)]
		self.class_count = [0 for i in range(10)]
		self.fitness = 0
		self.correctly_classified = 0
		self.age = 0
		self.__one_vs_all = -1 # feature inactive
		
	def __str__(self):
		str = "def classify(hand):\n"
		str += "\thand_classes = [0 for i in range(10)]\n"
		for gene in self.genes:
			str += "%s" % gene
		str += "\n\tif max(hand_classes) > 0:\n"
		str += "\t\thand.assigned_class = hand_classes.index(max(hand_classes))\n"
		str += "\telse:\n"
		str += "\t\thand.assigned_class = %d\n" % self.default_class
		return str
		
	def __repr__(self):
		return self.__str__()
		
	def generate_genes(self, max_genes, max_conds, seed):
		'''
		Randomly generate a variable size chromosome.
		'''
		random.seed(seed)
		self.default_class = random.randint(0,9)
		for i in range(random.randint(1,max_genes)):
			gene = Gene()
			gene.generate_conditions(max_conds, random.random())
			if self.one_vs_all != -1:
				gene.hand_class = self.one_vs_all
			self.genes.append(gene)
			
	@property
	def one_vs_all(self):
		return self.__one_vs_all
		
	@one_vs_all.setter
	def one_vs_all(self, hand_class):
		self.__one_vs_all = hand_class
		for gene in self.genes:
			gene.hand_class = hand_class
			
	def insertion(self, max_genes, max_conds, insertion_rate, seed):
		'''
		Mutation Function
		Randomly inserts genes into the chromosome. 
		'''
		random.seed(seed)
		for i in range(max_genes):
			if random.random() < (insertion_rate):
				gene = Gene()
				gene.generate_conditions(max_conds, random.random())
				if self.one_vs_all != -1:
					gene.hand_class = self.one_vs_all
				self.genes.append(gene)
			
	def deletion(self, deletion_rate, seed):
		'''
		Mutation Function
		Randomly deletes genes from the chromosome
		'''
		random.seed(seed)
		if len(self.genes) == 0:
			return
		idx = 0
		for i in range(len(self.genes)):
			if random.random() < (deletion_rate - self.genes[idx].mutation_resistance):
				del self.genes[idx]
				idx -= 1
			idx += 1
			
	def mutate_class(self, mutate_rate, seed):
		random.seed(seed)
		if random.random() < mutate_rate:
			self.default_class = random.randint(0,9)
		
	def classify_hands(self, hands, class_distr = None):
		''' Loops through list of hands, and classifies each hand '''
		# Initialize fitness
		#if self.fitness != 0:
		#	return
		initial_fitness = self.fitness
		try:
			self.fitness = 0
			self.correctly_classified = 0
			for gene in self.genes:
				gene.correct_assigns = 0
				gene.total_assigns = 0
				gene.mutation_resistance = 0.0
				gene.labelled = [0 for i in range(10)]
		
			# Loop through each hand in dataset
			for hand in hands:
				# Classify hand using genes
				hand.assigned_class = -1
				hand_classes = [0 for i in range(0,10)]
			
				# Experimental - create variables for this hand
				hand_confidences = [0 for i in range(10)]
			
				# Use genes to classify hand
				for gene in self.genes:
					if gene.compute_result(hand):
						# Add a count for given hand class
						hand_classes[gene.hand_class] += 1
						gene.labelled[hand.labelled_class] += 1
					
						# Experimental
						# Update mutation resistance if classification was correct
						#if self.one_vs_all != -1:
						#	pass
						if hand.labelled_class == gene.hand_class and gene.confidence > 0 and class_distr is not None:
							gene.mutation_resistance += 1.0 / float(class_distr[hand.labelled_class])
							#gene.mutation_resistance += 0.1 * float(int(class_distr[hand.labelled_class] / 1000)) / float(class_distr[hand.labelled_class])
						elif hand.labelled_class != gene.hand_class and gene.confidence < 0 and class_distr is not None:
							gene.mutation_resistance += 1.0 / float(class_distr[hand.labelled_class])
							#gene.mutation_resistance += 0.1 * float(int((len(hands) - class_distr[hand.labelled_class]) / 1000)) / float(len(hands) - class_distr[hand.labelled_class])
					
						#Experimental - Add confidence to given class. Assign if confidence has reached 100
						hand_confidences[gene.hand_class] += gene.confidence
			
				#Experimental	
				# Classify hand
				if max(hand_confidences) >= 100:
					hand.assigned_class = hand_confidences.index(max(hand_confidences))
				elif self.one_vs_all != -1:
					if hand.labelled_class == self.__one_vs_all:
						hand.assigned_class = -1
					else:
						hand.assigned_class = hand.labelled_class
				else:
					hand.assigned_class = self.default_class
				
				# Add up fitness for hand
				self.class_fitness[hand.labelled_class] += hand.fitness
				self.class_count[hand.labelled_class] += 1
				if hand.fitness == 1:
					self.correctly_classified += 1
					
		except KeyboardInterrupt:
			self.fitness = initial_fitness
			raise KeyboardInterrupt
		
	@property		
	def fitness(self):
		'''
		Computes the fitness of the chromosome. Must call classify_hands before 
		requesting this property. If you don't, it will always return 1.
		
		Proportional fitness computed, where the accuracy for each class is measured. Each 
		class can give 100 points to the fitness. A perfect fitness is a fitness of 
		(class_count*100).
		'''
		fitness = 0
		for idx in range(10):
			if self.class_count[idx] > 0 and idx == self.__one_vs_all:
				fitness += 500.0 * float(self.class_fitness[idx]) / float(self.class_count[idx])
			elif self.class_count[idx] > 0:
				fitness += 100.0 * float(self.class_fitness[idx]) / float(self.class_count[idx])
					
		if fitness <= 0:
			fitness = 1
			
		return fitness
		
	@fitness.setter
	def fitness(self, val):
		'''
		By trying to set the fitness, the fitness will automatically reset itself to 0.
		'''
		for idx in range(10):
			self.class_fitness[idx] = 0
			self.class_count[idx] = 0
				
				
			