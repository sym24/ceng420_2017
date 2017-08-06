from condition import *
import random

class Gene(object):
	def __init__(self):
		self.conditions = []
		self.hand_class = -1
		self.mutation_resistance = 0.0
		self.labelled = [0 for i in range(10)]
		self._possible_conditions = [ValueDiffEq, ValueEq, ValueIneq, ValueGt, ValueLt, \
			ValueCntEq, ValueCntIneq, SuitEq, SuitIneq, SuitCntEq, SuitCntIneq]
		
	def __str__(self):
		str = ""
		str += "\t# Mutation Resistance: %.2f percent" % (100.0 * self.mutation_resistance)
		str += "\n"
		str += "\tif "
		for condition in self.conditions:
			str += "(%s)" % condition
			if condition is not self.conditions[-1]:
				str += " and "
			else:
				str += ":\n\t\t"
		str += "hand_classes[%s] += 1\n" % self.hand_class
		return str
		
	def __repr__(self):
		return self.__str__()
		
	def generate_conditions(self, max_conds, seed):
		'''
		Randomly generates a gene of variable size. 
		'''
		random.seed(seed)
		self.hand_class = random.randint(0,9)
		for i in range(random.randint(1,max_conds)):
			condition_idx = random.randint(0,len(self._possible_conditions) - 1)
			self.conditions.append(self._possible_conditions[condition_idx](random.random()))
		self.conditions = list(set(self.conditions)) # Remove any duplicate conditions
		
	def rewire_gene(self, seed):
		'''
		After a gene has been used in classification, this function can be called to modify
		the class the gene belongs to by keeping a count of the most frequent class
		that the gene says yes to.
		'''
		max_occurence = max(self.labelled)
		
		# If gene is indecisive, replace if
		if self.labelled.count(max_occurence) > 1:
			# Rewire gene
			recomb_prob = float(self.labelled.count(max_occurence)) / 20.0
			self.recombination(recomb_prob - self.mutation_resistance, seed)
			
		# If gene is labelled incorrectly, fix it
		elif self.labelled.index(max_occurence) != self.hand_class:
			# Change gene label
			self.hand_class = self.labelled.index(max_occurence)
			
	def insertion(self, insertion_rate, seed):
		'''
		Randomly add conditions to the gene.
		'''
		random.seed(seed)
		for i in range(len(self.conditions)):
			if random.random() < (insertion_rate - self.mutation_resistance / 2):
				condition_idx = random.randint(0,len(self._possible_conditions) - 1)
				self.conditions.append(self._possible_conditions[condition_idx](random.random()))
			
	def deletion(self, deletion_rate, seed):
		'''
		Randomly delete conditions from the gene.
		'''
		random.seed(seed)
		if len(self.conditions) == 0:
			return
		idx = 0
		for i in range(len(self.conditions)):
			if random.random() < (deletion_rate - self.mutation_resistance / 2):
				del self.conditions[idx]
				idx -= 1
			idx += 1
		
	def recombination(self, recombination_rate, seed):
		'''
		Randomly change condition parameters for conditions in the gene.
		'''
		random.seed(seed)
		for condition in self.conditions:
			condition.mutate_params(recombination_rate - self.mutation_resistance, random.random())
			
	def mutate_class(self, mutate_rate, seed):
		'''
		Randomly change the class the gene represents.
		'''
		random.seed(seed)
		if random.random() < (mutate_rate - self.mutation_resistance):
			self.hand_class = random.randint(0,9)
		
	def compute_result(self, hand):
		''' 
		AND all conditions in gene, using the input hand. 
		If all conditions return True, then this gene says the hand is its corresponding class.
		If one of the conditions returns False, then this gene says nothing.
		'''
		for condition in self.conditions:
			if not condition.get_result(hand):
				return False
		return True