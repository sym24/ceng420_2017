from card import Card

class Hand(object):
	def __init__(self, data_row):
		self.cards = []
		for idx in range(0,5):
			self.cards.append(Card())
			self.cards[idx].init_card_num(data_row[2*idx], data_row[2*idx+1])
		self.labelled_class = data_row[10]
		self.assigned_class = -1
		
	@property
	def fitness(self):
		if self.labelled_class == self.assigned_class:
			return 1
		elif self.assigned_class == -1:
			return -1
		else:
			return 0