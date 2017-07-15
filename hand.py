from card import Card

class Hand(object):
	def __init__(self, data_row):
		self.cards = []
		for idx in range(5):
			self.cards.append(Card())
			self.cards[idx].init_card_num(data_row["S%s" % (idx+1)], data_row["C%s" % (idx+1)])
		self.labelled_class = data_row["hand"]
		self.assigned_class = -1
		
	@property
	def fitness(self):
		if self.labelled_class == self.assigned_class:
			return 1
		elif self.assigned_class == -1:
			return -1
		else:
			return 0