from condition import *
import random

class Gene(object):
	def __init__(self):
		self.conditions = []
		self.hand_class = -1
		self.mutation_resistance = 0.0
		self.labelled = [0 for i in range(10)]
		self._possible_conditions = [ValueDiffEq, ValueEq, ValueIneq, ValueGt, ValueLt, SuitEq, SuitIneq]
		
	'''
	@property
	def mutation_resistance(self):
		resistance = 0
		if self.total_assigns > 0:
			resistance = 2 * (float(self.correct_assigns) / float(self.total_assigns) - 0.5)
		return resistance
	'''
		
	def generate_conditions(self, max_conds, seed):
		random.seed(seed)
		self.hand_class = random.randint(0,9)
		for i in range(random.randint(1,max_conds)):
			condition_idx = random.randint(0,len(self._possible_conditions) - 1)
			self.conditions.append(self._possible_conditions[condition_idx](random.random()))
		self.conditions = list(set(self.conditions))
		
	def rewire_gene(self, seed):
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
		random.seed(seed)
		for i in range(len(self.conditions)):
			if random.random() < insertion_rate:
				condition_idx = random.randint(0,len(self._possible_conditions) - 1)
				self.conditions.append(self._possible_conditions[condition_idx](random.random()))
			
	def deletion(self, deletion_rate, seed):
		random.seed(seed)
		if len(self.conditions) == 0:
			return
		idx = 0
		for i in range(len(self.conditions)):
			if random.random() < (deletion_rate - self.mutation_resistance):
				del self.conditions[idx]
				idx -= 1
			idx += 1
		
	def recombination(self, recombination_rate, seed):
		random.seed(seed)
		for condition in self.conditions:
			condition.mutate_params(recombination_rate - self.mutation_resistance, random.random())
			
	def mutate_class(self, mutate_rate, seed):
		random.seed(seed)
		if random.random() < (mutate_rate - self.mutation_resistance):
			self.hand_class = random.randint(0,9)
		
	def compute_result(self, hand):
		''' AND all conditions '''
		for condition in self.conditions:
			if not condition.get_result(hand):
				return False
		return True