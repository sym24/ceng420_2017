from card import Card
import random
	
class Condition(object):
	'''
	Base class for all conditions
	'''
	def __init__(self, function, *parameters):
		self.function = function
		self.parameters = parameters
		
	def __eq__(self, other):
		if type(self) is type(other):
			result = self.function == other.function
			if result:
				result = result and self._parameter_equality(other)
			return result
		else:
			return NotImplemented
			
	def __ineq__(self, other):
		if type(self) is type(other):
			return not self.__eq__(self, other)
		
	def _parameter_equality(self, other):
		return self.parameters == other.parameters
		
	def update_condition(self, function, *parameters):
		self.function = function
		self.parameters = parameters
		
	def get_result(self, hand):
		if self.function is None:
			raise ValueError("Function hasn't been initialized.")
		return self.function(hand, *self.parameters)
		
	def gen_rand_params(self, seed):
		return ()
		
	def mutate_params(self, mutation_rate, seed):
		return
		
class ValueDiffEq(Condition):
	def __init__(self, seed):
		Condition.__init__(self, self.value_diff_eq, *self.gen_rand_params(seed))
		
	def __str__(self):
		return "(hand.cards[%s].val - hand.cards[%s].val) == %s" % (self.parameters[0], self.parameters[1], self.parameters[2])
		
	def __repr__(self):
		return "(C%s - C%s) == %s" % (self.parameters[0] + 1, self.parameters[1] + 1, self.parameters[2])
		
	@staticmethod
	def value_diff_eq(hand, idx1, idx2, diff):
		return ( hand.cards[idx1].val - hand.cards[idx2].val == diff )
		
	def _parameter_equality(self, other):
		result = self.parameters[0] in other.parameters[0:2]
		result = result and self.parameters[1] in other.parameters[0:2]
		result = result and self.parameters[2] == other.parameters[2]
		return result
	
	def gen_rand_params(self, seed):
		random.seed(seed)
		
		# Generate two unique card indices
		idx1 = random.randint(0,4)
		idx2 = random.randint(0,4)
		while idx1 == idx2:
			idx2 = random.randint(0,4)
			
		# Generate difference parameter (value of cards 1 - 13, therefore difference can be -12 - 12 to make this unique from equality)
		diff = random.randint(1,12)
		
		# 50% chance of making diff negative
		if random.randint(0,1):
			diff = -diff
		
		# Return them as a tuple
		return (idx1, idx2, diff)
		
	def mutate_params(self, mutation_rate, seed):
		random.seed(seed)
		
		# Get all parameters
		idx1 = self.parameters[0]
		idx2 = self.parameters[1]
		diff = self.parameters[2]
		
		# Randomly apply random mutations to parameters
		param1 = random.random()
		if param1 <= mutation_rate:
			idx1 = random.randint(0,4)
			while idx1 == idx2:
				idx1 = random.randint(0,4)
		
		param2 = random.random()
		if param2 <= mutation_rate:
			idx2 = random.randint(0,4)
			while idx1 == idx2:
				idx2 = random.randint(0,4)
			
		param3 = random.random()	
		if param3 <= mutation_rate:
			diff = random.randint(1,12)
			if random.randint(0,1):
				diff = -diff
			
		# Update the parameters of the class
		self.parameters = (idx1, idx2, diff)
		
		
class ValueEq(Condition):
	def __init__(self, seed):
		Condition.__init__(self, self.value_eq, *self.gen_rand_params(seed))
		
	def __str__(self):
		return "hand.cards[%s].val == hand.cards[%s].val" % (self.parameters[0], self.parameters[1])
		
	def __repr__(self):
		return "C%s == C%s" % (self.parameters[0] + 1, self.parameters[1] + 1)
		
	@staticmethod
	def value_eq(hand, idx1, idx2):
		return ( hand.cards[idx1].val == hand.cards[idx2].val )
		
	def _parameter_equality(self, other):
		result = self.parameters[0] in other.parameters[0:2]
		result = result and self.parameters[1] in other.parameters[0:2]
		return result
		
	def gen_rand_params(self, seed):
		random.seed(seed)
		
		# Generate two unique card indices
		idx1 = random.randint(0,4)
		idx2 = random.randint(0,4)
		while idx1 == idx2:
			idx2 = random.randint(0,4)
		
		# Return them as a tuple
		return (idx1, idx2)
		
	def mutate_params(self, mutation_rate, seed):
		random.seed(seed)
		
		# Get all parameters
		idx1 = self.parameters[0]
		idx2 = self.parameters[1]
		
		# Randomly apply random mutations to parameters
		param1 = random.random()
		if param1 <= mutation_rate:
			idx1 = random.randint(0,4)
			while idx1 == idx2:
				idx1 = random.randint(0,4)
		
		param2 = random.random()
		if param2 <= mutation_rate:
			idx2 = random.randint(0,4)
			while idx1 == idx2:
				idx2 = random.randint(0,4)
			
		# Update the parameters of the class
		self.parameters = (idx1, idx2)
		
class ValueIneq(Condition):
	def __init__(self, seed):
		Condition.__init__(self, self.value_ineq, *self.gen_rand_params(seed))
		
	def __str__(self):
		return "hand.cards[%s].val != hand.cards[%s].val" % (self.parameters[0], self.parameters[1])
		
	def __repr__(self):
		return "C%s != C%s" % (self.parameters[0] + 1, self.parameters[1] + 1)
		
	@staticmethod
	def value_ineq(hand, idx1, idx2):
		return ( hand.cards[idx1].val != hand.cards[idx2].val )
		
	def _parameter_equality(self, other):
		result = self.parameters[0] in other.parameters[0:2]
		result = result and self.parameters[1] in other.parameters[0:2]
		return result
		
	def gen_rand_params(self, seed):
		random.seed(seed)
		
		# Generate two unique card indices
		idx1 = random.randint(0,4)
		idx2 = random.randint(0,4)
		while idx1 == idx2:
			idx2 = random.randint(0,4)
		
		# Return them as a tuple
		return (idx1, idx2)
		
	def mutate_params(self, mutation_rate, seed):
		random.seed(seed)
		
		# Get all parameters
		idx1 = self.parameters[0]
		idx2 = self.parameters[1]
		
		# Randomly apply random mutations to parameters
		param1 = random.random()
		if param1 <= mutation_rate:
			idx1 = random.randint(0,4)
			while idx1 == idx2:
				idx1 = random.randint(0,4)
		
		param2 = random.random()
		if param2 <= mutation_rate:
			idx2 = random.randint(0,4)
			while idx1 == idx2:
				idx2 = random.randint(0,4)
			
		# Update the parameters of the class
		self.parameters = (idx1, idx2)
		
class ValueGt(Condition):
	def __init__(self, seed):
		Condition.__init__(self, self.value_gt, *self.gen_rand_params(seed))
		
	def __str__(self):
		return "hand.cards[%s].val > %s" % (self.parameters[0], self.parameters[1])
		
	def __repr__(self):
		return "C%s > %s" % (self.parameters[0] + 1, self.parameters[1])
			
	@staticmethod
	def value_gt(hand, idx, val):
		return ( hand.cards[idx].val > val )
		
	def gen_rand_params(self, seed):
		random.seed(seed)
		
		# Generate a card index
		idx = random.randint(0,4)
		
		# Generate a value to measure against (1 - 12) (every card > 0, no card > 13)
		val = random.randint(1,12)
		
		# Return them as a tuple
		return (idx, val)
		
	def mutate_params(self, mutation_rate, seed):
		random.seed(seed)
		
		# Get all parameters
		idx = self.parameters[0]
		val = self.parameters[1]
		
		# Randomly apply random mutations to parameters
		param1 = random.random()
		if param1 <= mutation_rate:
			idx = random.randint(0,4)
		
		param2 = random.random()
		if param2 <= mutation_rate:
			val = random.randint(1,12)
			
		# Update the parameters of the class
		self.parameters = (idx, val)
		
class ValueLt(Condition):
	def __init__(self, seed):
		Condition.__init__(self, self.value_lt, *self.gen_rand_params(seed))
		
	def __str__(self):
		return "hand.cards[%s].val < %s" % (self.parameters[0], self.parameters[1])
		
	def __repr__(self):
		return "C%s < %s" % (self.parameters[0] + 1, self.parameters[1])
		
	@staticmethod
	def value_lt(hand, idx, val):
		return ( hand.cards[idx].val < val )
		
	def gen_rand_params(self, seed):
		random.seed(seed)
		
		# Generate a card index
		idx = random.randint(0,4)
		
		# Generate a value to measure against (2 - 13) (no card < 1)
		val = random.randint(2,13)
		
		# Return them as a tuple
		return (idx, val)
		
	def mutate_params(self, mutation_rate, seed):
		random.seed(seed)
		
		# Get all parameters
		idx = self.parameters[0]
		val = self.parameters[1]
		
		# Randomly apply random mutations to parameters
		param1 = random.random()
		if param1 <= mutation_rate:
			idx = random.randint(0,4)
		
		param2 = random.random()
		if param2 <= mutation_rate:
			val = random.randint(2,13)
			
		# Update the parameters of the class
		self.parameters = (idx, val)
		
class SuitEq(Condition):
	def __init__(self, seed):
		Condition.__init__(self, self.suit_eq, *self.gen_rand_params(seed))
		
	def __str__(self):
		return "hand.cards[%s].suit == hand.cards[%s].suit" % (self.parameters[0], self.parameters[1])
		
	def __repr__(self):
		return "S%s == S%s" % (self.parameters[0] + 1, self.parameters[1] + 1)
		
	@staticmethod
	def suit_eq(hand, idx1, idx2):
		return (hand.cards[idx1].suit == hand.cards[idx2].suit)
		
	def _parameter_equality(self, other):
		result = self.parameters[0] in other.parameters[0:2]
		result = result and self.parameters[1] in other.parameters[0:2]
		return result
		
	def gen_rand_params(self, seed):
		random.seed(seed)
		
		# Generate two unique card indices
		idx1 = random.randint(0,4)
		idx2 = random.randint(0,4)
		while idx1 == idx2:
			idx2 = random.randint(0,4)
		
		# Return them as a tuple
		return (idx1, idx2)
		
	def mutate_params(self, mutation_rate, seed):
		random.seed(seed)
		
		# Get all parameters
		idx1 = self.parameters[0]
		idx2 = self.parameters[1]
		
		# Randomly apply random mutations to parameters
		param1 = random.random()
		if param1 <= mutation_rate:
			idx1 = random.randint(0,4)
			while idx1 == idx2:
				idx1 = random.randint(0,4)
		
		param2 = random.random()
		if param2 <= mutation_rate:
			idx2 = random.randint(0,4)
			while idx1 == idx2:
				idx2 = random.randint(0,4)
			
		# Update the parameters of the class
		self.parameters = (idx1, idx2)
		
class SuitIneq(Condition):
	def __init__(self, seed):
		Condition.__init__(self, self.suit_ineq, *self.gen_rand_params(seed))
		
	def __str__(self):
		return "hand.cards[%s].suit != hand.cards[%s].suit" % (self.parameters[0], self.parameters[1])
		
	def __repr__(self):
		return "S%s != S%s" % (self.parameters[0] + 1, self.parameters[1] + 1)
	
	@staticmethod
	def suit_ineq(hand, idx1, idx2):
		return (hand.cards[idx1].suit != hand.cards[idx2].suit)
		
	def _parameter_equality(self, other):
		result = self.parameters[0] in other.parameters[0:2]
		result = result and self.parameters[1] in other.parameters[0:2]
		return result
		
	def gen_rand_params(self, seed):
		random.seed(seed)
		
		# Generate two unique card indices
		idx1 = random.randint(0,4)
		idx2 = random.randint(0,4)
		while idx1 == idx2:
			idx2 = random.randint(0,4)
		
		# Return them as a tuple
		return (idx1, idx2)
		
	def mutate_params(self, mutation_rate, seed):
		random.seed(seed)
		
		# Get all parameters
		idx1 = self.parameters[0]
		idx2 = self.parameters[1]
		
		# Randomly apply random mutations to parameters
		param1 = random.random()
		if param1 <= mutation_rate:
			idx1 = random.randint(0,4)
			while idx1 == idx2:
				idx1 = random.randint(0,4)
		
		param2 = random.random()
		if param2 <= mutation_rate:
			idx2 = random.randint(0,4)
			while idx1 == idx2:
				idx2 = random.randint(0,4)
			
		# Update the parameters of the class
		self.parameters = (idx1, idx2)
	
		
		