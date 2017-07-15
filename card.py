class CardProperty(object):
	def __init__(self, possible_names):
		"""Base class for properties of a card"""
		self._possible_names_ = possible_names
		self._name = ""
		self._num = -1
		
	def init_property_name(self, name):
		if name.lower() not in self._possible_names_:
			raise ValueError("%s is not in list of possible names. Possible names: %s" % (name, self._possible_names_))
		self._name = name
		self._num = self._possible_names_.index(name.lower()) + 1
		
	def init_property_num(self, num):
		if num not in range(1,len(self._possible_names_) + 1):
			raise ValueError("%s is an invalid input. Valid inputs: %s" % (num, range(1,len(self._possible_names_) + 1)))
		self._num = num
		self._name = self._possible_names_[num - 1]
	
	@property
	def num(self):
		""":obj:`int` The numeric representation of the property.

        Calling any init function will modify both the numeric property, and the string property.
        """
		return self._num

	@num.setter
	def num(self, number):
		self.init_property_num(number)
		
	@property
	def name(self):
		""":obj:`str` The name of this property.

        Calling any init function will modify both the numeric property, and the string property.
        """
		return self._name
	
	@name.setter
	def name(self, new_name):
		self.init_property_name(new_name)

class Suit(CardProperty):
	def __init__(self):
		"""Class used to store a card's suit."""
		CardProperty.__init__(self, ["hearts", "spades", "diamonds", "clubs"])
		
class CardVal(CardProperty):
	def __init__(self):
		"""Class used to store a card's value."""
		CardProperty.__init__(self, ["a", "2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k"])
		
class Card(object):
	def __init__(self):
		"""Class used to store a card.
		
		Attributes:
        	suit (:obj:`Suit`): Object containing information about the suit of a card.
        	val (:obj:`CardVal`): Object containing information about the value of a card.
        """
		self._suit = Suit()
		self._val = CardVal()
		
	def init_card_name(self, suit_name, card_name):
		self._suit.init_property_name(suit_name)
		self._val.init_property_name(card_name)
		
	def init_card_num(self, suit_num, card_num):
		self._suit.init_property_num(suit_num)
		self._val.init_property_num(card_num)
		
	@property
	def val(self):
		return self._val.num
		
	@property
	def val_name(self):
		return self._val.name
		
	@property
	def suit(self):
		return self._suit.num
		
	@property
	def suit_name(self):
		return self._suit.name