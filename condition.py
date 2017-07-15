from card import Card
import random
	
class Condition(object):
	def __init__(self, function, *parameters):
		self.function = function
		self.parameters = parameters
		
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
	def __init__(self):
		Condition.__init__(self, self.value_diff_eq, *self.get_rand_params())
		
	@staticmethod
	def value_diff_eq(hand, idx1, idx2, diff):
		return ( (hand.cards[idx1].val - hand.cards[idx2].val) == diff )
	
	def gen_rand_params(self, seed):
		random.seed(seed)
		
		# Generate two unique card indices
		idx1 = random.randint(0,4)
		idx2 = random.randint(0,4)
		while idx1 == idx2:
			idx2 = random.randint(0,4)
			
		# Generate difference parameter (value of cards 1 - 13, therefore difference can be 1 - 12 to make this unique from equality)
		diff = random.randint(1,12)
		
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
			
		# Update the parameters of the class
		self.parameters = (idx1, idx2, diff)
		
		
class ValueEq(Condition):
	def __init__(self):
		Condition.__init__(self, self.value_eq, *self.get_rand_params())
		
	@staticmethod
	def value_eq(hand, idx1, idx2):
		return ( hand.cards[idx1].val == hand.cards[idx2].val )
		
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
	def __init__(self):
		Condition.__init__(self, self.value_ineq, *self.get_rand_params())
		
	@staticmethod
	def value_ineq(hand, idx1, idx2):
		return ( hand.cards[idx1].val != hand.cards[idx2].val )
		
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
	def __init__(self):
		Condition.__init__(self, self.value_gt, *self.get_rand_params())
	
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
	def __init__(self):
		Condition.__init__(self, self.value_gt, *self.get_rand_params())
		
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
	def __init__(self):
		Condition.__init__(self, self.suit_eq, *self.get_rand_params())
		
	@staticmethod
	def suit_eq(hand, idx1, idx2):
		return (hand.cards[idx1].suit == hand.cards[idx2].suit)
		
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
	def __init__(self):
		Condition.__init__(self, self.suit_ineq, *self.get_rand_params())
		
	@staticmethod
	def suit_eq(hand, idx1, idx2):
		return (hand.cards[idx1].suit != hand.cards[idx2].suit)
		
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
	
		
		