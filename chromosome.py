from condition import Condition

class Gene(object):
	def __init__(self):
		self.conditions = []
		self.hand = -1
		
	def add_condition(self, function, parameters):
		self.conditions += Condition.initialize(function, parameters)
		
	def remove_condition(self, idx):
		try:
			del self.conditions[idx]
		except IndexError:
			print "The index to remove is out of range. List size: %s" % len(self.conditions)
			
	def replace_condition(self, idx, new_function, *new_parameters):
		try:
			self.conditions[idx].update_condition(new_function, *new_parameters)
		except IndexError:
			print "The index to replace is out of range. List size: %s" % len(self.conditions)
		
class Chromosome(object):
	def __init__(self):
		self.genes = []
		self.fitness = -1
		
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
			