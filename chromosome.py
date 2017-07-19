import random
from gene import Gene
		
class Chromosome(object):
	def __init__(self):
		self.genes = []
		self.fitness = 0
		self.correctly_classified = 0 
		self.age = 0
		
	def generate_genes(self, max_genes, max_conds, seed):
		random.seed(seed)
		for i in range(random.randint(1,max_genes)):
			gene = Gene()
			gene.generate_conditions(max_conds, random.random())
			self.genes.append(gene)
			
	def insertion(self, max_conds, insertion_rate, seed):
		random.seed(seed)
		for i in range(len(self.genes)):
			if random.random() < insertion_rate:
				gene = Gene()
				gene.generate_conditions(max_conds, random.random())
				self.genes.append(gene)
			
	def deletion(self, deletion_rate, seed):
		random.seed(seed)
		if len(self.genes) == 0:
			return
		idx = 0
		for i in range(len(self.genes)):
			if random.random() < (deletion_rate - self.genes[idx].mutation_resistance):
				del self.genes[idx]
				idx -= 1
			idx += 1
		
	def classify_hands(self, hands):
		''' Loops through list of hands, and classifies each hand '''
		# Initialize fitness
		#if self.fitness != 0:
		#	return
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
			for gene in self.genes:
				if gene.compute_result(hand):
					# Add a count for given hand class
					hand_classes[gene.hand_class] += 1
					gene.labelled[hand.labelled_class] += 1
					if hand.labelled_class == gene.hand_class:
						gene.mutation_resistance += 1.0 / 100.0
					#else:
					#	gene.mutation_resistance -= 2.0 / len(hands)
					# Update variables for mutation resilience
					#gene.mutation_resistance = 0
						
			if max(hand_classes) > 0:
				hand.assigned_class = hand_classes.index(max(hand_classes))
			# Add up fitness for hand
			self.fitness += hand.fitness
			if hand.fitness == 1:
				self.correctly_classified += 1
				
				
			