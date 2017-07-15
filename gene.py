from condition import *
import random

class Gene(object):
	def __init__(self, max_conds, seed):
		self.conditions = []
		self.hand_class = -1
		self._possible_conditions = [ValueDiffEq, ValueEq, ValueIneq, ValueGt, ValueLt, SuitEq, SuitIneq]
		self.generate_conditions(max_conds, seed)
		
	def generate_conditions(self, max_conds, seed):
		random.seed(seed)
		self.hand_class = random.randint(0,9)
		for i in range(random.randint(1,max_conds)):
			condition_idx = random.randint(0,len(self._possible_conditions) - 1)
			self.conditions.append(self._possible_conditions[condition_idx](random.random()))
		
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
			
	def compute_result(self, hand):
		''' AND all conditions '''
		for condition in self.conditions:
			if not condition.get_result(hand):
				return False
		return True