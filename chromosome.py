import random
from gene import Gene
		
class Chromosome(object):
	def __init__(self, max_genes, max_conds, seed):
		self.genes = []
		self.fitness = 0
		self.generate_genes(max_genes, max_conds, seed)
		
	def generate_genes(self, max_genes, max_conds, seed):
		random.seed(seed)
		for i in range(random.randint(1,max_genes)):
			self.genes.append(Gene(max_conds, random.random()))
		
	def add_gene(self, gene):
		self.genes += gene
		
	def remove_gene(self, idx):
		try:
			del self.genes[idx]
		except IndexError:
			print "The index to remove is out of range. List size: %s" % len(self.genes)
			
	def replace_gene(self, idx, new_gene):
		try:
			self.genes[idx] = new_gene
		except IndexError:
			print "The index to replace is out of range. List size: %s" % len(self.genes)
		
	def classify_hands(self, hands):
		''' Loops through list of hands, and classifies each hand '''
		# Initialize fitness
		self.fitness = 0
		
		# Loop through each hand in dataset
		for hand in hands:
			# Classify hand using genes
			for gene in self.genes:
				if gene.compute_result(hand):
					hand.assigned_class = gene.hand_class
			# Add up fitness for hand
			self.fitness += hand.fitness
			
		# Apply minimum fitness so crossover still works
		if self.fitness < 1:
			self.fitness = 1
			