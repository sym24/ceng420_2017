import Condition

class Gene(object):
	def __init__(self):
		self.conditions = []
		self.hand_class = -1
		self._possible_conditions = [ValueDiffEq, ValueEq, ValueIneq, ValueGt, ValueLt, SuitEq, SuitIneq]
		
	def add_condition(self, condition):
		self.conditions += condition()
		
	def remove_condition(self, idx):
		try:
			del self.conditions[idx]
		except IndexError:
			print "The index to remove is out of range. List size: %s. Index request: %s" % (len(self.conditions), idx)
			
	def replace_condition(self, idx, new_function, *new_parameters):
		try:
			self.conditions[idx].update_condition(new_function, *new_parameters)
		except IndexError:
			print "The index to replace is out of range. List size: %s. Index request: %s" % (len(self.conditions), idx)
			
	def mutate_condition_parameters(self, idx, mutation_rate, seed):
		try:
			self.conditions[idx].mutate_params(mutation_rate, seed)
		except IndexError:
			print "The index to mutate is out of range. List size: %s. Index request: %s" % (len(self.conditions), idx)
			
	def compute_gene_result(self, hand):
		''' AND all conditions '''
		for condition in conditions:
			if not condition.get_result(hand):
				return False
		return True
		
class Chromosome(object):
	def __init__(self):
		self.genes = []
		self.fitness = 0
		
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
			for gene in genes:
				if gene.compute_result(hand):
					hand.assigned_class = gene.hand_class
			# Add up fitness for hand
			self.fitness += hand.fitness
			
		# Apply minimum fitness so crossover still works
		if fitness < 1:
			fitness = 1
			