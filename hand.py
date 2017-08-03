from card import Card

class Hand(object):
	def __init__(self, data_row):
		'''
		Converts a data_row formatted pandas style into a Hand class.
		'''
		self.cards = []
		for idx in range(5):
			self.cards.append(Card())
			self.cards[idx].init_card_num(data_row["S%s" % (idx+1)], data_row["C%s" % (idx+1)])
		try:
			self.labelled_class = data_row["hand"]
		except KeyError:
			self.labelled_class = -1
		try:
			self.id = data_row["id"]
		except KeyError:
			self.id = -1
		self.assigned_class = -1
		
	def __str__(self):
		str = ""
		for card in self.cards:
			str += "(%s,%s), " % (card.suit_name, card.val_name)
		str += "(l:%s,p:%s)\n" % (self.labelled_class, self.assigned_class)
		return str
		
	def __repr__(self):
		return self.__str__()
		
	@property
	def fitness(self):
		''' 
		Compute the fitness of the hand based on its classification. 
		'''
		if self.labelled_class == self.assigned_class:
			return 1.0
		elif self.assigned_class >= 0:
			return 0.0
		else:
			return 0.0