# Fitness: 1
def classify(hand):
	hand_classes = [0 for i in range(10)]
	
	
	# Mutation Resistance: 0.0
	if (hand.cards[0].val > 4) and (hand.cards[4].val < 11) and (hand.cards[4].val != hand.cards[1].val):
		hand_class[5] += 1
	
	# Mutation Resistance: 0.0
	if (hand.cards[4].val == hand.cards[3].val) and (hand.cards[0].suit == hand.cards[3].suit) and (hand.cards[0].suit != hand.cards[3].suit) and (hand.cards[0].val < 2):
		hand_class[0] += 1
	
	# Mutation Resistance: 0.0
	if (hand.cards[4].suit == hand.cards[0].suit) and (len([card for card in hand.cards if card.val == 3]) != 4) and (hand.cards[1].suit != hand.cards[2].suit) and (hand.cards[3].suit != hand.cards[2].suit) and (hand.cards[2].val == hand.cards[1].val):
		hand_class[6] += 1
	
	# Mutation Resistance: 0.0
	if (hand.cards[2].suit != hand.cards[4].suit) and (hand.cards[3].suit == hand.cards[2].suit):
		hand_class[5] += 1
	
	# Mutation Resistance: 0.0
	if (hand.cards[4].val > 4) and (len([card for card in hand.cards if card.suit == 3]) == 1):
		hand_class[4] += 1
	
	# Mutation Resistance: 0.0
	if (hand.cards[4].val < 5) and (len([card for card in hand.cards if card.val == 3]) != 2) and (hand.cards[1].val < 12):
		hand_class[5] += 1
	
	# Mutation Resistance: 0.0
	if (hand.cards[3].suit == hand.cards[1].suit):
		hand_class[2] += 1
	
	# Mutation Resistance: 0.0
	if (hand.cards[2].suit == hand.cards[0].suit) and (len([card for card in hand.cards if card.suit == 1]) != 5):
		hand_class[4] += 1
	
	# Make classification decision
	if max(hand_classes) > 0:
		hand.assigned_class = hand_classes.index(max(hand_classes))
	else:
		hand.assigned_class = 1