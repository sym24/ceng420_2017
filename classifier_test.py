# Fitness: 1
def yoyo(hand):
	hand_confidences = [0 for i in range(10)]
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].suit == hand.cards[0].suit) and (hand.cards[2].suit == hand.cards[1].suit):
		hand_confidences[5] += 20
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val < 2) and (hand.cards[0].val < 9) and (hand.cards[4].val > 5) and ((hand.cards[2].val - hand.cards[3].val) == 4) and (hand.cards[0].suit == hand.cards[2].suit):
		hand_confidences[0] += 40
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val < 2) and (len([card for card in hand.cards if card.val == 7]) != 4) and (hand.cards[1].suit == hand.cards[2].suit) and (hand.cards[4].val == hand.cards[1].val) and (len([card for card in hand.cards if card.suit == 4]) == 4):
		hand_confidences[1] += -35
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].suit == hand.cards[2].suit):
		hand_confidences[6] += 40
	
	# Mutation Resistance: 0.0%
	if ((hand.cards[2].val - hand.cards[4].val) == 7) and (hand.cards[3].val == hand.cards[1].val) and (hand.cards[0].suit != hand.cards[3].suit) and (len([card for card in hand.cards if card.val == 8]) == 1) and (hand.cards[0].val > 6):
		hand_confidences[2] += 90
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].suit != hand.cards[2].suit) and (hand.cards[3].suit != hand.cards[4].suit) and (hand.cards[0].val > 3) and (hand.cards[4].val < 13):
		hand_confidences[2] += -55
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 3]) != 0) and (len([card for card in hand.cards if card.suit == 2]) == 5) and (len([card for card in hand.cards if card.suit == 2]) == 5) and (hand.cards[2].suit == hand.cards[0].suit):
		hand_confidences[1] += -30
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 9]) != 0) and (hand.cards[3].val < 3) and (hand.cards[2].val < 5) and (hand.cards[2].val != hand.cards[4].val):
		hand_confidences[6] += 50
	
	if max(hand_confidences) >= 100:
		hand.assigned_class = hand_confidences.index(max(hand_confidences))
	else:
		hand.assigned_class = 1