# Fitness: 519.44
def classify(hands):
	hand_classes = [0 for i in range(10)]
	for hand in hands:
		# Mutation Resistance: 80.00 percent
		if (hand.cards[3].val < 9) and (hand.cards[1].val < 7) and (len([card for card in hand.cards if card.suit == 1]) != 3):
			hand_classes[8] += 1
		# Mutation Resistance: 5.02 percent
		if (hand.cards[1].val != hand.cards[0].val) and (hand.cards[0].val > 10) and (hand.cards[3].val < 3) and (len([card for card in hand.cards if card.suit == 1]) != 0):
			hand_classes[1] += 1
		# Mutation Resistance: 83.33 percent
		if (hand.cards[0].val == hand.cards[1].val):
			hand_classes[7] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[3].val != hand.cards[1].val) and (hand.cards[1].val != hand.cards[4].val):
			hand_classes[4] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[0].suit == hand.cards[4].suit):
			hand_classes[5] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[0].suit == hand.cards[4].suit):
			hand_classes[5] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[2].val != hand.cards[4].val) and (hand.cards[1].val != hand.cards[0].val) and (hand.cards[2].val != hand.cards[4].val):
			hand_classes[4] += 1
		# Mutation Resistance: 79.57 percent
		if (len([card for card in hand.cards if card.suit == 3]) != 5) and (hand.cards[2].suit != hand.cards[0].suit):
			hand_classes[4] += 1
		# Mutation Resistance: 83.33 percent
		if (hand.cards[2].suit != hand.cards[0].suit) and (hand.cards[2].val == hand.cards[3].val) and (hand.cards[3].suit != hand.cards[1].suit):
			hand_classes[7] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[2].suit == hand.cards[4].suit) and (len([card for card in hand.cards if card.val == 10]) != 0) and (hand.cards[3].val != hand.cards[0].val) and (len([card for card in hand.cards if card.val == 11]) != 0):
			hand_classes[9] += 1
		# Mutation Resistance: 83.33 percent
		if (hand.cards[2].suit != hand.cards[0].suit) and (hand.cards[3].suit != hand.cards[1].suit) and (hand.cards[2].val == hand.cards[3].val):
			hand_classes[7] += 1
		# Mutation Resistance: 0.00 percent
		if ((hand.cards[4].val - hand.cards[0].val) == -2) and (hand.cards[4].val > 3) and (hand.cards[2].suit == hand.cards[3].suit) and ((hand.cards[0].val - hand.cards[4].val) == -6):
			hand_classes[3] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[3].val != hand.cards[0].val) and (len([card for card in hand.cards if card.val == 10]) != 0) and (hand.cards[2].suit == hand.cards[4].suit) and (len([card for card in hand.cards if card.val == 11]) != 0):
			hand_classes[9] += 1
		# Mutation Resistance: 86.19 percent
		if (hand.cards[4].val > 2) and (hand.cards[1].val > 1):
			hand_classes[2] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[0].suit == hand.cards[4].suit):
			hand_classes[5] += 1
		# Mutation Resistance: 0.09 percent
		if (hand.cards[2].suit == hand.cards[3].suit) and (len([card for card in hand.cards if card.val == 9]) == 2) and (hand.cards[1].val == hand.cards[4].val) and (len([card for card in hand.cards if card.suit == 2]) == 1) and (hand.cards[0].suit != hand.cards[1].suit):
			hand_classes[2] += 1
		# Mutation Resistance: 80.00 percent
		if (hand.cards[1].val < 7) and (len([card for card in hand.cards if card.suit == 1]) != 3) and (hand.cards[3].val < 9):
			hand_classes[8] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[3].val != hand.cards[0].val) and (len([card for card in hand.cards if card.val == 11]) != 0) and (len([card for card in hand.cards if card.val == 10]) != 0) and (hand.cards[2].suit == hand.cards[4].suit):
			hand_classes[9] += 1
		# Mutation Resistance: 80.00 percent
		if (hand.cards[0].val < 7):
			hand_classes[8] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.suit == 4]) != 3):
			hand_classes[5] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[1].val != hand.cards[0].val) and (hand.cards[2].val != hand.cards[4].val) and (hand.cards[2].val != hand.cards[4].val):
			hand_classes[4] += 1
		# Mutation Resistance: 80.00 percent
		if (hand.cards[3].val < 9) and (len([card for card in hand.cards if card.suit == 1]) != 3) and (hand.cards[1].val < 7):
			hand_classes[8] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.val == 12]) != 2):
			hand_classes[3] += 1
		# Mutation Resistance: 0.00 percent
		if (len([card for card in hand.cards if card.suit == 3]) != 0) and (hand.cards[2].val < 12):
			hand_classes[9] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.val == 11]) != 0) and (hand.cards[2].suit == hand.cards[4].suit) and (len([card for card in hand.cards if card.val == 10]) != 0) and (hand.cards[3].val != hand.cards[0].val):
			hand_classes[9] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[2].suit == hand.cards[0].suit) and (hand.cards[1].suit == hand.cards[3].suit):
			hand_classes[9] += 1
		# Mutation Resistance: 83.33 percent
		if (hand.cards[0].val == hand.cards[1].val):
			hand_classes[7] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[3].val != hand.cards[0].val) and (len([card for card in hand.cards if card.val == 11]) != 0) and (hand.cards[2].suit == hand.cards[4].suit) and (len([card for card in hand.cards if card.val == 10]) != 0):
			hand_classes[9] += 1
		# Mutation Resistance: 80.00 percent
		if (hand.cards[3].val < 9) and (hand.cards[1].val < 7) and (len([card for card in hand.cards if card.suit == 1]) != 3):
			hand_classes[8] += 1
		# Mutation Resistance: 92.01 percent
		if (len([card for card in hand.cards if card.val == 2]) != 3):
			hand_classes[3] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[2].suit == hand.cards[0].suit) and (hand.cards[1].suit == hand.cards[3].suit):
			hand_classes[9] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.val == 7]) != 1):
			hand_classes[7] += 1
		# Mutation Resistance: 82.85 percent
		if (hand.cards[0].suit != hand.cards[1].suit):
			hand_classes[3] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.val == 10]) != 0) and (hand.cards[2].suit == hand.cards[4].suit) and (len([card for card in hand.cards if card.val == 11]) != 0) and (hand.cards[3].val != hand.cards[0].val):
			hand_classes[9] += 1
		# Mutation Resistance: 82.85 percent
		if (hand.cards[0].suit != hand.cards[1].suit):
			hand_classes[3] += 1
		# Mutation Resistance: 0.00 percent
		if (hand.cards[0].suit != hand.cards[2].suit) and (hand.cards[3].val > 7) and (hand.cards[4].val < 3) and (hand.cards[1].val == hand.cards[3].val) and (hand.cards[2].val < 6) and (hand.cards[1].suit == hand.cards[4].suit) and (hand.cards[2].val != hand.cards[1].val) and (hand.cards[1].val == hand.cards[2].val) and (hand.cards[4].val != hand.cards[2].val) and (hand.cards[1].val < 7) and (len([card for card in hand.cards if card.val == 2]) != 4) and (hand.cards[1].suit != hand.cards[0].suit) and (hand.cards[4].suit != hand.cards[2].suit):
			hand_classes[8] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[2].val != hand.cards[4].val) and (hand.cards[1].val != hand.cards[0].val) and (hand.cards[2].val != hand.cards[4].val):
			hand_classes[4] += 1
		# Mutation Resistance: 80.00 percent
		if (len([card for card in hand.cards if card.suit == 1]) != 3) and (hand.cards[3].val < 9) and (hand.cards[1].val < 7):
			hand_classes[8] += 1
		# Mutation Resistance: 83.33 percent
		if (len([card for card in hand.cards if card.suit == 4]) != 4) and (hand.cards[0].val == hand.cards[2].val):
			hand_classes[7] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[0].val != hand.cards[1].val) and (len([card for card in hand.cards if card.val == 6]) != 4):
			hand_classes[5] += 1
		# Mutation Resistance: 83.33 percent
		if (hand.cards[0].val == hand.cards[1].val):
			hand_classes[7] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[3].val != hand.cards[0].val) and (len([card for card in hand.cards if card.val == 10]) != 0) and (hand.cards[2].suit == hand.cards[4].suit) and (len([card for card in hand.cards if card.val == 11]) != 0):
			hand_classes[9] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.val == 11]) != 0) and (len([card for card in hand.cards if card.val == 10]) != 0) and (hand.cards[2].suit == hand.cards[4].suit) and (hand.cards[3].val != hand.cards[0].val):
			hand_classes[9] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.val == 12]) != 2):
			hand_classes[3] += 1
		# Mutation Resistance: 0.00 percent
		if (hand.cards[0].val == hand.cards[4].val) and (hand.cards[1].val > 8) and (len([card for card in hand.cards if card.val == 3]) == 4) and (len([card for card in hand.cards if card.val == 4]) == 0):
			hand_classes[3] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.val == 7]) != 1):
			hand_classes[7] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[3].val != hand.cards[4].val):
			hand_classes[5] += 1
		# Mutation Resistance: 79.57 percent
		if (len([card for card in hand.cards if card.suit == 3]) != 5) and (hand.cards[2].suit != hand.cards[0].suit):
			hand_classes[4] += 1
		# Mutation Resistance: 83.33 percent
		if (hand.cards[2].suit != hand.cards[0].suit) and (hand.cards[3].suit != hand.cards[1].suit) and (hand.cards[2].val == hand.cards[3].val):
			hand_classes[7] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.val == 10]) != 3):
			hand_classes[7] += 1
		# Mutation Resistance: 4.42 percent
		if (hand.cards[2].suit != hand.cards[3].suit) and (hand.cards[3].val > 6) and (hand.cards[3].val != hand.cards[1].val) and (hand.cards[4].val < 10) and ((hand.cards[0].val - hand.cards[3].val) == 1) and (len([card for card in hand.cards if card.suit == 3]) != 4):
			hand_classes[0] += 1
		# Mutation Resistance: 165.67 percent
		if (hand.cards[3].val != hand.cards[2].val) and (hand.cards[2].suit != hand.cards[4].suit):
			hand_classes[0] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[2].val != hand.cards[4].val) and (hand.cards[1].val != hand.cards[0].val) and (hand.cards[2].val != hand.cards[4].val):
			hand_classes[4] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[1].val != hand.cards[0].val) and (hand.cards[2].val != hand.cards[4].val) and (hand.cards[2].val != hand.cards[4].val):
			hand_classes[4] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[0].suit == hand.cards[4].suit):
			hand_classes[5] += 1
		# Mutation Resistance: 0.00 percent
		if (len([card for card in hand.cards if card.val == 7]) != 3) and ((hand.cards[2].val - hand.cards[4].val) == 10) and (hand.cards[2].val < 10) and (hand.cards[2].val != hand.cards[4].val) and (hand.cards[2].val == hand.cards[0].val) and (hand.cards[4].suit == hand.cards[2].suit) and (hand.cards[0].suit != hand.cards[2].suit):
			hand_classes[0] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[2].val != hand.cards[4].val) and (hand.cards[2].val != hand.cards[4].val) and (hand.cards[1].val != hand.cards[0].val):
			hand_classes[4] += 1
		# Mutation Resistance: 83.33 percent
		if (hand.cards[0].val == hand.cards[1].val):
			hand_classes[7] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[2].val > 1):
			hand_classes[7] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.suit == 2]) != 5):
			hand_classes[3] += 1
		# Mutation Resistance: 80.00 percent
		if (hand.cards[0].val < 7):
			hand_classes[8] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.val == 6]) != 2):
			hand_classes[8] += 1
		# Mutation Resistance: 80.00 percent
		if (len([card for card in hand.cards if card.suit == 1]) != 3) and (hand.cards[1].val < 7) and (hand.cards[3].val < 9):
			hand_classes[8] += 1
		# Mutation Resistance: 80.00 percent
		if (hand.cards[1].val < 7) and (hand.cards[3].val < 9) and (len([card for card in hand.cards if card.suit == 1]) != 3):
			hand_classes[8] += 1
		# Mutation Resistance: 67.25 percent
		if (hand.cards[2].val != hand.cards[4].val):
			hand_classes[3] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.suit == 4]) != 3):
			hand_classes[5] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[0].suit == hand.cards[4].suit):
			hand_classes[5] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.val == 8]) != 1):
			hand_classes[6] += 1
		# Mutation Resistance: 83.33 percent
		if (hand.cards[0].val == hand.cards[1].val):
			hand_classes[7] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[0].suit == hand.cards[4].suit):
			hand_classes[5] += 1
		# Mutation Resistance: 83.33 percent
		if (hand.cards[1].val == hand.cards[0].val):
			hand_classes[7] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[2].val != hand.cards[1].val):
			hand_classes[5] += 1
		# Mutation Resistance: 80.00 percent
		if (hand.cards[0].val < 7):
			hand_classes[8] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.val == 10]) != 0) and (hand.cards[3].val != hand.cards[0].val) and (hand.cards[2].suit == hand.cards[4].suit) and (len([card for card in hand.cards if card.val == 11]) != 0):
			hand_classes[9] += 1
		# Mutation Resistance: 83.33 percent
		if (hand.cards[0].val == hand.cards[1].val):
			hand_classes[7] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[2].suit == hand.cards[0].suit) and (hand.cards[1].suit == hand.cards[3].suit):
			hand_classes[9] += 1
		# Mutation Resistance: 82.85 percent
		if (hand.cards[0].suit != hand.cards[1].suit):
			hand_classes[3] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.val == 7]) != 1):
			hand_classes[7] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[0].val != hand.cards[1].val) and (len([card for card in hand.cards if card.val == 6]) != 4):
			hand_classes[5] += 1
		# Mutation Resistance: 75.27 percent
		if (hand.cards[1].suit != hand.cards[2].suit) and (hand.cards[2].val != hand.cards[4].val):
			hand_classes[4] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[0].suit == hand.cards[4].suit):
			hand_classes[5] += 1
		# Mutation Resistance: 79.57 percent
		if (hand.cards[0].suit != hand.cards[2].suit):
			hand_classes[4] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.val == 7]) != 1):
			hand_classes[7] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[3].val != hand.cards[4].val):
			hand_classes[5] += 1
		# Mutation Resistance: 79.57 percent
		if (hand.cards[2].suit != hand.cards[0].suit) and (len([card for card in hand.cards if card.suit == 3]) != 5):
			hand_classes[4] += 1
		# Mutation Resistance: 39.76 percent
		if (hand.cards[3].val < 4) and (len([card for card in hand.cards if card.suit == 1]) != 4) and (hand.cards[0].suit != hand.cards[3].suit):
			hand_classes[0] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[2].val != hand.cards[4].val) and (hand.cards[2].val != hand.cards[4].val) and (hand.cards[1].val != hand.cards[0].val):
			hand_classes[4] += 1
		# Mutation Resistance: 0.00 percent
		if (len([card for card in hand.cards if card.val == 11]) != 1) and (hand.cards[3].val == hand.cards[0].val) and (len([card for card in hand.cards if card.suit == 1]) == 1):
			hand_classes[9] += 1
		# Mutation Resistance: 135.67 percent
		if (len([card for card in hand.cards if card.val == 8]) != 1):
			hand_classes[0] += 1
		# Mutation Resistance: 117.40 percent
		if (hand.cards[4].val > 6):
			hand_classes[0] += 1
		# Mutation Resistance: 0.00 percent
		if (hand.cards[2].val == hand.cards[4].val) and (hand.cards[0].val < 6) and (len([card for card in hand.cards if card.val == 8]) != 3) and (len([card for card in hand.cards if card.suit == 1]) == 1) and (hand.cards[2].val != hand.cards[0].val) and (len([card for card in hand.cards if card.suit == 3]) != 3):
			hand_classes[0] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[0].suit == hand.cards[2].suit) and (hand.cards[4].suit == hand.cards[2].suit) and (len([card for card in hand.cards if card.val == 3]) != 4):
			hand_classes[8] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.val == 12]) != 2):
			hand_classes[3] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[1].val != hand.cards[4].val) and (hand.cards[3].val != hand.cards[1].val):
			hand_classes[4] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[3].val != hand.cards[1].val) and (hand.cards[1].val != hand.cards[4].val):
			hand_classes[4] += 1
		# Mutation Resistance: 0.00 percent
		if (hand.cards[3].val == hand.cards[0].val) and (len([card for card in hand.cards if card.val == 7]) == 2) and (hand.cards[2].val != hand.cards[4].val) and (hand.cards[4].val < 3) and (hand.cards[2].suit != hand.cards[4].suit) and (len([card for card in hand.cards if card.suit == 1]) != 0) and (hand.cards[1].suit != hand.cards[4].suit) and (len([card for card in hand.cards if card.suit == 2]) != 2) and (hand.cards[1].val < 8) and (hand.cards[0].suit == hand.cards[1].suit) and (len([card for card in hand.cards if card.suit == 4]) != 3):
			hand_classes[9] += 1
		# Mutation Resistance: 82.85 percent
		if (hand.cards[0].suit != hand.cards[1].suit):
			hand_classes[3] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.val == 10]) != 0) and (len([card for card in hand.cards if card.val == 11]) != 0) and (hand.cards[3].val != hand.cards[0].val) and (hand.cards[2].suit == hand.cards[4].suit):
			hand_classes[9] += 1
		# Mutation Resistance: 82.85 percent
		if (hand.cards[0].suit != hand.cards[1].suit):
			hand_classes[3] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[2].suit == hand.cards[0].suit) and (hand.cards[1].suit == hand.cards[3].suit):
			hand_classes[9] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.val == 7]) != 1):
			hand_classes[7] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[0].suit == hand.cards[2].suit) and (hand.cards[4].suit == hand.cards[2].suit) and (len([card for card in hand.cards if card.val == 3]) != 4):
			hand_classes[8] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.suit == 4]) != 3):
			hand_classes[5] += 1
		# Mutation Resistance: 62.48 percent
		if (len([card for card in hand.cards if card.val == 5]) == 0) and (len([card for card in hand.cards if card.val == 11]) == 0):
			hand_classes[2] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[0].suit == hand.cards[4].suit):
			hand_classes[5] += 1
		# Mutation Resistance: 83.33 percent
		if (hand.cards[3].suit != hand.cards[1].suit) and (hand.cards[2].val == hand.cards[3].val) and (hand.cards[2].suit != hand.cards[0].suit):
			hand_classes[7] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.val == 11]) != 0) and (len([card for card in hand.cards if card.val == 10]) != 0) and (hand.cards[3].val != hand.cards[0].val) and (hand.cards[2].suit == hand.cards[4].suit):
			hand_classes[9] += 1
		# Mutation Resistance: 26.36 percent
		if (hand.cards[1].val < 7) and (len([card for card in hand.cards if card.suit == 1]) == 2):
			hand_classes[1] += 1
		# Mutation Resistance: 0.00 percent
		if ((hand.cards[0].val - hand.cards[3].val) == 10) and (len([card for card in hand.cards if card.suit == 3]) != 3) and (hand.cards[2].val == hand.cards[0].val):
			hand_classes[8] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.val == 11]) != 0) and (hand.cards[3].val != hand.cards[0].val) and (len([card for card in hand.cards if card.val == 10]) != 0) and (hand.cards[2].suit == hand.cards[4].suit):
			hand_classes[9] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.val == 8]) != 1):
			hand_classes[6] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[3].val != hand.cards[0].val) and (len([card for card in hand.cards if card.val == 11]) != 0) and (len([card for card in hand.cards if card.val == 10]) != 0) and (hand.cards[2].suit == hand.cards[4].suit):
			hand_classes[9] += 1
		# Mutation Resistance: 83.33 percent
		if (hand.cards[2].val == hand.cards[3].val) and (hand.cards[2].suit != hand.cards[0].suit) and (hand.cards[3].suit != hand.cards[1].suit):
			hand_classes[7] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[3].val != hand.cards[0].val) and (len([card for card in hand.cards if card.val == 10]) != 0) and (hand.cards[2].suit == hand.cards[4].suit) and (len([card for card in hand.cards if card.val == 11]) != 0):
			hand_classes[9] += 1
		# Mutation Resistance: 69.44 percent
		if (hand.cards[2].val != hand.cards[3].val) and (len([card for card in hand.cards if card.suit == 2]) != 5):
			hand_classes[6] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[0].suit == hand.cards[4].suit):
			hand_classes[5] += 1
		# Mutation Resistance: 41.32 percent
		if (len([card for card in hand.cards if card.val == 2]) != 1) and (len([card for card in hand.cards if card.suit == 2]) != 3) and (hand.cards[4].val < 8) and (hand.cards[0].suit != hand.cards[1].suit):
			hand_classes[2] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[1].val != hand.cards[4].val) and (hand.cards[3].val != hand.cards[1].val):
			hand_classes[4] += 1
		# Mutation Resistance: 80.00 percent
		if (hand.cards[0].val < 7):
			hand_classes[8] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[3].suit != hand.cards[0].suit) and (hand.cards[2].suit != hand.cards[0].suit):
			hand_classes[7] += 1
		# Mutation Resistance: 61.57 percent
		if (len([card for card in hand.cards if card.val == 13]) != 1) and (hand.cards[0].val < 9):
			hand_classes[2] += 1
		# Mutation Resistance: 33.33 percent
		if (hand.cards[1].val == hand.cards[4].val):
			hand_classes[6] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.val == 3]) != 4) and (hand.cards[4].suit == hand.cards[2].suit) and (hand.cards[0].suit == hand.cards[2].suit):
			hand_classes[8] += 1
		# Mutation Resistance: 80.00 percent
		if (hand.cards[0].val < 7):
			hand_classes[8] += 1
		# Mutation Resistance: 0.00 percent
		if (hand.cards[3].val != hand.cards[1].val) and (hand.cards[2].val != hand.cards[0].val) and (hand.cards[0].val == hand.cards[1].val) and (len([card for card in hand.cards if card.val == 3]) != 4) and (hand.cards[0].suit == hand.cards[1].suit) and (hand.cards[2].val == hand.cards[4].val) and (hand.cards[4].suit == hand.cards[3].suit) and (hand.cards[3].suit == hand.cards[1].suit) and (len([card for card in hand.cards if card.val == 5]) == 0):
			hand_classes[2] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.val == 10]) != 3):
			hand_classes[7] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[2].val != hand.cards[4].val) and (hand.cards[2].val != hand.cards[4].val) and (hand.cards[1].val != hand.cards[0].val):
			hand_classes[4] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.val == 11]) != 0) and (hand.cards[2].suit == hand.cards[4].suit) and (hand.cards[3].val != hand.cards[0].val) and (len([card for card in hand.cards if card.val == 10]) != 0):
			hand_classes[9] += 1
		# Mutation Resistance: 83.33 percent
		if (hand.cards[0].val == hand.cards[1].val):
			hand_classes[7] += 1
		# Mutation Resistance: 83.33 percent
		if (hand.cards[2].suit != hand.cards[0].suit) and (hand.cards[2].val == hand.cards[3].val) and (hand.cards[3].suit != hand.cards[1].suit):
			hand_classes[7] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[1].val != hand.cards[4].val) and (hand.cards[3].val != hand.cards[1].val):
			hand_classes[4] += 1
		# Mutation Resistance: 0.00 percent
		if ((hand.cards[0].val - hand.cards[1].val) == 1) and (hand.cards[4].val < 2) and (len([card for card in hand.cards if card.val == 4]) == 4) and (len([card for card in hand.cards if card.suit == 4]) != 2) and (len([card for card in hand.cards if card.suit == 2]) != 3) and (len([card for card in hand.cards if card.val == 3]) != 3) and (len([card for card in hand.cards if card.suit == 1]) == 5) and (hand.cards[2].val < 3) and (hand.cards[1].val != hand.cards[0].val):
			hand_classes[0] += 1
		# Mutation Resistance: 74.19 percent
		if (len([card for card in hand.cards if card.val == 3]) != 3) and (hand.cards[4].suit != hand.cards[0].suit):
			hand_classes[4] += 1
		# Mutation Resistance: 67.25 percent
		if (hand.cards[2].val != hand.cards[4].val):
			hand_classes[3] += 1
		# Mutation Resistance: 20.00 percent
		if (len([card for card in hand.cards if card.suit == 3]) != 0):
			hand_classes[9] += 1
		# Mutation Resistance: 0.00 percent
		if (len([card for card in hand.cards if card.val == 8]) != 1) and (hand.cards[2].val > 12) and (len([card for card in hand.cards if card.val == 8]) == 2) and (hand.cards[1].val > 3):
			hand_classes[9] += 1
		# Mutation Resistance: 83.33 percent
		if (hand.cards[0].val == hand.cards[1].val):
			hand_classes[7] += 1
		# Mutation Resistance: 85.77 percent
		if (len([card for card in hand.cards if card.suit == 2]) != 0):
			hand_classes[3] += 1
		# Mutation Resistance: 82.85 percent
		if (hand.cards[0].suit != hand.cards[1].suit):
			hand_classes[3] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[2].suit == hand.cards[0].suit) and (hand.cards[1].suit == hand.cards[3].suit):
			hand_classes[9] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[4].val > 3) and (hand.cards[3].val != hand.cards[0].val):
			hand_classes[8] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.val == 8]) != 1):
			hand_classes[6] += 1
		# Mutation Resistance: 80.00 percent
		if (hand.cards[0].val < 7):
			hand_classes[8] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.suit == 2]) != 5):
			hand_classes[3] += 1
		# Mutation Resistance: 82.85 percent
		if (hand.cards[0].suit != hand.cards[1].suit):
			hand_classes[3] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[2].val != hand.cards[4].val) and (hand.cards[2].val != hand.cards[4].val) and (hand.cards[1].val != hand.cards[0].val):
			hand_classes[4] += 1
		# Mutation Resistance: 0.00 percent
		if (hand.cards[3].val != hand.cards[2].val) and (len([card for card in hand.cards if card.val == 8]) == 4) and (len([card for card in hand.cards if card.val == 9]) != 2) and (len([card for card in hand.cards if card.val == 2]) == 4) and (hand.cards[2].val > 8) and (hand.cards[3].val != hand.cards[2].val):
			hand_classes[9] += 1
		# Mutation Resistance: 24.72 percent
		if (hand.cards[0].val == hand.cards[4].val):
			hand_classes[2] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.val == 6]) != 2):
			hand_classes[8] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[1].val != hand.cards[0].val) and (hand.cards[2].val != hand.cards[4].val) and (hand.cards[2].val != hand.cards[4].val):
			hand_classes[4] += 1
		# Mutation Resistance: 83.33 percent
		if (hand.cards[1].val == hand.cards[0].val):
			hand_classes[7] += 1
		# Mutation Resistance: 82.85 percent
		if (hand.cards[0].suit != hand.cards[1].suit):
			hand_classes[3] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[2].val != hand.cards[4].val) and (hand.cards[2].val != hand.cards[4].val) and (hand.cards[1].val != hand.cards[0].val):
			hand_classes[4] += 1
		# Mutation Resistance: 83.33 percent
		if (hand.cards[3].val == hand.cards[2].val) and (len([card for card in hand.cards if card.suit == 4]) != 4):
			hand_classes[7] += 1
		# Mutation Resistance: 80.00 percent
		if (hand.cards[0].val < 7):
			hand_classes[8] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[1].val != hand.cards[0].val) and (hand.cards[2].val != hand.cards[4].val) and (hand.cards[2].val != hand.cards[4].val):
			hand_classes[4] += 1
		# Mutation Resistance: 85.77 percent
		if (len([card for card in hand.cards if card.suit == 2]) != 0):
			hand_classes[3] += 1
		# Mutation Resistance: 1.17 percent
		if (hand.cards[3].val < 6) and (len([card for card in hand.cards if card.val == 4]) != 1) and (hand.cards[2].val < 9) and ((hand.cards[1].val - hand.cards[2].val) == 7):
			hand_classes[3] += 1
		# Mutation Resistance: 71.15 percent
		if (hand.cards[0].val != hand.cards[2].val):
			hand_classes[3] += 1
		# Mutation Resistance: 16.67 percent
		if (hand.cards[2].suit == hand.cards[0].suit):
			hand_classes[6] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[0].suit == hand.cards[4].suit):
			hand_classes[5] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[1].val != hand.cards[4].val) and (hand.cards[3].val != hand.cards[1].val):
			hand_classes[4] += 1
		# Mutation Resistance: 82.85 percent
		if (hand.cards[0].suit != hand.cards[1].suit):
			hand_classes[3] += 1
		# Mutation Resistance: 80.00 percent
		if (hand.cards[3].val < 9) and (len([card for card in hand.cards if card.suit == 1]) != 3) and (hand.cards[1].val < 7):
			hand_classes[8] += 1
		# Mutation Resistance: 91.94 percent
		if (hand.cards[0].val < 12):
			hand_classes[2] += 1
		# Mutation Resistance: 0.00 percent
		if (len([card for card in hand.cards if card.val == 6]) == 1) and (hand.cards[0].val < 5) and (hand.cards[0].val > 10):
			hand_classes[3] += 1
		# Mutation Resistance: 80.00 percent
		if (hand.cards[0].val < 7):
			hand_classes[8] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.val == 10]) != 0) and (hand.cards[2].suit == hand.cards[4].suit) and (len([card for card in hand.cards if card.val == 11]) != 0) and (hand.cards[3].val != hand.cards[0].val):
			hand_classes[9] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[2].suit == hand.cards[4].suit) and (hand.cards[3].val != hand.cards[0].val) and (len([card for card in hand.cards if card.val == 11]) != 0) and (len([card for card in hand.cards if card.val == 10]) != 0):
			hand_classes[9] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.suit == 4]) != 3):
			hand_classes[5] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[2].suit == hand.cards[4].suit):
			hand_classes[8] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[2].val != hand.cards[1].val):
			hand_classes[5] += 1
		# Mutation Resistance: 0.00 percent
		if (hand.cards[3].val < 11) and (hand.cards[3].val == hand.cards[1].val) and (len([card for card in hand.cards if card.val == 9]) == 3) and (hand.cards[2].val != hand.cards[4].val) and (len([card for card in hand.cards if card.val == 2]) == 3) and (hand.cards[0].val > 4) and (hand.cards[4].val == hand.cards[2].val) and (hand.cards[2].suit != hand.cards[0].suit) and (hand.cards[1].val < 10) and (hand.cards[4].val > 8) and (hand.cards[3].val < 2) and (len([card for card in hand.cards if card.val == 11]) == 4) and (hand.cards[1].suit != hand.cards[3].suit) and (len([card for card in hand.cards if card.val == 4]) != 3) and (len([card for card in hand.cards if card.val == 2]) != 4) and (hand.cards[2].val > 4) and (len([card for card in hand.cards if card.suit == 3]) != 1) and (hand.cards[3].val == hand.cards[4].val) and (len([card for card in hand.cards if card.val == 7]) != 3) and (len([card for card in hand.cards if card.val == 9]) == 1):
			hand_classes[0] += 1
		# Mutation Resistance: 79.57 percent
		if (hand.cards[1].val != hand.cards[4].val) and (hand.cards[3].val != hand.cards[1].val) and (hand.cards[0].suit != hand.cards[2].suit):
			hand_classes[4] += 1
		# Mutation Resistance: 79.57 percent
		if (hand.cards[3].val != hand.cards[1].val) and (hand.cards[0].suit != hand.cards[2].suit) and (hand.cards[1].val != hand.cards[4].val):
			hand_classes[4] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[0].suit == hand.cards[4].suit):
			hand_classes[5] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[3].val != hand.cards[1].val) and (hand.cards[1].val != hand.cards[4].val):
			hand_classes[4] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.val == 7]) != 1):
			hand_classes[7] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[3].val != hand.cards[0].val) and (hand.cards[2].suit == hand.cards[4].suit) and (len([card for card in hand.cards if card.val == 10]) != 0) and (len([card for card in hand.cards if card.val == 11]) != 0):
			hand_classes[9] += 1
		# Mutation Resistance: 79.57 percent
		if (len([card for card in hand.cards if card.suit == 3]) != 5) and (hand.cards[2].suit != hand.cards[0].suit):
			hand_classes[4] += 1
		# Mutation Resistance: 0.00 percent
		if (len([card for card in hand.cards if card.val == 6]) == 2) and (hand.cards[0].suit == hand.cards[4].suit):
			hand_classes[0] += 1
		# Mutation Resistance: 75.27 percent
		if (hand.cards[2].val != hand.cards[4].val) and (hand.cards[1].suit != hand.cards[2].suit):
			hand_classes[4] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[2].suit != hand.cards[0].suit) and (hand.cards[3].suit != hand.cards[0].suit):
			hand_classes[7] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.suit == 4]) != 3):
			hand_classes[5] += 1
		# Mutation Resistance: 0.00 percent
		if (hand.cards[1].val != hand.cards[3].val) and (hand.cards[1].val == hand.cards[0].val) and (hand.cards[2].suit == hand.cards[3].suit) and (len([card for card in hand.cards if card.val == 6]) != 1) and ((hand.cards[2].val - hand.cards[4].val) == -6) and (hand.cards[4].val < 2) and (hand.cards[4].val > 9) and (hand.cards[0].val == hand.cards[3].val) and (len([card for card in hand.cards if card.suit == 3]) == 0) and (hand.cards[3].val < 9) and (len([card for card in hand.cards if card.suit == 1]) != 1):
			hand_classes[0] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[3].val != hand.cards[0].val) and (len([card for card in hand.cards if card.val == 10]) != 0) and (hand.cards[2].suit == hand.cards[4].suit) and (len([card for card in hand.cards if card.val == 11]) != 0):
			hand_classes[9] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.val == 10]) != 0) and (hand.cards[2].suit == hand.cards[4].suit) and (hand.cards[3].val != hand.cards[0].val) and (len([card for card in hand.cards if card.val == 11]) != 0):
			hand_classes[9] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[2].suit == hand.cards[4].suit) and (hand.cards[3].val != hand.cards[0].val) and (len([card for card in hand.cards if card.val == 11]) != 0) and (len([card for card in hand.cards if card.val == 10]) != 0):
			hand_classes[9] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[0].suit == hand.cards[2].suit) and (len([card for card in hand.cards if card.val == 3]) != 4) and (hand.cards[4].suit == hand.cards[2].suit):
			hand_classes[8] += 1
		# Mutation Resistance: 20.00 percent
		if (len([card for card in hand.cards if card.suit == 1]) == 0) and (hand.cards[1].val > 12) and (hand.cards[0].val != hand.cards[4].val) and (hand.cards[0].val > 7):
			hand_classes[9] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[0].val != hand.cards[1].val) and (len([card for card in hand.cards if card.val == 6]) != 4):
			hand_classes[5] += 1
		# Mutation Resistance: 0.00 percent
		if (len([card for card in hand.cards if card.val == 6]) == 2) and (len([card for card in hand.cards if card.suit == 3]) != 5) and (hand.cards[4].val > 4) and (hand.cards[3].val == hand.cards[0].val):
			hand_classes[8] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.suit == 2]) != 5):
			hand_classes[3] += 1
		# Mutation Resistance: 79.57 percent
		if (len([card for card in hand.cards if card.suit == 3]) != 5) and (hand.cards[2].suit != hand.cards[0].suit):
			hand_classes[4] += 1
		# Mutation Resistance: 82.85 percent
		if (hand.cards[0].suit != hand.cards[1].suit):
			hand_classes[3] += 1
		# Mutation Resistance: 100.00 percent
		if (len([card for card in hand.cards if card.val == 12]) != 2):
			hand_classes[3] += 1
		# Mutation Resistance: 100.00 percent
		if (hand.cards[1].suit == hand.cards[3].suit) and (hand.cards[2].suit == hand.cards[0].suit):
			hand_classes[9] += 1
		# Mutation Resistance: 220.00 percent
		if (hand.cards[3].val != hand.cards[0].val):
			hand_classes[0] += 1
		# Mutation Resistance: 0.00 percent
		if ((hand.cards[0].val - hand.cards[1].val) == 6) and (hand.cards[0].suit != hand.cards[3].suit) and ((hand.cards[3].val - hand.cards[1].val) == -7) and (len([card for card in hand.cards if card.val == 11]) == 4) and (hand.cards[3].val < 5) and (len([card for card in hand.cards if card.suit == 4]) != 1) and ((hand.cards[2].val - hand.cards[1].val) == -5) and (hand.cards[0].suit == hand.cards[3].suit) and (hand.cards[4].val != hand.cards[3].val):
			hand_classes[5] += 1
		# Mutation Resistance: 180.28 percent
		if (hand.cards[4].val != hand.cards[2].val):
			hand_classes[1] += 1
		# Mutation Resistance: 53.09 percent
		if (hand.cards[2].val != hand.cards[0].val) and (hand.cards[2].suit == hand.cards[3].suit):
			hand_classes[0] += 1
		# Mutation Resistance: 0.00 percent
		if (len([card for card in hand.cards if card.suit == 2]) == 2) and (len([card for card in hand.cards if card.val == 8]) == 4) and (hand.cards[2].val > 5) and (hand.cards[0].val < 13):
			hand_classes[0] += 1
		# Mutation Resistance: 0.00 percent
		if (hand.cards[3].val != hand.cards[4].val) and (hand.cards[4].suit != hand.cards[2].suit) and (len([card for card in hand.cards if card.val == 8]) == 4) and (hand.cards[0].val > 10) and (hand.cards[3].suit == hand.cards[4].suit) and (hand.cards[2].val != hand.cards[0].val) and (hand.cards[1].val != hand.cards[4].val) and (hand.cards[1].val < 9) and (hand.cards[0].val != hand.cards[4].val) and (hand.cards[1].val != hand.cards[4].val):
			hand_classes[2] += 1
		# Mutation Resistance: 0.00 percent
		if (len([card for card in hand.cards if card.val == 4]) == 1) and (hand.cards[2].val == hand.cards[4].val) and (hand.cards[1].val != hand.cards[3].val) and (hand.cards[0].suit == hand.cards[2].suit) and (len([card for card in hand.cards if card.val == 1]) != 2):
			hand_classes[9] += 1
		# Mutation Resistance: 36.11 percent
		if (len([card for card in hand.cards if card.val == 1]) != 3) and (hand.cards[1].val == hand.cards[0].val):
			hand_classes[6] += 1
		# Mutation Resistance: 0.00 percent
		if (hand.cards[2].val < 7) and (hand.cards[0].val < 11) and (hand.cards[4].val < 10) and (hand.cards[0].val != hand.cards[1].val) and (hand.cards[2].val == hand.cards[0].val) and (hand.cards[4].val == hand.cards[1].val) and (hand.cards[4].val == hand.cards[1].val) and ((hand.cards[0].val - hand.cards[4].val) == -9) and (hand.cards[2].val < 8) and (hand.cards[3].val != hand.cards[1].val):
			hand_classes[0] += 1
		# Mutation Resistance: 0.00 percent
		if (len([card for card in hand.cards if card.val == 5]) == 2) and (hand.cards[0].suit == hand.cards[4].suit) and ((hand.cards[4].val - hand.cards[0].val) == 1) and (hand.cards[1].suit == hand.cards[3].suit) and (len([card for card in hand.cards if card.suit == 1]) == 2):
			hand_classes[4] += 1
		# Mutation Resistance: 0.00 percent
		if (len([card for card in hand.cards if card.suit == 2]) == 3) and (hand.cards[0].val == hand.cards[2].val) and (len([card for card in hand.cards if card.suit == 3]) == 0) and ((hand.cards[1].val - hand.cards[0].val) == 9) and ((hand.cards[3].val - hand.cards[2].val) == -8) and (hand.cards[2].val < 10) and (len([card for card in hand.cards if card.val == 5]) == 0) and (hand.cards[4].suit != hand.cards[2].suit) and (hand.cards[2].val < 8) and (hand.cards[0].suit == hand.cards[4].suit):
			hand_classes[3] += 1
		# Mutation Resistance: 0.00 percent
		if (hand.cards[4].val == hand.cards[0].val) and (hand.cards[2].val < 11) and (len([card for card in hand.cards if card.suit == 1]) == 0) and (len([card for card in hand.cards if card.val == 9]) == 3) and (hand.cards[2].val < 7):
			hand_classes[5] += 1
		# Mutation Resistance: 0.00 percent
		if ((hand.cards[3].val - hand.cards[2].val) == 10) and (hand.cards[1].val == hand.cards[4].val) and (hand.cards[2].suit != hand.cards[0].suit):
			hand_classes[5] += 1
		# Mutation Resistance: 0.00 percent
		if ((hand.cards[3].val - hand.cards[4].val) == 11) and (hand.cards[1].suit == hand.cards[2].suit) and (len([card for card in hand.cards if card.suit == 2]) != 3) and (len([card for card in hand.cards if card.suit == 1]) != 4) and (hand.cards[3].suit != hand.cards[1].suit) and (len([card for card in hand.cards if card.suit == 2]) != 4) and (hand.cards[3].val < 11) and (len([card for card in hand.cards if card.val == 7]) != 1):
			hand_classes[5] += 1
		# Mutation Resistance: 0.00 percent
		if (len([card for card in hand.cards if card.val == 5]) != 2) and (len([card for card in hand.cards if card.suit == 1]) != 1) and ((hand.cards[0].val - hand.cards[2].val) == 5) and (hand.cards[4].suit != hand.cards[2].suit) and (len([card for card in hand.cards if card.val == 4]) == 3) and (hand.cards[0].suit == hand.cards[1].suit) and (hand.cards[3].val != hand.cards[1].val) and (len([card for card in hand.cards if card.val == 10]) == 0):
			hand_classes[7] += 1
		# Mutation Resistance: 5.34 percent
		if ((hand.cards[1].val - hand.cards[4].val) == -9):
			hand_classes[0] += 1
		# Mutation Resistance: 0.00 percent
		if (hand.cards[1].val == hand.cards[4].val) and (len([card for card in hand.cards if card.suit == 2]) != 1) and (hand.cards[3].val == hand.cards[0].val) and (len([card for card in hand.cards if card.suit == 1]) != 0) and (len([card for card in hand.cards if card.suit == 3]) == 2) and (hand.cards[3].val == hand.cards[2].val) and (hand.cards[4].suit != hand.cards[1].suit) and (hand.cards[1].val > 12) and (len([card for card in hand.cards if card.suit == 3]) != 3) and (len([card for card in hand.cards if card.suit == 2]) == 1) and ((hand.cards[2].val - hand.cards[4].val) == -11) and (hand.cards[4].suit == hand.cards[2].suit) and (hand.cards[1].val < 10) and (len([card for card in hand.cards if card.suit == 1]) == 0):
			hand_classes[1] += 1
		# Mutation Resistance: 0.00 percent
		if (len([card for card in hand.cards if card.val == 1]) != 2) and (len([card for card in hand.cards if card.suit == 1]) != 0) and (len([card for card in hand.cards if card.val == 3]) == 4) and (hand.cards[1].val > 8) and (hand.cards[2].val < 8) and (len([card for card in hand.cards if card.suit == 4]) == 4) and (hand.cards[4].val == hand.cards[0].val) and (len([card for card in hand.cards if card.val == 7]) == 0) and (len([card for card in hand.cards if card.suit == 4]) != 4) and (hand.cards[4].val != hand.cards[1].val):
			hand_classes[9] += 1
		# Mutation Resistance: 6.50 percent
		if (len([card for card in hand.cards if card.suit == 3]) != 5) and (len([card for card in hand.cards if card.val == 1]) != 3) and (hand.cards[0].val != hand.cards[4].val) and (hand.cards[2].suit == hand.cards[1].suit) and (hand.cards[0].val != hand.cards[4].val) and (len([card for card in hand.cards if card.val == 4]) != 0) and (hand.cards[4].val < 6) and (len([card for card in hand.cards if card.suit == 3]) != 0):
			hand_classes[0] += 1
		# Mutation Resistance: 2.78 percent
		if (len([card for card in hand.cards if card.suit == 1]) != 2) and (hand.cards[3].val == hand.cards[1].val) and (hand.cards[4].val != hand.cards[2].val) and (hand.cards[2].suit != hand.cards[4].suit) and (hand.cards[1].val > 9):
			hand_classes[6] += 1
		# Mutation Resistance: 0.00 percent
		if (len([card for card in hand.cards if card.val == 4]) != 4) and (len([card for card in hand.cards if card.suit == 2]) == 1) and (len([card for card in hand.cards if card.val == 12]) == 2) and (hand.cards[4].val == hand.cards[1].val) and (hand.cards[1].val == hand.cards[2].val) and (hand.cards[4].suit == hand.cards[1].suit) and (len([card for card in hand.cards if card.val == 12]) == 2) and (len([card for card in hand.cards if card.suit == 1]) == 3) and (hand.cards[3].val == hand.cards[2].val) and (hand.cards[3].suit != hand.cards[4].suit) and (len([card for card in hand.cards if card.val == 11]) == 0) and (len([card for card in hand.cards if card.suit == 2]) != 1) and (len([card for card in hand.cards if card.suit == 2]) == 4) and (hand.cards[1].suit == hand.cards[3].suit):
			hand_classes[9] += 1
		# Mutation Resistance: 0.00 percent
		if (hand.cards[2].val == hand.cards[3].val):
			hand_classes[9] += 1
		# Mutation Resistance: 0.00 percent
		if (hand.cards[2].val > 10) and (len([card for card in hand.cards if card.val == 3]) == 2) and (hand.cards[1].val == hand.cards[4].val) and (hand.cards[1].val < 6) and (len([card for card in hand.cards if card.val == 13]) != 4) and (hand.cards[4].val < 4) and (len([card for card in hand.cards if card.val == 12]) != 3):
			hand_classes[6] += 1
		# Mutation Resistance: 0.00 percent
		if (len([card for card in hand.cards if card.suit == 4]) == 4) and (len([card for card in hand.cards if card.val == 6]) != 0):
			hand_classes[6] += 1
		# Mutation Resistance: 0.00 percent
		if (hand.cards[3].val == hand.cards[4].val) and ((hand.cards[0].val - hand.cards[3].val) == -10) and (len([card for card in hand.cards if card.suit == 4]) != 3):
			hand_classes[3] += 1
		# Mutation Resistance: 0.00 percent
		if (len([card for card in hand.cards if card.suit == 1]) == 1) and (len([card for card in hand.cards if card.val == 3]) == 3) and (len([card for card in hand.cards if card.val == 13]) == 3) and (len([card for card in hand.cards if card.val == 1]) != 3) and (len([card for card in hand.cards if card.val == 10]) != 4):
			hand_classes[3] += 1
		# Mutation Resistance: 4.87 percent
		if (hand.cards[2].suit == hand.cards[0].suit) and (len([card for card in hand.cards if card.suit == 2]) != 4) and (len([card for card in hand.cards if card.suit == 2]) != 2) and (hand.cards[0].suit == hand.cards[3].suit) and (len([card for card in hand.cards if card.val == 13]) == 0) and (len([card for card in hand.cards if card.val == 2]) != 2) and (len([card for card in hand.cards if card.suit == 1]) != 4):
			hand_classes[1] += 1
		# Mutation Resistance: 11.11 percent
		if (len([card for card in hand.cards if card.val == 5]) != 0) and (hand.cards[0].val < 11) and (hand.cards[3].val != hand.cards[0].val):
			hand_classes[6] += 1
		# Mutation Resistance: 0.00 percent
		if (len([card for card in hand.cards if card.suit == 3]) == 5) and (hand.cards[0].val > 6) and (len([card for card in hand.cards if card.val == 7]) == 1) and ((hand.cards[3].val - hand.cards[0].val) == 1) and ((hand.cards[2].val - hand.cards[0].val) == 12) and (hand.cards[4].suit == hand.cards[3].suit) and (hand.cards[1].suit == hand.cards[3].suit):
			hand_classes[0] += 1
		# Mutation Resistance: 0.00 percent
		if (hand.cards[1].val > 3) and (len([card for card in hand.cards if card.val == 4]) != 4) and (len([card for card in hand.cards if card.suit == 3]) == 2) and (len([card for card in hand.cards if card.suit == 1]) == 2) and (len([card for card in hand.cards if card.suit == 3]) != 5):
			hand_classes[7] += 1

		if max(hand_classes) > 0:
			hand.assigned_class = hand_classes.index(max(hand_classes))
		else:
			hand.assigned_class = 1
