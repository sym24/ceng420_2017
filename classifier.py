# Fitness: 472.505062108
def classify(hand):
	hand_confidences = [0 for i in range(10)]
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].suit != hand.cards[4].suit) and (hand.cards[2].suit == hand.cards[1].suit) and (len([card for card in hand.cards if card.val == 12]) != 3) and (hand.cards[3].val != hand.cards[2].val):
		hand_confidences[0] += 70
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].suit != hand.cards[1].suit):
		hand_confidences[0] += 20
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 3]) != 5) and (len([card for card in hand.cards if card.suit == 4]) != 2) and (hand.cards[4].val != hand.cards[0].val):
		hand_confidences[0] += 75
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 3]) == 0) and (hand.cards[0].val > 10) and (len([card for card in hand.cards if card.val == 6]) != 4):
		hand_confidences[0] += -25
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val > 3) and (hand.cards[3].suit == hand.cards[0].suit):
		hand_confidences[0] += -10
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val == hand.cards[1].val):
		hand_confidences[0] += -100
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val == hand.cards[3].val) and ((hand.cards[2].val - hand.cards[0].val) == 4):
		hand_confidences[0] += -40
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 2]) != 2) and ((hand.cards[0].val - hand.cards[4].val) == -2) and (hand.cards[3].suit != hand.cards[0].suit) and (hand.cards[1].val < 12):
		hand_confidences[0] += -25
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val != hand.cards[0].val) and (len([card for card in hand.cards if card.suit == 3]) != 5) and (len([card for card in hand.cards if card.suit == 4]) != 4):
		hand_confidences[0] += 20
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 4]) != 2) and (len([card for card in hand.cards if card.val == 5]) == 1) and (hand.cards[3].val == hand.cards[4].val) and (hand.cards[2].val < 10) and (hand.cards[2].val < 6) and (len([card for card in hand.cards if card.val == 11]) == 2) and (hand.cards[4].suit == hand.cards[0].suit) and (len([card for card in hand.cards if card.suit == 2]) != 0):
		hand_confidences[0] += 95
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 6]) == 3) and (len([card for card in hand.cards if card.val == 2]) != 0) and (hand.cards[2].suit != hand.cards[0].suit) and (hand.cards[1].val < 12) and (len([card for card in hand.cards if card.suit == 1]) == 2) and (hand.cards[1].val > 6) and (hand.cards[3].val != hand.cards[0].val) and (len([card for card in hand.cards if card.val == 11]) != 4):
		hand_confidences[0] += -95
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 3]) == 2) and (hand.cards[0].val == hand.cards[1].val) and ((hand.cards[4].val - hand.cards[0].val) == 7) and (hand.cards[1].suit == hand.cards[0].suit) and (hand.cards[1].val != hand.cards[0].val) and (hand.cards[0].val == hand.cards[1].val) and (hand.cards[2].val > 8) and (len([card for card in hand.cards if card.val == 12]) == 1):
		hand_confidences[0] += 35
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val > 12) and (len([card for card in hand.cards if card.suit == 4]) != 4) and (len([card for card in hand.cards if card.val == 4]) == 4) and (len([card for card in hand.cards if card.suit == 4]) != 1):
		hand_confidences[0] += 60
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 3]) == 1) and (len([card for card in hand.cards if card.suit == 4]) == 2) and (len([card for card in hand.cards if card.suit == 4]) != 4) and (len([card for card in hand.cards if card.suit == 4]) != 3) and (hand.cards[4].val > 6) and (hand.cards[4].val > 9):
		hand_confidences[0] += -70
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 8]) == 0) and (hand.cards[4].val < 7) and ((hand.cards[1].val - hand.cards[0].val) == -9) and (len([card for card in hand.cards if card.suit == 1]) != 0) and (hand.cards[1].suit != hand.cards[0].suit) and (hand.cards[2].val == hand.cards[0].val) and (len([card for card in hand.cards if card.suit == 1]) == 1) and (len([card for card in hand.cards if card.val == 8]) != 1) and (hand.cards[2].val > 9) and (len([card for card in hand.cards if card.suit == 3]) != 3) and (len([card for card in hand.cards if card.suit == 4]) != 3) and (len([card for card in hand.cards if card.suit == 3]) != 3):
		hand_confidences[0] += -45
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 13]) != 2) and (len([card for card in hand.cards if card.suit == 3]) == 5) and (len([card for card in hand.cards if card.val == 9]) != 0) and (len([card for card in hand.cards if card.suit == 3]) != 0) and (hand.cards[1].suit == hand.cards[3].suit) and (hand.cards[1].suit != hand.cards[2].suit) and (hand.cards[1].suit == hand.cards[2].suit) and (hand.cards[0].val != hand.cards[3].val) and ((hand.cards[1].val - hand.cards[3].val) == -3) and (hand.cards[0].suit != hand.cards[3].suit) and (len([card for card in hand.cards if card.suit == 3]) == 1) and (len([card for card in hand.cards if card.suit == 1]) == 1):
		hand_confidences[0] += -35
	
	# Mutation Resistance: 0.0%
	if ((hand.cards[0].val - hand.cards[4].val) == -1) and (len([card for card in hand.cards if card.val == 1]) == 3) and (hand.cards[2].suit != hand.cards[3].suit) and (hand.cards[3].val == hand.cards[0].val):
		hand_confidences[0] += 75
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 6]) == 1) and (hand.cards[3].val < 5) and ((hand.cards[2].val - hand.cards[1].val) == 11) and (len([card for card in hand.cards if card.val == 6]) != 2) and ((hand.cards[2].val - hand.cards[0].val) == 12):
		hand_confidences[0] += 10
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val == hand.cards[1].val) and (hand.cards[4].val == hand.cards[0].val) and (hand.cards[1].val != hand.cards[3].val) and (hand.cards[4].val == hand.cards[2].val) and (hand.cards[1].val < 3) and (hand.cards[0].val != hand.cards[3].val) and (hand.cards[3].suit != hand.cards[1].suit) and (len([card for card in hand.cards if card.val == 6]) != 3) and (hand.cards[2].val == hand.cards[4].val) and (hand.cards[4].val > 10) and (len([card for card in hand.cards if card.val == 2]) != 2) and (hand.cards[2].val != hand.cards[0].val):
		hand_confidences[0] += 95
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].suit != hand.cards[4].suit) and (hand.cards[4].suit == hand.cards[1].suit) and (hand.cards[4].val < 6) and ((hand.cards[1].val - hand.cards[3].val) == -8):
		hand_confidences[0] += 60
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val > 8) and (len([card for card in hand.cards if card.suit == 2]) == 2) and (hand.cards[4].val != hand.cards[1].val) and (len([card for card in hand.cards if card.val == 2]) != 1) and ((hand.cards[4].val - hand.cards[0].val) == -10) and ((hand.cards[0].val - hand.cards[2].val) == -8) and (len([card for card in hand.cards if card.suit == 1]) == 2):
		hand_confidences[1] += -20
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 1]) != 4) and (hand.cards[1].suit == hand.cards[2].suit) and (hand.cards[2].val != hand.cards[4].val) and (len([card for card in hand.cards if card.suit == 1]) == 4) and (hand.cards[1].suit == hand.cards[4].suit):
		hand_confidences[1] += -90
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].suit != hand.cards[1].suit) and (len([card for card in hand.cards if card.val == 11]) != 4) and (hand.cards[3].val != hand.cards[0].val):
		hand_confidences[1] += -15
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val > 11) and (hand.cards[1].val != hand.cards[2].val) and (hand.cards[4].suit == hand.cards[2].suit):
		hand_confidences[1] += 25
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].val < 11) and (hand.cards[2].val != hand.cards[0].val) and (hand.cards[1].val != hand.cards[0].val) and ((hand.cards[1].val - hand.cards[0].val) == 8) and (len([card for card in hand.cards if card.val == 9]) != 3) and (hand.cards[4].val == hand.cards[3].val) and (len([card for card in hand.cards if card.suit == 2]) != 1) and (hand.cards[3].suit != hand.cards[2].suit):
		hand_confidences[1] += -75
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val != hand.cards[1].val):
		hand_confidences[1] += 80
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 13]) != 2):
		hand_confidences[1] += -80
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val != hand.cards[4].val) and (hand.cards[3].suit != hand.cards[0].suit):
		hand_confidences[1] += 60
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].suit != hand.cards[0].suit) and (hand.cards[4].val != hand.cards[1].val):
		hand_confidences[1] += 60
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val != hand.cards[1].val) and (hand.cards[3].suit != hand.cards[0].suit):
		hand_confidences[1] += 65
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val > 12) and (hand.cards[4].val != hand.cards[2].val) and (hand.cards[3].suit != hand.cards[2].suit) and (hand.cards[0].suit != hand.cards[2].suit):
		hand_confidences[1] += 85
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].suit == hand.cards[4].suit) and ((hand.cards[2].val - hand.cards[1].val) == -8) and (len([card for card in hand.cards if card.val == 11]) != 2) and (hand.cards[4].val < 11) and (len([card for card in hand.cards if card.val == 12]) == 0):
		hand_confidences[1] += -65
	
	# Mutation Resistance: 0.0%
	if ((hand.cards[1].val - hand.cards[3].val) == 4) and (len([card for card in hand.cards if card.val == 10]) == 3) and (len([card for card in hand.cards if card.val == 5]) != 4) and (len([card for card in hand.cards if card.suit == 2]) != 5) and (len([card for card in hand.cards if card.val == 12]) == 3) and (hand.cards[2].val > 11):
		hand_confidences[1] += -50
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 3]) == 2) and (len([card for card in hand.cards if card.suit == 3]) == 4):
		hand_confidences[1] += -40
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val > 1) and (hand.cards[2].val > 2) and (hand.cards[0].val > 1) and (len([card for card in hand.cards if card.val == 10]) != 4) and (hand.cards[1].val > 2):
		hand_confidences[2] += 30
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].suit != hand.cards[3].suit) and (hand.cards[2].val == hand.cards[0].val) and ((hand.cards[4].val - hand.cards[2].val) == 9) and (hand.cards[2].val > 8) and (hand.cards[1].val < 11) and (hand.cards[4].val == hand.cards[2].val):
		hand_confidences[2] += -25
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val != hand.cards[4].val):
		hand_confidences[2] += 60
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 2]) != 2) and (len([card for card in hand.cards if card.val == 10]) != 2):
		hand_confidences[2] += -100
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val != hand.cards[4].val):
		hand_confidences[2] += 5
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].val != hand.cards[2].val) and (hand.cards[1].val != hand.cards[2].val):
		hand_confidences[2] += 10
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 4]) != 2) and (len([card for card in hand.cards if card.val == 11]) != 3):
		hand_confidences[2] += -95
	
	# Mutation Resistance: 0.0%
	if ((hand.cards[2].val - hand.cards[4].val) == 12) and (hand.cards[0].val < 2) and (len([card for card in hand.cards if card.val == 2]) == 2) and ((hand.cards[2].val - hand.cards[1].val) == 9) and ((hand.cards[4].val - hand.cards[1].val) == -7) and (hand.cards[4].val == hand.cards[1].val):
		hand_confidences[2] += 40
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].suit != hand.cards[3].suit):
		hand_confidences[2] += -10
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 3]) != 2) and (len([card for card in hand.cards if card.val == 12]) != 2):
		hand_confidences[2] += -30
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 12]) != 2) and (len([card for card in hand.cards if card.val == 7]) != 2):
		hand_confidences[2] += -80
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 12]) != 1) and (len([card for card in hand.cards if card.suit == 3]) != 4):
		hand_confidences[2] += 65
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].val != hand.cards[0].val) and (hand.cards[0].suit != hand.cards[1].suit) and (hand.cards[0].val != hand.cards[2].val) and (len([card for card in hand.cards if card.val == 7]) != 0) and (hand.cards[2].val != hand.cards[3].val) and ((hand.cards[3].val - hand.cards[1].val) == 11) and (len([card for card in hand.cards if card.suit == 1]) == 4) and (len([card for card in hand.cards if card.suit == 3]) != 4) and (hand.cards[1].val < 8) and (hand.cards[2].val < 6) and (hand.cards[3].suit != hand.cards[1].suit) and (hand.cards[3].val != hand.cards[4].val):
		hand_confidences[2] += -5
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].val != hand.cards[2].val) and (hand.cards[1].val != hand.cards[2].val):
		hand_confidences[2] += 40
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].val == hand.cards[3].val) and (len([card for card in hand.cards if card.suit == 4]) == 0) and (hand.cards[1].val < 3) and (len([card for card in hand.cards if card.suit == 1]) == 3) and (hand.cards[3].suit == hand.cards[4].suit) and (len([card for card in hand.cards if card.val == 8]) == 2) and (len([card for card in hand.cards if card.suit == 2]) != 0):
		hand_confidences[2] += 90
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val != hand.cards[4].val):
		hand_confidences[2] += 90
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 3]) != 2) and (len([card for card in hand.cards if card.val == 6]) != 2):
		hand_confidences[2] += -5
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val != hand.cards[4].val):
		hand_confidences[2] += 30
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val != hand.cards[4].val):
		hand_confidences[2] += 70
	
	# Mutation Resistance: 0.0%
	if ((hand.cards[0].val - hand.cards[4].val) == -12) and (hand.cards[0].val == hand.cards[3].val) and (len([card for card in hand.cards if card.suit == 4]) != 5) and (hand.cards[2].val != hand.cards[4].val) and (hand.cards[0].val > 2):
		hand_confidences[2] += 25
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val > 10) and (len([card for card in hand.cards if card.suit == 2]) == 2) and (len([card for card in hand.cards if card.val == 3]) == 3) and (len([card for card in hand.cards if card.val == 7]) == 4):
		hand_confidences[2] += -15
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 4]) == 1) and (hand.cards[3].val > 9) and (hand.cards[2].val == hand.cards[0].val) and (hand.cards[2].val == hand.cards[4].val) and (hand.cards[0].suit != hand.cards[3].suit):
		hand_confidences[2] += -80
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val < 6) and (hand.cards[1].val != hand.cards[4].val) and (len([card for card in hand.cards if card.val == 10]) == 2) and (hand.cards[3].val > 5) and (len([card for card in hand.cards if card.suit == 4]) == 4) and (len([card for card in hand.cards if card.val == 1]) == 1) and (hand.cards[4].suit != hand.cards[0].suit) and (hand.cards[0].val == hand.cards[1].val) and (hand.cards[1].suit == hand.cards[2].suit):
		hand_confidences[2] += 90
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val < 6) and (hand.cards[1].val == hand.cards[3].val) and (len([card for card in hand.cards if card.suit == 4]) != 2) and (hand.cards[0].suit == hand.cards[4].suit) and (len([card for card in hand.cards if card.suit == 1]) != 1):
		hand_confidences[2] += 10
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val != hand.cards[1].val) and (len([card for card in hand.cards if card.suit == 2]) != 5):
		hand_confidences[3] += 65
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 4]) != 5) and (hand.cards[3].val != hand.cards[1].val):
		hand_confidences[3] += 35
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 4]) != 5) and (hand.cards[3].val != hand.cards[1].val):
		hand_confidences[3] += 50
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 2]) != 3) and (hand.cards[3].val != hand.cards[1].val):
		hand_confidences[3] += 5
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val != hand.cards[3].val) and (hand.cards[4].val != hand.cards[0].val):
		hand_confidences[3] += -95
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val != hand.cards[2].val) and (hand.cards[4].val != hand.cards[1].val):
		hand_confidences[3] += -5
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val != hand.cards[1].val) and (len([card for card in hand.cards if card.suit == 3]) != 5):
		hand_confidences[3] += 20
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val != hand.cards[1].val) and (hand.cards[4].val != hand.cards[2].val):
		hand_confidences[3] += -35
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 3]) != 4):
		hand_confidences[3] += 30
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val != hand.cards[2].val) and (hand.cards[0].val != hand.cards[2].val):
		hand_confidences[3] += -90
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 3]) != 5) and (hand.cards[3].val != hand.cards[1].val):
		hand_confidences[3] += 35
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val != hand.cards[1].val) and (hand.cards[1].val != hand.cards[0].val):
		hand_confidences[3] += -25
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val != hand.cards[1].val) and (len([card for card in hand.cards if card.suit == 4]) != 5):
		hand_confidences[3] += 5
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 3]) != 5) and (hand.cards[3].val != hand.cards[1].val):
		hand_confidences[3] += 65
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val != hand.cards[1].val) and (hand.cards[0].val != hand.cards[2].val):
		hand_confidences[3] += -70
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val != hand.cards[1].val) and (len([card for card in hand.cards if card.suit == 1]) != 5):
		hand_confidences[3] += 75
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val != hand.cards[1].val) and (hand.cards[0].val != hand.cards[3].val):
		hand_confidences[3] += -85
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val != hand.cards[1].val) and (hand.cards[0].val != hand.cards[3].val):
		hand_confidences[3] += -85
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val != hand.cards[1].val) and (len([card for card in hand.cards if card.suit == 4]) != 5):
		hand_confidences[3] += 70
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 3]) != 4):
		hand_confidences[3] += 55
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 1]) != 4) and (hand.cards[4].val != hand.cards[3].val) and (hand.cards[3].val != hand.cards[0].val):
		hand_confidences[3] += -20
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val != hand.cards[1].val) and (hand.cards[1].val != hand.cards[3].val):
		hand_confidences[3] += -95
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val != hand.cards[3].val) and (hand.cards[3].val != hand.cards[1].val):
		hand_confidences[3] += -75
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val != hand.cards[2].val) and (hand.cards[1].val != hand.cards[0].val):
		hand_confidences[3] += -100
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 3]) != 5) and (hand.cards[3].val != hand.cards[1].val):
		hand_confidences[3] += 70
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val != hand.cards[0].val) and (hand.cards[4].val != hand.cards[3].val):
		hand_confidences[3] += -5
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 9]) != 4) and (hand.cards[3].val == hand.cards[1].val) and (len([card for card in hand.cards if card.suit == 2]) != 1) and (len([card for card in hand.cards if card.val == 10]) == 2) and (len([card for card in hand.cards if card.suit == 2]) == 2) and (len([card for card in hand.cards if card.suit == 1]) != 0):
		hand_confidences[3] += -70
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 3]) != 4):
		hand_confidences[3] += 10
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].val != hand.cards[2].val) and (hand.cards[0].val != hand.cards[3].val):
		hand_confidences[3] += -65
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val != hand.cards[3].val) and (hand.cards[4].val != hand.cards[2].val):
		hand_confidences[3] += -15
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val == hand.cards[4].val) and (hand.cards[3].val < 4) and (len([card for card in hand.cards if card.suit == 3]) != 2) and (hand.cards[4].suit != hand.cards[0].suit) and (hand.cards[4].suit != hand.cards[1].suit) and (hand.cards[3].val != hand.cards[1].val) and (hand.cards[1].val > 12) and (len([card for card in hand.cards if card.val == 2]) != 0) and (hand.cards[0].val == hand.cards[3].val) and (hand.cards[3].val == hand.cards[4].val) and (len([card for card in hand.cards if card.val == 5]) == 1) and (hand.cards[4].suit == hand.cards[1].suit) and ((hand.cards[1].val - hand.cards[2].val) == -4) and ((hand.cards[2].val - hand.cards[1].val) == 3) and (len([card for card in hand.cards if card.suit == 3]) == 1):
		hand_confidences[3] += 85
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].suit == hand.cards[3].suit) and (len([card for card in hand.cards if card.suit == 3]) != 4) and (len([card for card in hand.cards if card.suit == 2]) != 1) and ((hand.cards[0].val - hand.cards[2].val) == -1) and (len([card for card in hand.cards if card.suit == 3]) == 1):
		hand_confidences[3] += -85
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val > 4) and (hand.cards[2].suit != hand.cards[1].suit) and (hand.cards[2].val > 2) and (hand.cards[3].suit == hand.cards[0].suit) and (hand.cards[3].suit != hand.cards[2].suit):
		hand_confidences[3] += 85
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].suit == hand.cards[1].suit) and (hand.cards[3].val != hand.cards[2].val) and (len([card for card in hand.cards if card.val == 3]) != 4) and (hand.cards[3].val < 6) and (len([card for card in hand.cards if card.suit == 4]) != 0) and (hand.cards[0].suit == hand.cards[1].suit) and (len([card for card in hand.cards if card.suit == 4]) != 2) and ((hand.cards[2].val - hand.cards[1].val) == -2) and (hand.cards[4].val != hand.cards[3].val) and (len([card for card in hand.cards if card.val == 8]) != 0):
		hand_confidences[3] += 15
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 9]) == 3) and (hand.cards[3].val != hand.cards[4].val):
		hand_confidences[4] += -15
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].suit == hand.cards[3].suit) and ((hand.cards[0].val - hand.cards[2].val) == 3) and (hand.cards[4].val == hand.cards[0].val) and (hand.cards[2].val > 9) and (hand.cards[3].val > 5) and (len([card for card in hand.cards if card.suit == 3]) != 1) and (len([card for card in hand.cards if card.suit == 2]) != 3) and (hand.cards[1].val == hand.cards[4].val) and ((hand.cards[0].val - hand.cards[2].val) == 6):
		hand_confidences[4] += -75
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val < 4) and (len([card for card in hand.cards if card.val == 5]) == 0):
		hand_confidences[4] += -70
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 10]) != 0) and (len([card for card in hand.cards if card.suit == 1]) != 4) and (hand.cards[4].suit == hand.cards[1].suit) and (hand.cards[2].val > 1) and (hand.cards[4].val != hand.cards[3].val) and (hand.cards[2].suit != hand.cards[4].suit) and (hand.cards[1].val < 5) and (hand.cards[4].val < 5):
		hand_confidences[4] += -95
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val != hand.cards[0].val) and (hand.cards[1].val > 1) and (hand.cards[1].suit != hand.cards[4].suit):
		hand_confidences[4] += 10
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].val != hand.cards[4].val) and (hand.cards[0].val < 3) and (hand.cards[0].val > 2) and (hand.cards[2].suit != hand.cards[3].suit):
		hand_confidences[4] += -95
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val == hand.cards[4].val) and (hand.cards[2].val == hand.cards[0].val) and (len([card for card in hand.cards if card.suit == 2]) != 0):
		hand_confidences[4] += -75
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 13]) == 0) and (len([card for card in hand.cards if card.val == 13]) != 4) and (len([card for card in hand.cards if card.suit == 2]) == 0) and (len([card for card in hand.cards if card.val == 6]) == 1) and (len([card for card in hand.cards if card.val == 3]) != 0) and ((hand.cards[1].val - hand.cards[2].val) == -4) and (hand.cards[2].suit != hand.cards[0].suit):
		hand_confidences[4] += 25
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].suit != hand.cards[1].suit) and (len([card for card in hand.cards if card.val == 4]) == 1):
		hand_confidences[4] += 70
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 8]) != 2) and (hand.cards[0].val == hand.cards[4].val) and ((hand.cards[1].val - hand.cards[3].val) == -8):
		hand_confidences[4] += 10
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 11]) == 1):
		hand_confidences[4] += 20
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].suit != hand.cards[3].suit) and (len([card for card in hand.cards if card.suit == 2]) != 5):
		hand_confidences[4] += 35
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val == hand.cards[0].val):
		hand_confidences[4] += -80
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 11]) == 1):
		hand_confidences[4] += 80
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 4]) == 1):
		hand_confidences[4] += 70
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 5]) != 0) and (hand.cards[1].suit == hand.cards[4].suit) and ((hand.cards[2].val - hand.cards[3].val) == 7) and (len([card for card in hand.cards if card.val == 10]) == 3) and (len([card for card in hand.cards if card.val == 11]) != 1) and (hand.cards[0].suit != hand.cards[2].suit) and (hand.cards[2].val < 2) and (hand.cards[3].val == hand.cards[2].val) and ((hand.cards[1].val - hand.cards[0].val) == 2) and (len([card for card in hand.cards if card.val == 12]) != 1):
		hand_confidences[4] += 25
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 7]) != 0) and ((hand.cards[0].val - hand.cards[4].val) == 9) and ((hand.cards[2].val - hand.cards[1].val) == -12) and (hand.cards[4].val != hand.cards[3].val) and (hand.cards[4].val > 9) and (hand.cards[1].val < 10):
		hand_confidences[4] += 45
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].suit != hand.cards[0].suit) and (len([card for card in hand.cards if card.suit == 1]) == 5) and (len([card for card in hand.cards if card.suit == 2]) != 4):
		hand_confidences[4] += -85
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val == hand.cards[3].val) and (hand.cards[0].val < 2) and (len([card for card in hand.cards if card.val == 13]) == 2) and ((hand.cards[1].val - hand.cards[2].val) == -5) and (len([card for card in hand.cards if card.suit == 3]) == 3) and (hand.cards[3].val > 12):
		hand_confidences[4] += -95
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].suit != hand.cards[0].suit):
		hand_confidences[4] += 5
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 11]) != 2):
		hand_confidences[4] += -10
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 4]) == 5) and (hand.cards[4].suit == hand.cards[0].suit) and (hand.cards[3].val < 10) and (hand.cards[4].val == hand.cards[3].val) and (hand.cards[4].val != hand.cards[0].val) and (hand.cards[3].val > 9) and (len([card for card in hand.cards if card.val == 12]) == 2) and (len([card for card in hand.cards if card.val == 8]) == 2) and (len([card for card in hand.cards if card.suit == 4]) == 0) and ((hand.cards[1].val - hand.cards[0].val) == -4) and (hand.cards[0].val == hand.cards[1].val) and (hand.cards[1].val != hand.cards[2].val) and (len([card for card in hand.cards if card.suit == 3]) != 0) and (hand.cards[2].val < 3) and (hand.cards[1].suit != hand.cards[4].suit):
		hand_confidences[4] += -80
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val == hand.cards[4].val) and (hand.cards[2].val != hand.cards[4].val) and ((hand.cards[2].val - hand.cards[0].val) == -10) and (len([card for card in hand.cards if card.suit == 1]) == 0) and (hand.cards[2].val == hand.cards[1].val):
		hand_confidences[4] += 80
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val == hand.cards[3].val) and (len([card for card in hand.cards if card.val == 5]) != 1) and (hand.cards[4].suit == hand.cards[0].suit) and (len([card for card in hand.cards if card.val == 8]) == 1) and (hand.cards[4].val != hand.cards[1].val) and (len([card for card in hand.cards if card.suit == 2]) == 2):
		hand_confidences[4] += 40
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val == hand.cards[1].val) and (hand.cards[1].suit != hand.cards[0].suit) and (hand.cards[4].val < 12) and (hand.cards[1].suit == hand.cards[4].suit):
		hand_confidences[4] += -10
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].suit != hand.cards[4].suit):
		hand_confidences[5] += -55
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val != hand.cards[3].val) and (hand.cards[0].suit == hand.cards[2].suit) and (len([card for card in hand.cards if card.suit == 4]) != 3) and (len([card for card in hand.cards if card.suit == 1]) != 2):
		hand_confidences[5] += 45
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].suit != hand.cards[1].suit):
		hand_confidences[5] += -80
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 4]) != 2) and ((hand.cards[3].val - hand.cards[1].val) == -3) and (hand.cards[3].suit == hand.cards[2].suit):
		hand_confidences[5] += -50
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].suit != hand.cards[1].suit):
		hand_confidences[5] += -90
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 6]) != 2):
		hand_confidences[5] += 40
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 7]) != 1):
		hand_confidences[5] += -100
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 13]) == 4) and (len([card for card in hand.cards if card.val == 10]) == 1) and (hand.cards[1].val == hand.cards[0].val) and (len([card for card in hand.cards if card.val == 3]) != 0):
		hand_confidences[5] += -95
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val == hand.cards[1].val) and (hand.cards[3].val != hand.cards[0].val) and (len([card for card in hand.cards if card.val == 2]) != 1) and (hand.cards[1].val > 1) and (len([card for card in hand.cards if card.suit == 3]) == 1) and (len([card for card in hand.cards if card.suit == 2]) != 5) and (len([card for card in hand.cards if card.suit == 1]) == 1):
		hand_confidences[5] += -25
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val > 1) and (hand.cards[3].val != hand.cards[4].val) and (hand.cards[2].suit == hand.cards[3].suit):
		hand_confidences[5] += 25
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].suit == hand.cards[3].suit) and (hand.cards[3].val != hand.cards[4].val) and (hand.cards[0].val > 1):
		hand_confidences[5] += 55
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 6]) != 2):
		hand_confidences[5] += 15
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 12]) == 1) and (len([card for card in hand.cards if card.suit == 1]) != 0):
		hand_confidences[5] += 70
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].suit == hand.cards[0].suit):
		hand_confidences[5] += 45
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].suit != hand.cards[2].suit):
		hand_confidences[5] += -95
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val > 1) and (hand.cards[2].suit == hand.cards[3].suit) and (hand.cards[3].val != hand.cards[4].val):
		hand_confidences[5] += 100
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].suit != hand.cards[2].suit):
		hand_confidences[5] += -95
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].suit != hand.cards[2].suit):
		hand_confidences[5] += -45
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 4]) == 4) and (len([card for card in hand.cards if card.val == 11]) != 4) and (hand.cards[3].val < 13) and (hand.cards[0].val == hand.cards[3].val):
		hand_confidences[5] += 20
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val == hand.cards[1].val):
		hand_confidences[5] += 60
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 1]) == 5) and (hand.cards[0].val != hand.cards[3].val) and (len([card for card in hand.cards if card.suit == 3]) != 3) and ((hand.cards[1].val - hand.cards[3].val) == -7) and (len([card for card in hand.cards if card.val == 4]) != 4):
		hand_confidences[5] += 55
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 12]) != 1):
		hand_confidences[6] += 35
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val != hand.cards[1].val):
		hand_confidences[6] += -5
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].suit != hand.cards[1].suit) and (hand.cards[1].suit != hand.cards[4].suit):
		hand_confidences[6] += 100
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val == hand.cards[0].val):
		hand_confidences[6] += 75
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 12]) != 1):
		hand_confidences[6] += 35
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val != hand.cards[0].val):
		hand_confidences[6] += -70
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val != hand.cards[3].val):
		hand_confidences[6] += -75
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 3]) != 0) and (len([card for card in hand.cards if card.val == 12]) != 1) and (len([card for card in hand.cards if card.val == 11]) != 0) and (hand.cards[4].suit != hand.cards[2].suit):
		hand_confidences[6] += 60
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val != hand.cards[3].val):
		hand_confidences[6] += -75
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 12]) != 1):
		hand_confidences[6] += 45
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val != hand.cards[3].val):
		hand_confidences[6] += -80
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val != hand.cards[1].val):
		hand_confidences[6] += -90
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val != hand.cards[3].val):
		hand_confidences[6] += -45
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].suit != hand.cards[2].suit) and (len([card for card in hand.cards if card.suit == 3]) != 0) and (len([card for card in hand.cards if card.val == 11]) != 1) and (len([card for card in hand.cards if card.val == 7]) != 1):
		hand_confidences[6] += 95
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val != hand.cards[2].val):
		hand_confidences[6] += -15
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val != hand.cards[2].val):
		hand_confidences[6] += -80
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val != hand.cards[1].val):
		hand_confidences[6] += -60
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 4]) != 0) and (hand.cards[0].val == hand.cards[3].val) and (hand.cards[4].suit != hand.cards[2].suit) and (hand.cards[1].val < 4) and (hand.cards[1].val > 6) and (len([card for card in hand.cards if card.suit == 2]) != 4) and ((hand.cards[1].val - hand.cards[4].val) == -9):
		hand_confidences[6] += 50
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].suit != hand.cards[1].suit) and (hand.cards[1].suit != hand.cards[4].suit):
		hand_confidences[6] += 85
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val != hand.cards[3].val):
		hand_confidences[6] += -40
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 11]) != 1) and (len([card for card in hand.cards if card.suit == 3]) != 0) and (hand.cards[3].suit != hand.cards[2].suit) and (len([card for card in hand.cards if card.val == 7]) != 1):
		hand_confidences[6] += 55
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val != hand.cards[3].val):
		hand_confidences[6] += -5
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].suit != hand.cards[4].suit) and (hand.cards[4].suit != hand.cards[1].suit):
		hand_confidences[6] += 95
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 12]) != 4):
		hand_confidences[6] += 60
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val == hand.cards[3].val):
		hand_confidences[6] += 60
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val != hand.cards[2].val):
		hand_confidences[6] += -90
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 3]) == 0):
		hand_confidences[6] += 15
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val != hand.cards[0].val) and (len([card for card in hand.cards if card.val == 6]) == 2) and (hand.cards[1].val > 9) and ((hand.cards[1].val - hand.cards[0].val) == 3):
		hand_confidences[6] += 5
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 3]) != 0) and (hand.cards[0].suit != hand.cards[2].suit) and (len([card for card in hand.cards if card.val == 11]) != 1) and (len([card for card in hand.cards if card.val == 7]) != 1):
		hand_confidences[6] += 90
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val != hand.cards[0].val):
		hand_confidences[6] += -25
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 4]) == 2):
		hand_confidences[6] += -15
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val != hand.cards[0].val):
		hand_confidences[6] += -90
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val != hand.cards[3].val):
		hand_confidences[6] += -55
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 12]) != 1):
		hand_confidences[6] += 80
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val != hand.cards[1].val):
		hand_confidences[6] += -60
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val != hand.cards[1].val):
		hand_confidences[6] += -85
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].suit != hand.cards[4].suit) and (hand.cards[4].suit != hand.cards[1].suit):
		hand_confidences[6] += 10
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val != hand.cards[3].val):
		hand_confidences[6] += -75
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 12]) == 1) and (len([card for card in hand.cards if card.val == 4]) != 2) and (hand.cards[4].suit == hand.cards[3].suit) and (hand.cards[0].val < 8) and (hand.cards[0].val > 5):
		hand_confidences[6] += -60
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val != hand.cards[0].val):
		hand_confidences[6] += -85
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 12]) != 1):
		hand_confidences[6] += 35
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val != hand.cards[0].val) and (len([card for card in hand.cards if card.suit == 4]) != 3) and (hand.cards[3].val < 8) and (hand.cards[2].val != hand.cards[0].val) and (len([card for card in hand.cards if card.val == 4]) == 2) and (len([card for card in hand.cards if card.val == 11]) != 3):
		hand_confidences[6] += -65
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 12]) != 1):
		hand_confidences[6] += 75
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 3]) != 0) and (len([card for card in hand.cards if card.val == 11]) != 1) and (len([card for card in hand.cards if card.val == 7]) != 1) and (hand.cards[3].suit != hand.cards[2].suit):
		hand_confidences[6] += 95
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 12]) != 1):
		hand_confidences[6] += 35
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val != hand.cards[1].val):
		hand_confidences[7] += -55
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val != hand.cards[3].val):
		hand_confidences[7] += -50
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 1]) == 5) and (hand.cards[3].suit == hand.cards[1].suit) and ((hand.cards[2].val - hand.cards[0].val) == 1) and (hand.cards[4].suit == hand.cards[3].suit) and (hand.cards[3].val != hand.cards[2].val) and (hand.cards[4].suit == hand.cards[2].suit) and (hand.cards[2].suit != hand.cards[1].suit) and (len([card for card in hand.cards if card.suit == 3]) != 1) and (hand.cards[0].val == hand.cards[1].val) and (hand.cards[0].suit != hand.cards[2].suit) and (hand.cards[1].val > 4) and (hand.cards[2].suit != hand.cards[0].suit) and (hand.cards[4].val == hand.cards[0].val) and (hand.cards[4].val == hand.cards[3].val) and (hand.cards[1].val == hand.cards[0].val):
		hand_confidences[7] += 90
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 4]) != 4) and (hand.cards[1].val == hand.cards[4].val) and (len([card for card in hand.cards if card.val == 4]) != 1) and (hand.cards[2].suit != hand.cards[1].suit) and (hand.cards[2].val == hand.cards[3].val):
		hand_confidences[7] += 75
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val != hand.cards[1].val):
		hand_confidences[7] += -75
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].suit != hand.cards[2].suit):
		hand_confidences[7] += 60
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].suit == hand.cards[4].suit) and (len([card for card in hand.cards if card.val == 12]) != 4) and (hand.cards[1].suit != hand.cards[0].suit) and (len([card for card in hand.cards if card.val == 1]) == 4) and (hand.cards[3].suit != hand.cards[0].suit) and (len([card for card in hand.cards if card.val == 5]) == 2) and (hand.cards[3].suit != hand.cards[1].suit):
		hand_confidences[7] += -85
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 2]) != 1) and (hand.cards[4].val < 5) and (hand.cards[3].suit == hand.cards[2].suit):
		hand_confidences[7] += -10
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val != hand.cards[4].val):
		hand_confidences[7] += -90
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val != hand.cards[1].val):
		hand_confidences[7] += -95
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val < 5) and ((hand.cards[1].val - hand.cards[0].val) == 1) and (len([card for card in hand.cards if card.val == 3]) == 2) and (hand.cards[2].val < 8) and (len([card for card in hand.cards if card.suit == 1]) == 3) and (len([card for card in hand.cards if card.val == 13]) == 0) and (hand.cards[4].val == hand.cards[0].val) and (hand.cards[4].suit != hand.cards[0].suit) and (hand.cards[4].val == hand.cards[1].val) and (len([card for card in hand.cards if card.val == 8]) == 0) and (len([card for card in hand.cards if card.suit == 2]) == 3) and (hand.cards[1].suit != hand.cards[2].suit) and (len([card for card in hand.cards if card.suit == 1]) == 5):
		hand_confidences[7] += -15
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].suit != hand.cards[0].suit) and (hand.cards[3].val > 4):
		hand_confidences[7] += 60
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].val != hand.cards[4].val) and (len([card for card in hand.cards if card.suit == 2]) != 2) and (len([card for card in hand.cards if card.val == 5]) != 4) and (hand.cards[1].val < 12):
		hand_confidences[7] += 40
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val < 13) and (hand.cards[4].val > 3):
		hand_confidences[7] += -10
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val == hand.cards[1].val) and (len([card for card in hand.cards if card.suit == 3]) != 2) and (len([card for card in hand.cards if card.val == 2]) != 1):
		hand_confidences[7] += 25
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 9]) == 1) and (hand.cards[2].val == hand.cards[0].val) and (hand.cards[3].val != hand.cards[0].val) and ((hand.cards[0].val - hand.cards[1].val) == -9) and (len([card for card in hand.cards if card.val == 13]) == 4) and (hand.cards[1].suit != hand.cards[4].suit) and (len([card for card in hand.cards if card.val == 2]) == 0) and (len([card for card in hand.cards if card.suit == 1]) == 2) and (hand.cards[3].val > 8) and ((hand.cards[2].val - hand.cards[0].val) == -11):
		hand_confidences[7] += 70
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 2]) == 1) and (hand.cards[2].suit != hand.cards[0].suit):
		hand_confidences[7] += 85
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 3]) != 2) and (len([card for card in hand.cards if card.val == 1]) != 1) and (hand.cards[0].val == hand.cards[1].val):
		hand_confidences[7] += 70
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].val == hand.cards[2].val) and (hand.cards[1].val < 13) and (hand.cards[1].val > 9) and (hand.cards[0].suit == hand.cards[3].suit) and (hand.cards[3].suit != hand.cards[2].suit) and (hand.cards[3].suit != hand.cards[0].suit) and (hand.cards[3].suit != hand.cards[4].suit) and (len([card for card in hand.cards if card.suit == 4]) == 2) and (hand.cards[3].val > 5):
		hand_confidences[7] += 40
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].val > 9) and (len([card for card in hand.cards if card.val == 2]) == 0) and (hand.cards[4].suit == hand.cards[2].suit) and (hand.cards[3].val == hand.cards[1].val) and (len([card for card in hand.cards if card.val == 4]) != 0) and (hand.cards[0].suit != hand.cards[4].suit) and (len([card for card in hand.cards if card.suit == 4]) != 2):
		hand_confidences[7] += -70
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 11]) != 2):
		hand_confidences[7] += -80
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].val < 13) and (len([card for card in hand.cards if card.suit == 1]) != 2):
		hand_confidences[7] += 60
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val == hand.cards[3].val) and (len([card for card in hand.cards if card.val == 7]) != 4) and (hand.cards[2].val > 9):
		hand_confidences[7] += 40
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val != hand.cards[1].val):
		hand_confidences[7] += -65
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val < 12) and (hand.cards[3].val == hand.cards[1].val):
		hand_confidences[7] += 100
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val == hand.cards[1].val) and (hand.cards[1].val < 5) and (len([card for card in hand.cards if card.suit == 1]) != 4) and (hand.cards[3].suit != hand.cards[1].suit) and (len([card for card in hand.cards if card.suit == 3]) != 2) and (hand.cards[4].suit != hand.cards[3].suit) and (hand.cards[1].suit == hand.cards[0].suit) and ((hand.cards[2].val - hand.cards[3].val) == 4) and (hand.cards[0].suit != hand.cards[3].suit):
		hand_confidences[7] += 20
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val != hand.cards[4].val):
		hand_confidences[7] += -95
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val != hand.cards[0].val):
		hand_confidences[7] += -85
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val < 12) and (hand.cards[3].val == hand.cards[1].val):
		hand_confidences[7] += 50
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val != hand.cards[0].val):
		hand_confidences[7] += -25
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val == hand.cards[1].val) and (hand.cards[2].val < 12):
		hand_confidences[7] += 60
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val != hand.cards[1].val):
		hand_confidences[7] += -100
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 7]) == 1) and (hand.cards[0].suit != hand.cards[3].suit) and (len([card for card in hand.cards if card.val == 3]) != 2) and (hand.cards[0].suit != hand.cards[1].suit) and (hand.cards[2].val == hand.cards[0].val) and (hand.cards[1].val == hand.cards[3].val) and (len([card for card in hand.cards if card.val == 12]) != 0):
		hand_confidences[7] += 20
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].suit == hand.cards[3].suit):
		hand_confidences[8] += 80
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 3]) != 5):
		hand_confidences[8] += -95
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 12]) == 3) and ((hand.cards[0].val - hand.cards[2].val) == -10):
		hand_confidences[8] += 65
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].suit != hand.cards[2].suit):
		hand_confidences[8] += -40
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val != hand.cards[0].val):
		hand_confidences[8] += -45
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 13]) != 1) and (hand.cards[4].suit != hand.cards[3].suit):
		hand_confidences[8] += 50
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val != hand.cards[0].val) and (hand.cards[3].val != hand.cards[4].val):
		hand_confidences[8] += 35
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].suit != hand.cards[0].suit):
		hand_confidences[8] += -95
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].suit == hand.cards[2].suit):
		hand_confidences[8] += 65
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val > 7) and (hand.cards[2].val > 4):
		hand_confidences[8] += 35
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val != hand.cards[2].val) and (len([card for card in hand.cards if card.val == 13]) != 2) and (hand.cards[0].val < 10):
		hand_confidences[8] += 45
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val != hand.cards[1].val):
		hand_confidences[8] += -15
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val > 3):
		hand_confidences[8] += -90
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].suit != hand.cards[2].suit):
		hand_confidences[8] += -65
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val == hand.cards[0].val) and (hand.cards[1].val < 13) and (len([card for card in hand.cards if card.suit == 1]) == 0):
		hand_confidences[8] += -65
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].val < 8):
		hand_confidences[8] += 70
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 5]) != 3) and (hand.cards[0].val < 3) and (hand.cards[1].val != hand.cards[2].val):
		hand_confidences[8] += 10
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val < 11) and (len([card for card in hand.cards if card.suit == 4]) != 4):
		hand_confidences[8] += -5
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].suit != hand.cards[1].suit):
		hand_confidences[8] += -5
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val != hand.cards[2].val) and (hand.cards[0].val < 10) and (len([card for card in hand.cards if card.val == 13]) != 2):
		hand_confidences[8] += 75
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 1]) != 5):
		hand_confidences[8] += -90
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val < 10) and (hand.cards[3].val != hand.cards[2].val) and (len([card for card in hand.cards if card.val == 13]) != 2):
		hand_confidences[8] += 40
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 13]) != 2) and (hand.cards[0].suit != hand.cards[3].suit):
		hand_confidences[8] += -40
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 1]) != 4):
		hand_confidences[8] += -65
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val != hand.cards[1].val):
		hand_confidences[8] += -50
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 2]) != 1) and (hand.cards[2].val != hand.cards[3].val):
		hand_confidences[8] += 20
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val != hand.cards[0].val) and (hand.cards[0].val != hand.cards[4].val):
		hand_confidences[8] += 65
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val != hand.cards[2].val) and (hand.cards[0].val < 10) and (len([card for card in hand.cards if card.val == 13]) != 2):
		hand_confidences[8] += 65
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].suit != hand.cards[1].suit):
		hand_confidences[8] += -35
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val != hand.cards[4].val) and (len([card for card in hand.cards if card.val == 7]) != 4):
		hand_confidences[8] += -95
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 1]) != 5):
		hand_confidences[8] += -35
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].val > 3) and (len([card for card in hand.cards if card.val == 10]) != 3) and (hand.cards[0].val < 8) and (hand.cards[4].val > 4) and (len([card for card in hand.cards if card.suit == 1]) != 0) and (len([card for card in hand.cards if card.val == 10]) != 4):
		hand_confidences[8] += 95
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 1]) != 5):
		hand_confidences[8] += -80
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val < 10) and (hand.cards[3].val != hand.cards[2].val) and (len([card for card in hand.cards if card.val == 13]) != 2):
		hand_confidences[8] += 70
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 3]) != 4) and (hand.cards[2].val != hand.cards[4].val):
		hand_confidences[8] += -55
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].suit == hand.cards[2].suit):
		hand_confidences[8] += 40
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].suit != hand.cards[2].suit):
		hand_confidences[8] += -40
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val != hand.cards[4].val) and (len([card for card in hand.cards if card.suit == 3]) != 2):
		hand_confidences[8] += 10
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val > 11):
		hand_confidences[8] += 70
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val != hand.cards[2].val) and (len([card for card in hand.cards if card.val == 13]) != 2) and (hand.cards[0].val < 10):
		hand_confidences[8] += 45
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].val < 12) and (len([card for card in hand.cards if card.val == 10]) == 4):
		hand_confidences[8] += 5
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 3]) == 0) and (hand.cards[2].val == hand.cards[4].val) and (hand.cards[4].suit == hand.cards[1].suit) and (hand.cards[3].val == hand.cards[1].val) and (hand.cards[3].val > 5) and (len([card for card in hand.cards if card.suit == 3]) != 1) and (len([card for card in hand.cards if card.val == 3]) == 2) and (hand.cards[1].val == hand.cards[4].val) and (hand.cards[0].val == hand.cards[1].val) and (len([card for card in hand.cards if card.suit == 1]) == 4) and (hand.cards[4].val > 3):
		hand_confidences[8] += -85
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].suit == hand.cards[0].suit):
		hand_confidences[9] += 75
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val > 1) and (len([card for card in hand.cards if card.val == 12]) != 1) and (hand.cards[1].val != hand.cards[4].val):
		hand_confidences[9] += -100
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val > 8) and (hand.cards[2].val == hand.cards[4].val) and (hand.cards[3].val != hand.cards[4].val) and (len([card for card in hand.cards if card.suit == 4]) == 1) and (hand.cards[2].val > 11) and (len([card for card in hand.cards if card.val == 6]) != 0):
		hand_confidences[9] += -5
	
	# Mutation Resistance: 0.0%
	if ((hand.cards[3].val - hand.cards[0].val) == -9) and (hand.cards[4].val != hand.cards[1].val) and (hand.cards[1].suit != hand.cards[0].suit) and (len([card for card in hand.cards if card.suit == 1]) != 1):
		hand_confidences[9] += 100
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val < 10):
		hand_confidences[9] += -100
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val > 5) and (len([card for card in hand.cards if card.val == 1]) == 1):
		hand_confidences[9] += 15
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val != hand.cards[1].val):
		hand_confidences[9] += 80
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 6]) == 3) and (hand.cards[4].suit == hand.cards[0].suit) and (hand.cards[1].suit == hand.cards[0].suit):
		hand_confidences[9] += -40
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 2]) != 3) and (hand.cards[2].val != hand.cards[1].val):
		hand_confidences[9] += -10
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val < 13):
		hand_confidences[9] += -70
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].suit != hand.cards[4].suit):
		hand_confidences[9] += -30
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].suit == hand.cards[2].suit) and (hand.cards[3].suit != hand.cards[2].suit) and (hand.cards[2].suit != hand.cards[3].suit) and (hand.cards[4].suit != hand.cards[1].suit):
		hand_confidences[9] += -90
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 9]) != 2) and (len([card for card in hand.cards if card.val == 10]) != 0) and (len([card for card in hand.cards if card.val == 4]) == 4):
		hand_confidences[9] += -95
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val != hand.cards[1].val):
		hand_confidences[9] += 55
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val == hand.cards[1].val) and (len([card for card in hand.cards if card.suit == 2]) != 1) and (hand.cards[0].suit == hand.cards[1].suit) and (hand.cards[4].suit != hand.cards[3].suit) and (hand.cards[0].val < 7) and (len([card for card in hand.cards if card.suit == 3]) != 2):
		hand_confidences[9] += -80
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val != hand.cards[1].val):
		hand_confidences[9] += 5
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val != hand.cards[4].val) and (len([card for card in hand.cards if card.val == 2]) != 3):
		hand_confidences[9] += -10
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val > 5) and (len([card for card in hand.cards if card.val == 1]) == 1):
		hand_confidences[9] += 60
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].suit != hand.cards[2].suit) and (hand.cards[1].val != hand.cards[3].val):
		hand_confidences[9] += -60
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val != hand.cards[1].val) and (len([card for card in hand.cards if card.val == 2]) != 3):
		hand_confidences[9] += -55
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].suit != hand.cards[4].suit):
		hand_confidences[9] += -45
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 1]) != 0) and (hand.cards[2].val != hand.cards[0].val) and (len([card for card in hand.cards if card.val == 13]) != 0):
		hand_confidences[9] += -5
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 3]) == 4) and (hand.cards[4].val < 7):
		hand_confidences[9] += 95
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 10]) != 1):
		hand_confidences[9] += -35
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 4]) != 1) and ((hand.cards[0].val - hand.cards[1].val) == 11) and (hand.cards[4].val > 12) and ((hand.cards[0].val - hand.cards[4].val) == -1) and (hand.cards[3].val > 8) and (hand.cards[3].suit != hand.cards[4].suit) and (hand.cards[3].suit != hand.cards[2].suit) and (len([card for card in hand.cards if card.suit == 3]) != 5) and (hand.cards[0].val == hand.cards[2].val) and (hand.cards[4].suit != hand.cards[3].suit) and (hand.cards[0].val < 10):
		hand_confidences[9] += -60
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 4]) != 1) and (hand.cards[3].suit == hand.cards[1].suit):
		hand_confidences[9] += -30
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].suit != hand.cards[4].suit):
		hand_confidences[9] += -65
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val < 10):
		hand_confidences[9] += -30
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val < 10):
		hand_confidences[9] += -90
	
	if max(hand_confidences) >= 100:
		hand.assigned_class = hand_confidences.index(max(hand_confidences))
	else:
		hand.assigned_class = 0
		
