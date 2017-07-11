from card import Card

def value_diff_eq(hand, idx1, idx2, diff):
	return ( (hand[idx1].val - hand[idx2].val) == diff )
	
def value_eq(hand, idx1, idx2):
	return ( hand[idx1].val == hand[idx2].val )

def value_ineq(hand, idx1, idx2):
	return ( hand[idx1].val != hand[idx2].val )
	
def value_gt(hand, idx, val):
	return ( hand[idx].val > val )
	
def value_lt(hand, idx, val):
	return ( hand[idx].val < val )
	
def suit_eq(card1, card2):
	return (card1.suit == card2.suit)
	
def suit_ineq(card1, card2):
	return (card1.suit != card1.suit)

class Condition(object):
	def __init__(self):
		self.function = None
		self.parameters = []
		
	@classmethod
	def initialize(cond, function, *parameters):
		cond = cond()
		cond.function = function
		cond.parameters = parameters
		return cond
		
	def update_condition(self, function, *parameters):
		self.function = function
		self.parameters = parameters
		
	def get_result(self, hand):
		if self.function is None:
			raise ValueError("Function hasn't been initialized.")
		return self.function(hand, *self.parameters)