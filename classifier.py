#Class 0 fitness: 1390.80
#Class 1 fitness: 1400.00
#Class 2 fitness: 1400.00
#Class 3 fitness: 1400.00
#Class 4 fitness: 1392.00
#Class 5 fitness: 1400.00
#Class 6 fitness: 1400.00
#Class 7 fitness: 1400.00
#Class 8 fitness: 1400.00
#Class 9 fitness: 1400.00
# Fitness: 998.070919715
def classify(hand):
	hand_confidences = [0 for i in range(10)]
	
	# Mutation Resistance: 231.087363494%
	if ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 4):
		hand_confidences[0] += -25
	
	# Mutation Resistance: 100.0%
	if (hand.cards[0].val != hand.cards[2].val):
		hand_confidences[0] += 15
	
	# Mutation Resistance: 231.087363494%
	if ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 4):
		hand_confidences[0] += -95
	
	# Mutation Resistance: 231.087363494%
	if ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 4):
		hand_confidences[0] += -15
	
	# Mutation Resistance: 100.0%
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 0) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 2):
		hand_confidences[0] += -25
	
	# Mutation Resistance: 75.338189386%
	if (hand.cards[1].suit != hand.cards[3].suit):
		hand_confidences[0] += 25
	
	# Mutation Resistance: 100.0%
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 0) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 2):
		hand_confidences[0] += -35
	
	# Mutation Resistance: 200.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1):
		hand_confidences[0] += -15
	
	# Mutation Resistance: 200.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1):
		hand_confidences[0] += -20
	
	# Mutation Resistance: 128.909491102%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 9]) == 1):
		hand_confidences[0] += -85
	
	# Mutation Resistance: 200.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 1):
		hand_confidences[0] += -75
	
	# Mutation Resistance: 128.27594284%
	if (hand.cards[4].val == hand.cards[3].val):
		hand_confidences[0] += -85
	
	# Mutation Resistance: 231.087363494%
	if ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 4):
		hand_confidences[0] += -30
	
	# Mutation Resistance: 128.27594284%
	if (hand.cards[4].val == hand.cards[3].val):
		hand_confidences[0] += -60
	
	# Mutation Resistance: 128.909491102%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 9]) == 1):
		hand_confidences[0] += -85
	
	# Mutation Resistance: 128.909491102%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 9]) == 1):
		hand_confidences[0] += -85
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val == hand.cards[2].val):
		hand_confidences[0] += 35
	
	# Mutation Resistance: 128.27594284%
	if (hand.cards[4].val == hand.cards[3].val):
		hand_confidences[0] += -75
	
	# Mutation Resistance: 128.27594284%
	if (hand.cards[4].val == hand.cards[3].val):
		hand_confidences[0] += -100
	
	# Mutation Resistance: 128.909491102%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 9]) == 1):
		hand_confidences[0] += -75
	
	# Mutation Resistance: 179.490713226%
	if (hand.cards[1].val == hand.cards[0].val):
		hand_confidences[0] += -95
	
	# Mutation Resistance: 200.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 1):
		hand_confidences[0] += -20
	
	# Mutation Resistance: 128.27594284%
	if (hand.cards[4].val == hand.cards[3].val):
		hand_confidences[0] += -95
	
	# Mutation Resistance: 200.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1):
		hand_confidences[0] += -80
	
	# Mutation Resistance: 200.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 1):
		hand_confidences[0] += -100
	
	# Mutation Resistance: 64.5161290323%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4) and (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[0] += -75
	
	# Mutation Resistance: 231.087363494%
	if ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 4):
		hand_confidences[0] += -20
	
	# Mutation Resistance: 200.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1):
		hand_confidences[0] += -40
	
	# Mutation Resistance: 75.2501400784%
	if (hand.cards[4].suit != hand.cards[3].suit):
		hand_confidences[0] += 65
	
	# Mutation Resistance: 333.05234099%
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(1) == 0):
		hand_confidences[0] += -80
	
	# Mutation Resistance: 100.0%
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 0) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 2):
		hand_confidences[0] += -95
	
	# Mutation Resistance: 200.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1):
		hand_confidences[0] += -75
	
	# Mutation Resistance: 100.0%
	if (hand.cards[0].val != hand.cards[2].val):
		hand_confidences[0] += 65
	
	# Mutation Resistance: 100.0%
	if (hand.cards[0].val != hand.cards[2].val):
		hand_confidences[0] += 75
	
	# Mutation Resistance: 5.27495397423%
	if (hand.cards[3].suit != hand.cards[1].suit) and ((hand.cards[0].val - hand.cards[3].val) == -2):
		hand_confidences[0] += 10
	
	# Mutation Resistance: 89.7160109444%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 1) and (hand.cards[4].val != hand.cards[0].val):
		hand_confidences[1] += 85
	
	# Mutation Resistance: 700.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0):
		hand_confidences[1] += -5
	
	# Mutation Resistance: 89.7160109444%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 1) and (hand.cards[4].val != hand.cards[0].val):
		hand_confidences[1] += 30
	
	# Mutation Resistance: 90.1783187093%
	if (hand.cards[0].val != hand.cards[3].val) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 3):
		hand_confidences[1] += 75
	
	# Mutation Resistance: 93.6623024037%
	if (hand.cards[0].val > 1) and (hand.cards[1].val > 8) and (hand.cards[0].suit == hand.cards[3].suit) and (hand.cards[2].val < 13) and (hand.cards[3].val > 8):
		hand_confidences[1] += -25
	
	# Mutation Resistance: 89.7160109444%
	if (hand.cards[4].val != hand.cards[0].val) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 1):
		hand_confidences[1] += 35
	
	# Mutation Resistance: 0.0%
	if ((hand.cards[0].val - hand.cards[4].val) == -2) and (hand.cards[1].suit != hand.cards[3].suit) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 3) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 5) and (hand.cards[2].suit != hand.cards[3].suit) and (hand.cards[4].val == hand.cards[0].val):
		hand_confidences[1] += -65
	
	# Mutation Resistance: 700.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0):
		hand_confidences[1] += -90
	
	# Mutation Resistance: 89.7160109444%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 1) and (hand.cards[4].val != hand.cards[0].val):
		hand_confidences[1] += 80
	
	# Mutation Resistance: 90.1783187093%
	if (hand.cards[0].val != hand.cards[3].val) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 3):
		hand_confidences[1] += 100
	
	# Mutation Resistance: 81.5057243205%
	if (hand.cards[4].suit != hand.cards[2].suit) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 0) and (hand.cards[1].suit == hand.cards[2].suit):
		hand_confidences[1] += -20
	
	# Mutation Resistance: 186.695602973%
	if (hand.cards[1].val == hand.cards[2].val):
		hand_confidences[2] += -25
	
	# Mutation Resistance: 100.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 1):
		hand_confidences[2] += 60
	
	# Mutation Resistance: 300.0%
	if (hand.cards[2].suit == hand.cards[1].suit) and (hand.cards[2].val != hand.cards[3].val) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 1) and (hand.cards[0].suit == hand.cards[4].suit):
		hand_confidences[2] += -20
	
	# Mutation Resistance: 87.1832358674%
	if (hand.cards[1].val == hand.cards[2].val) and (hand.cards[0].val == hand.cards[1].val) and (hand.cards[0].val < 11):
		hand_confidences[2] += -60
	
	# Mutation Resistance: 186.695602973%
	if (hand.cards[1].val == hand.cards[2].val):
		hand_confidences[2] += -35
	
	# Mutation Resistance: 186.695602973%
	if (hand.cards[1].val == hand.cards[2].val):
		hand_confidences[2] += -75
	
	# Mutation Resistance: 186.695602973%
	if (hand.cards[1].val == hand.cards[2].val):
		hand_confidences[2] += -20
	
	# Mutation Resistance: 72.4906426625%
	if (hand.cards[3].suit == hand.cards[0].suit) and (hand.cards[4].suit != hand.cards[1].suit) and (hand.cards[2].suit != hand.cards[1].suit):
		hand_confidences[2] += -15
	
	# Mutation Resistance: 100.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 1):
		hand_confidences[2] += 5
	
	# Mutation Resistance: 66.6666666667%
	if (hand.cards[2].val > 4) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(4) == 1) and (hand.cards[3].suit != hand.cards[4].suit):
		hand_confidences[2] += -70
	
	# Mutation Resistance: 100.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 1):
		hand_confidences[2] += 85
	
	# Mutation Resistance: 77.3631840796%
	if (hand.cards[4].val < 11) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 1):
		hand_confidences[2] += 20
	
	# Mutation Resistance: 326.016113872%
	if (hand.cards[3].val != hand.cards[4].val) and (hand.cards[4].suit == hand.cards[2].suit) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0):
		hand_confidences[2] += -35
	
	# Mutation Resistance: 100.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 1):
		hand_confidences[2] += 30
	
	# Mutation Resistance: 153.28679082%
	if (hand.cards[3].val == hand.cards[2].val):
		hand_confidences[2] += -55
	
	# Mutation Resistance: 186.695602973%
	if (hand.cards[1].val == hand.cards[2].val):
		hand_confidences[2] += -45
	
	# Mutation Resistance: 79.1873963516%
	if (hand.cards[3].val != hand.cards[1].val):
		hand_confidences[2] += 35
	
	# Mutation Resistance: 148.260754565%
	if (hand.cards[0].val < 8) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0) and (hand.cards[4].val < 10):
		hand_confidences[2] += -50
	
	# Mutation Resistance: 186.695602973%
	if (hand.cards[1].val == hand.cards[2].val):
		hand_confidences[2] += -20
	
	# Mutation Resistance: 187.096774194%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4):
		hand_confidences[2] += -15
	
	# Mutation Resistance: 100.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 1):
		hand_confidences[2] += 15
	
	# Mutation Resistance: 153.28679082%
	if (hand.cards[3].val == hand.cards[2].val):
		hand_confidences[2] += -90
	
	# Mutation Resistance: 300.0%
	if (hand.cards[2].suit == hand.cards[1].suit) and (hand.cards[0].suit == hand.cards[4].suit) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 1) and (hand.cards[2].val != hand.cards[3].val):
		hand_confidences[2] += -70
	
	# Mutation Resistance: 100.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 1):
		hand_confidences[2] += 90
	
	# Mutation Resistance: 95.6649198396%
	if (hand.cards[0].val != hand.cards[4].val) and (hand.cards[0].suit != hand.cards[4].suit) and (hand.cards[2].val == hand.cards[0].val):
		hand_confidences[2] += -65
	
	# Mutation Resistance: 187.096774194%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4):
		hand_confidences[2] += -85
	
	# Mutation Resistance: 100.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 1):
		hand_confidences[2] += 85
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val > 3) and (hand.cards[2].val != hand.cards[1].val) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 3]) == 4) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 4]) == 1) and ((hand.cards[4].val - hand.cards[3].val) == 5) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 10) and (hand.cards[1].val == hand.cards[2].val) and (hand.cards[1].val > 7) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 1) and (hand.cards[4].suit == hand.cards[1].suit) and (hand.cards[3].val < 10) and (hand.cards[2].val != hand.cards[0].val) and (hand.cards[3].suit != hand.cards[0].suit) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 1):
		hand_confidences[2] += -20
	
	# Mutation Resistance: 0.0%
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 1) and ((hand.cards[0].val - hand.cards[3].val) == 5) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0) and ((hand.cards[2].val - hand.cards[0].val) == -3) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 1) and ((hand.cards[3].val - hand.cards[2].val) == 12) and (hand.cards[1].val > 12) and (hand.cards[2].val < 3) and (hand.cards[3].val < 11) and ((hand.cards[2].val - hand.cards[3].val) == -1) and (hand.cards[1].val == hand.cards[0].val):
		hand_confidences[2] += -10
	
	# Mutation Resistance: 2.39645249552%
	if (hand.cards[4].val == hand.cards[3].val) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0):
		hand_confidences[2] += -80
	
	# Mutation Resistance: 0.0%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 2) and ((hand.cards[2].val - hand.cards[4].val) == -4) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 2) and ((hand.cards[0].val - hand.cards[1].val) == -4) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 10]) == 1):
		hand_confidences[2] += -85
	
	# Mutation Resistance: 458.903535492%
	if (hand.cards[1].val < 8):
		hand_confidences[3] += -20
	
	# Mutation Resistance: 100.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 2):
		hand_confidences[3] += 75
	
	# Mutation Resistance: 100.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 2):
		hand_confidences[3] += 65
	
	# Mutation Resistance: 90.0584795322%
	if (hand.cards[4].val > 1):
		hand_confidences[3] += 60
	
	# Mutation Resistance: 100.0%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 2):
		hand_confidences[3] += 5
	
	# Mutation Resistance: 100.0%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 2):
		hand_confidences[3] += 40
	
	# Mutation Resistance: 100.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 2):
		hand_confidences[3] += 80
	
	# Mutation Resistance: 113.908285282%
	if (hand.cards[4].val > 10) and (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[3] += -5
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].suit == hand.cards[3].suit) and (hand.cards[1].val == hand.cards[3].val) and (hand.cards[3].suit != hand.cards[2].suit) and (hand.cards[0].suit == hand.cards[1].suit):
		hand_confidences[3] += 25
	
	# Mutation Resistance: 115.053763441%
	if (hand.cards[1].suit == hand.cards[4].suit) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0) and (hand.cards[1].val != hand.cards[4].val):
		hand_confidences[3] += -50
	
	# Mutation Resistance: 100.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 2):
		hand_confidences[3] += 40
	
	# Mutation Resistance: 100.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 2):
		hand_confidences[3] += 20
	
	# Mutation Resistance: 4.82053691423%
	if (hand.cards[1].val < 2) and (hand.cards[1].val < 13) and (hand.cards[2].suit != hand.cards[3].suit) and (hand.cards[4].suit == hand.cards[1].suit):
		hand_confidences[3] += -100
	
	# Mutation Resistance: 115.053763441%
	if (hand.cards[1].val != hand.cards[4].val) and (hand.cards[1].suit == hand.cards[4].suit) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4):
		hand_confidences[3] += -60
	
	# Mutation Resistance: 0.0%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 2]) == 3) and (hand.cards[0].suit == hand.cards[1].suit) and (hand.cards[4].val == hand.cards[0].val) and (hand.cards[1].val == hand.cards[0].val) and (hand.cards[3].suit == hand.cards[2].suit) and (hand.cards[3].val > 3) and (hand.cards[3].suit == hand.cards[1].suit) and (hand.cards[3].suit != hand.cards[0].suit):
		hand_confidences[3] += 100
	
	# Mutation Resistance: 100.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 2):
		hand_confidences[3] += 85
	
	# Mutation Resistance: 100.0%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 2):
		hand_confidences[3] += 35
	
	# Mutation Resistance: 889.223155646%
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0):
		hand_confidences[3] += -95
	
	# Mutation Resistance: 743.316844313%
	if (hand.cards[3].val < 12):
		hand_confidences[3] += -100
	
	# Mutation Resistance: 100.0%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 2):
		hand_confidences[3] += 50
	
	# Mutation Resistance: 771.058708019%
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0):
		hand_confidences[3] += -65
	
	# Mutation Resistance: 115.053763441%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4) and (hand.cards[0].val < 10) and (hand.cards[3].suit == hand.cards[2].suit):
		hand_confidences[3] += -20
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].val != hand.cards[3].val) and (hand.cards[0].val > 1) and (hand.cards[2].val == hand.cards[1].val) and (hand.cards[2].val > 4) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0) and (hand.cards[1].val == hand.cards[3].val) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 10):
		hand_confidences[3] += -95
	
	# Mutation Resistance: 0.0%
	if ((hand.cards[1].val - hand.cards[4].val) == -12) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4) and (hand.cards[4].val < 9) and (hand.cards[2].val > 9):
		hand_confidences[3] += -80
	
	# Mutation Resistance: 5.06822612086%
	if (hand.cards[1].val == hand.cards[4].val) and (hand.cards[3].suit != hand.cards[0].suit) and (hand.cards[2].suit == hand.cards[0].suit):
		hand_confidences[3] += 5
	
	# Mutation Resistance: 100.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 5):
		hand_confidences[4] += 100
	
	# Mutation Resistance: 100.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 5):
		hand_confidences[4] += 75
	
	# Mutation Resistance: 100.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 3):
		hand_confidences[4] += -15
	
	# Mutation Resistance: 691.662605983%
	if (hand.cards[2].val != hand.cards[1].val):
		hand_confidences[4] += -45
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].val == hand.cards[3].val) and (hand.cards[2].val < 3) and (hand.cards[1].suit != hand.cards[3].suit) and (hand.cards[4].val > 10) and (hand.cards[2].val != hand.cards[0].val) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 1):
		hand_confidences[4] += -100
	
	# Mutation Resistance: 147.606985838%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 5) and (hand.cards[3].val < 7):
		hand_confidences[4] += -10
	
	# Mutation Resistance: 12.9032258065%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 3):
		hand_confidences[4] += 85
	
	# Mutation Resistance: 129.243389163%
	if (hand.cards[0].suit == hand.cards[1].suit) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0) and (hand.cards[2].val < 11) and (hand.cards[1].val != hand.cards[2].val) and (hand.cards[0].val < 8):
		hand_confidences[4] += -55
	
	# Mutation Resistance: 67.7419354839%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4) and (hand.cards[0].suit != hand.cards[1].suit):
		hand_confidences[4] += 10
	
	# Mutation Resistance: 389.600875379%
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0) and (hand.cards[1].suit == hand.cards[4].suit):
		hand_confidences[4] += -70
	
	# Mutation Resistance: 100.0%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 3) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1):
		hand_confidences[4] += -40
	
	# Mutation Resistance: 100.0%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 3) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1):
		hand_confidences[4] += -65
	
	# Mutation Resistance: 127.697547769%
	if (hand.cards[1].val == hand.cards[4].val):
		hand_confidences[4] += -5
	
	# Mutation Resistance: 79.9999743479%
	if (hand.cards[3].val == hand.cards[1].val) and (hand.cards[4].val > 8):
		hand_confidences[4] += -75
	
	# Mutation Resistance: 63.4408602151%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4) and (hand.cards[0].suit != hand.cards[3].suit):
		hand_confidences[4] += 65
	
	# Mutation Resistance: 100.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 5):
		hand_confidences[4] += 30
	
	# Mutation Resistance: 161.28170053%
	if (hand.cards[2].val > 8) and (hand.cards[1].val < 10):
		hand_confidences[4] += -35
	
	# Mutation Resistance: 389.600875379%
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0) and (hand.cards[1].suit == hand.cards[4].suit):
		hand_confidences[4] += -90
	
	# Mutation Resistance: 64.5161290323%
	if (hand.cards[0].suit != hand.cards[4].suit) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4):
		hand_confidences[4] += 60
	
	# Mutation Resistance: 72.0430107527%
	if (hand.cards[1].suit != hand.cards[4].suit) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4):
		hand_confidences[4] += 95
	
	# Mutation Resistance: 691.662605983%
	if (hand.cards[2].val != hand.cards[1].val):
		hand_confidences[4] += -70
	
	# Mutation Resistance: 499.738098135%
	if (hand.cards[3].suit != hand.cards[0].suit):
		hand_confidences[4] += -35
	
	# Mutation Resistance: 64.5161290323%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4) and (hand.cards[0].suit != hand.cards[4].suit):
		hand_confidences[4] += 80
	
	# Mutation Resistance: 100.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 5):
		hand_confidences[4] += 5
	
	# Mutation Resistance: 67.7419354839%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4) and (hand.cards[0].suit != hand.cards[1].suit):
		hand_confidences[4] += 85
	
	# Mutation Resistance: 389.600875379%
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0) and (hand.cards[1].suit == hand.cards[4].suit):
		hand_confidences[4] += -85
	
	# Mutation Resistance: 79.9999743479%
	if (hand.cards[3].val == hand.cards[1].val) and (hand.cards[4].val > 8):
		hand_confidences[4] += -25
	
	# Mutation Resistance: 0.0%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 2) and (hand.cards[0].suit != hand.cards[3].suit):
		hand_confidences[4] += 25
	
	# Mutation Resistance: 691.662605983%
	if (hand.cards[2].val != hand.cards[1].val):
		hand_confidences[4] += -25
	
	# Mutation Resistance: 68.8172043011%
	if (hand.cards[2].suit != hand.cards[3].suit) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4):
		hand_confidences[4] += 75
	
	# Mutation Resistance: 100.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 5):
		hand_confidences[4] += 30
	
	# Mutation Resistance: 12.9032258065%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 3):
		hand_confidences[4] += 75
	
	# Mutation Resistance: 67.7419354839%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4) and (hand.cards[0].suit != hand.cards[1].suit):
		hand_confidences[4] += 15
	
	# Mutation Resistance: 3.66515376335%
	if (hand.cards[2].suit != hand.cards[0].suit) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 11]) == 1):
		hand_confidences[4] += -10
	
	# Mutation Resistance: 67.7419354839%
	if (hand.cards[0].suit != hand.cards[1].suit) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4):
		hand_confidences[4] += 35
	
	# Mutation Resistance: 208.337394017%
	if (hand.cards[2].val == hand.cards[1].val):
		hand_confidences[4] += -100
	
	# Mutation Resistance: 100.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 3):
		hand_confidences[4] += -70
	
	# Mutation Resistance: 389.600875379%
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0) and (hand.cards[1].suit == hand.cards[4].suit):
		hand_confidences[4] += -40
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].suit == hand.cards[4].suit) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 11]) == 1) and (hand.cards[3].suit != hand.cards[4].suit) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 5) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 2]) == 4) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 5) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 6) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 12]) == 1) and (hand.cards[2].suit != hand.cards[0].suit) and (hand.cards[0].suit == hand.cards[1].suit) and (hand.cards[2].val > 7) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(1) == 0) and (hand.cards[4].val < 4):
		hand_confidences[4] += -20
	
	# Mutation Resistance: 100.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 3):
		hand_confidences[4] += -60
	
	# Mutation Resistance: 100.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 3):
		hand_confidences[4] += -30
	
	# Mutation Resistance: 100.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 5):
		hand_confidences[4] += 50
	
	# Mutation Resistance: 691.662605983%
	if (hand.cards[2].val != hand.cards[1].val):
		hand_confidences[4] += -65
	
	# Mutation Resistance: 79.9999743479%
	if (hand.cards[3].val == hand.cards[1].val) and (hand.cards[4].val > 8):
		hand_confidences[4] += -85
	
	# Mutation Resistance: 147.606985838%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 5) and (hand.cards[3].val < 7):
		hand_confidences[4] += -5
	
	# Mutation Resistance: 67.7419354839%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4) and (hand.cards[0].suit != hand.cards[1].suit):
		hand_confidences[4] += 90
	
	# Mutation Resistance: 67.7419354839%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4) and (hand.cards[0].suit != hand.cards[1].suit):
		hand_confidences[4] += 20
	
	# Mutation Resistance: 147.606985838%
	if (hand.cards[3].val < 7) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 5):
		hand_confidences[4] += -75
	
	# Mutation Resistance: 0.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0) and (hand.cards[4].suit != hand.cards[3].suit) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 6]) == 2) and (hand.cards[4].val == hand.cards[1].val) and (hand.cards[1].val != hand.cards[2].val) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 9) and (hand.cards[0].val == hand.cards[1].val) and (hand.cards[3].suit != hand.cards[4].suit) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 1):
		hand_confidences[4] += 80
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val > 10) and (hand.cards[0].val == hand.cards[1].val) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 1) and (hand.cards[3].val == hand.cards[0].val) and (hand.cards[4].suit != hand.cards[3].suit) and (hand.cards[1].val != hand.cards[3].val) and (hand.cards[4].val != hand.cards[3].val):
		hand_confidences[4] += -90
	
	# Mutation Resistance: 100.0%
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 0) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(4) == 1):
		hand_confidences[5] += -95
	
	# Mutation Resistance: 558.206966691%
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -25
	
	# Mutation Resistance: 558.206966691%
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -55
	
	# Mutation Resistance: 558.206966691%
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -10
	
	# Mutation Resistance: 100.0%
	if (hand.cards[4].suit == hand.cards[3].suit):
		hand_confidences[5] += 15
	
	# Mutation Resistance: 155.6297773%
	if (hand.cards[0].val == hand.cards[3].val) and (hand.cards[3].val < 12):
		hand_confidences[5] += -60
	
	# Mutation Resistance: 127.697547769%
	if (hand.cards[4].val == hand.cards[1].val):
		hand_confidences[5] += -85
	
	# Mutation Resistance: 558.206966691%
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -80
	
	# Mutation Resistance: 137.4923716%
	if (hand.cards[0].val == hand.cards[1].val) and (hand.cards[2].val != hand.cards[4].val):
		hand_confidences[5] += -100
	
	# Mutation Resistance: 100.0%
	if (hand.cards[4].suit == hand.cards[3].suit):
		hand_confidences[5] += 75
	
	# Mutation Resistance: 100.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(4) == 1) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 0):
		hand_confidences[5] += -30
	
	# Mutation Resistance: 559.353910415%
	if (hand.cards[2].suit != hand.cards[4].suit):
		hand_confidences[5] += -35
	
	# Mutation Resistance: 187.096774194%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4) and (hand.cards[1].val != hand.cards[0].val):
		hand_confidences[5] += -90
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val > 4) and (hand.cards[0].suit == hand.cards[1].suit) and (hand.cards[2].val != hand.cards[4].val) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 2) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 3]) == 3) and (hand.cards[1].val > 1) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 6]) == 2) and (hand.cards[0].val == hand.cards[4].val):
		hand_confidences[5] += -25
	
	# Mutation Resistance: 475.852879877%
	if (hand.cards[4].val != hand.cards[0].val) and (hand.cards[0].suit != hand.cards[2].suit):
		hand_confidences[5] += -65
	
	# Mutation Resistance: 558.206966691%
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -60
	
	# Mutation Resistance: 569.630571253%
	if (hand.cards[3].suit != hand.cards[0].suit):
		hand_confidences[5] += -40
	
	# Mutation Resistance: 42.5925925926%
	if (hand.cards[2].val != hand.cards[4].val) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 2):
		hand_confidences[5] += 80
	
	# Mutation Resistance: 559.353910415%
	if (hand.cards[2].suit != hand.cards[4].suit):
		hand_confidences[5] += -75
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val != hand.cards[0].val) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 2]) == 4) and (hand.cards[1].val < 3):
		hand_confidences[5] += 30
	
	# Mutation Resistance: 600.906646657%
	if (hand.cards[4].val > 3) and (hand.cards[4].val != hand.cards[0].val):
		hand_confidences[5] += -10
	
	# Mutation Resistance: 14.3005731576%
	if ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 2) and (hand.cards[0].val != hand.cards[3].val):
		hand_confidences[5] += -10
	
	# Mutation Resistance: 174.099394469%
	if (hand.cards[2].val == hand.cards[3].val):
		hand_confidences[5] += -75
	
	# Mutation Resistance: 0.0%
	if ((hand.cards[4].val - hand.cards[0].val) == -8) and (hand.cards[3].suit == hand.cards[0].suit) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 1) and ((hand.cards[3].val - hand.cards[4].val) == 5) and (hand.cards[1].val > 3) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 12]) == 1) and (hand.cards[3].suit == hand.cards[2].suit):
		hand_confidences[5] += -75
	
	# Mutation Resistance: 109.138635299%
	if (hand.cards[2].val != hand.cards[0].val) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 12) and (hand.cards[1].suit == hand.cards[4].suit):
		hand_confidences[5] += -5
	
	# Mutation Resistance: 329.46712745%
	if (hand.cards[1].val > 9):
		hand_confidences[5] += -50
	
	# Mutation Resistance: 558.206966691%
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -40
	
	# Mutation Resistance: 559.353910415%
	if (hand.cards[2].suit != hand.cards[4].suit):
		hand_confidences[5] += -65
	
	# Mutation Resistance: 53.2400230835%
	if (hand.cards[3].val < 4) and (hand.cards[3].suit != hand.cards[1].suit) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0) and (hand.cards[4].val < 8):
		hand_confidences[5] += -25
	
	# Mutation Resistance: 558.206966691%
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -15
	
	# Mutation Resistance: 103.819713867%
	if (hand.cards[3].suit != hand.cards[1].suit) and (hand.cards[3].val > 1) and (hand.cards[0].suit == hand.cards[4].suit):
		hand_confidences[5] += -65
	
	# Mutation Resistance: 558.206966691%
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -65
	
	# Mutation Resistance: 0.0%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 4]) == 2) and (hand.cards[0].val == hand.cards[4].val) and ((hand.cards[3].val - hand.cards[1].val) == -8) and (hand.cards[4].suit != hand.cards[1].suit) and ((hand.cards[4].val - hand.cards[1].val) == 8):
		hand_confidences[5] += -30
	
	# Mutation Resistance: 600.906646657%
	if (hand.cards[4].val > 3) and (hand.cards[4].val != hand.cards[0].val):
		hand_confidences[5] += -10
	
	# Mutation Resistance: 127.697547769%
	if (hand.cards[4].val == hand.cards[1].val):
		hand_confidences[5] += -90
	
	# Mutation Resistance: 187.096774194%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4) and (hand.cards[1].val != hand.cards[0].val):
		hand_confidences[5] += -20
	
	# Mutation Resistance: 100.0%
	if (hand.cards[4].suit == hand.cards[0].suit):
		hand_confidences[5] += 25
	
	# Mutation Resistance: 187.096774194%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4) and (hand.cards[1].val != hand.cards[0].val):
		hand_confidences[5] += -65
	
	# Mutation Resistance: 329.46712745%
	if (hand.cards[1].val > 9):
		hand_confidences[5] += -25
	
	# Mutation Resistance: 0.0%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 8]) == 1) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 12]) == 1) and (hand.cards[1].val != hand.cards[3].val) and (hand.cards[4].val != hand.cards[3].val) and (hand.cards[4].val != hand.cards[0].val):
		hand_confidences[5] += 45
	
	# Mutation Resistance: 558.206966691%
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -5
	
	# Mutation Resistance: 558.206966691%
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -15
	
	# Mutation Resistance: 558.206966691%
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -40
	
	# Mutation Resistance: 137.4923716%
	if (hand.cards[0].val == hand.cards[1].val) and (hand.cards[2].val != hand.cards[4].val):
		hand_confidences[5] += -40
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].val > 10) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 3]) == 4) and (hand.cards[0].suit == hand.cards[2].suit) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 3) and (hand.cards[4].val != hand.cards[0].val) and (hand.cards[3].val != hand.cards[0].val) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0) and ((hand.cards[3].val - hand.cards[2].val) == 10) and ((hand.cards[4].val - hand.cards[2].val) == -5) and (hand.cards[4].val < 9) and ((hand.cards[4].val - hand.cards[1].val) == 2) and (hand.cards[4].suit == hand.cards[3].suit):
		hand_confidences[5] += -5
	
	# Mutation Resistance: 558.206966691%
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -15
	
	# Mutation Resistance: 558.206966691%
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -60
	
	# Mutation Resistance: 558.206966691%
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -55
	
	# Mutation Resistance: 558.206966691%
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -20
	
	# Mutation Resistance: 103.819713867%
	if (hand.cards[3].val > 1) and (hand.cards[3].suit != hand.cards[1].suit) and (hand.cards[0].suit == hand.cards[4].suit):
		hand_confidences[5] += -90
	
	# Mutation Resistance: 559.353910415%
	if (hand.cards[2].suit != hand.cards[4].suit):
		hand_confidences[5] += -35
	
	# Mutation Resistance: 100.0%
	if (hand.cards[4].suit == hand.cards[3].suit):
		hand_confidences[5] += 90
	
	# Mutation Resistance: 0.0%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 2]) == 4) and ((hand.cards[0].val - hand.cards[3].val) == -7) and (hand.cards[2].suit != hand.cards[0].suit) and (hand.cards[3].suit == hand.cards[2].suit) and (hand.cards[4].suit == hand.cards[1].suit) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 0):
		hand_confidences[5] += 30
	
	# Mutation Resistance: 0.0%
	if ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 10) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 3) and (hand.cards[3].val != hand.cards[2].val) and (hand.cards[4].val == hand.cards[1].val) and (hand.cards[3].suit == hand.cards[0].suit) and (hand.cards[0].suit != hand.cards[4].suit):
		hand_confidences[5] += 35
	
	# Mutation Resistance: 100.0%
	if (hand.cards[4].suit == hand.cards[3].suit):
		hand_confidences[5] += 15
	
	# Mutation Resistance: 103.819713867%
	if (hand.cards[3].suit != hand.cards[1].suit) and (hand.cards[3].val > 1) and (hand.cards[0].suit == hand.cards[4].suit):
		hand_confidences[5] += -75
	
	# Mutation Resistance: 0.575775925608%
	if (hand.cards[4].val == hand.cards[2].val) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 6]) == 1) and (hand.cards[0].val != hand.cards[2].val) and (hand.cards[1].val < 2):
		hand_confidences[5] += -35
	
	# Mutation Resistance: 109.138635299%
	if (hand.cards[1].suit == hand.cards[4].suit) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 12) and (hand.cards[2].val != hand.cards[0].val):
		hand_confidences[5] += -55
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val == hand.cards[0].val) and ((hand.cards[2].val - hand.cards[1].val) == 12) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 2) and (hand.cards[4].val == hand.cards[3].val) and ((hand.cards[2].val - hand.cards[4].val) == 10) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0) and (hand.cards[1].val != hand.cards[2].val) and (hand.cards[3].val != hand.cards[0].val) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 1) and (hand.cards[3].val > 9) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(4) == 1) and (hand.cards[1].val != hand.cards[4].val) and (hand.cards[2].suit == hand.cards[0].suit):
		hand_confidences[5] += -20
	
	# Mutation Resistance: 558.206966691%
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -55
	
	# Mutation Resistance: 137.4923716%
	if (hand.cards[0].val == hand.cards[1].val) and (hand.cards[2].val != hand.cards[4].val):
		hand_confidences[5] += -40
	
	# Mutation Resistance: 137.4923716%
	if (hand.cards[2].val != hand.cards[4].val) and (hand.cards[0].val == hand.cards[1].val):
		hand_confidences[5] += -75
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val == hand.cards[2].val) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 1):
		hand_confidences[5] += 35
	
	# Mutation Resistance: 558.206966691%
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -95
	
	# Mutation Resistance: 559.353910415%
	if (hand.cards[2].suit != hand.cards[4].suit):
		hand_confidences[5] += -55
	
	# Mutation Resistance: 127.697547769%
	if (hand.cards[4].val == hand.cards[1].val):
		hand_confidences[5] += -75
	
	# Mutation Resistance: 558.206966691%
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -80
	
	# Mutation Resistance: 137.4923716%
	if (hand.cards[2].val != hand.cards[4].val) and (hand.cards[0].val == hand.cards[1].val):
		hand_confidences[5] += -5
	
	# Mutation Resistance: 558.206966691%
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -45
	
	# Mutation Resistance: 434.776594029%
	if (hand.cards[1].suit == hand.cards[4].suit):
		hand_confidences[6] += -15
	
	# Mutation Resistance: 388.232310643%
	if (hand.cards[3].val > 8):
		hand_confidences[6] += -40
	
	# Mutation Resistance: 100.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 2):
		hand_confidences[6] += -100
	
	# Mutation Resistance: 100.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(3) == 1):
		hand_confidences[6] += 70
	
	# Mutation Resistance: 148.307280953%
	if (hand.cards[3].suit != hand.cards[4].suit) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 1):
		hand_confidences[6] += -35
	
	# Mutation Resistance: 100.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 2):
		hand_confidences[6] += -55
	
	# Mutation Resistance: 110.997986265%
	if (hand.cards[1].val != hand.cards[0].val) and (hand.cards[2].val < 3):
		hand_confidences[6] += -5
	
	# Mutation Resistance: 100.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(3) == 1):
		hand_confidences[6] += 85
	
	# Mutation Resistance: 100.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 2):
		hand_confidences[6] += -50
	
	# Mutation Resistance: 100.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(3) == 1):
		hand_confidences[6] += 60
	
	# Mutation Resistance: 0.0%
	if ((hand.cards[0].val - hand.cards[2].val) == 7) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 2) and (hand.cards[1].val > 9) and (hand.cards[4].val == hand.cards[3].val):
		hand_confidences[6] += -5
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].suit == hand.cards[0].suit) and (hand.cards[4].val != hand.cards[3].val) and (hand.cards[2].val > 2) and (hand.cards[4].val == hand.cards[1].val) and (hand.cards[2].suit != hand.cards[3].suit) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 3]) == 3) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1) and (hand.cards[0].suit == hand.cards[1].suit):
		hand_confidences[6] += 50
	
	# Mutation Resistance: 9.94152046784%
	if (hand.cards[2].suit != hand.cards[0].suit) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(3) == 1) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 1) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(3) == 1) and (hand.cards[2].suit != hand.cards[4].suit):
		hand_confidences[6] += -100
	
	# Mutation Resistance: 0.0%
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 1) and (hand.cards[2].suit != hand.cards[3].suit) and (hand.cards[3].suit == hand.cards[2].suit):
		hand_confidences[6] += 50
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].val == hand.cards[2].val) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 6]) == 1) and (hand.cards[1].val < 5) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 0) and (hand.cards[3].val < 8) and ((hand.cards[1].val - hand.cards[2].val) == 8):
		hand_confidences[6] += 80
	
	# Mutation Resistance: 0.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(4) == 1) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 12) and (hand.cards[2].suit != hand.cards[4].suit) and (hand.cards[0].val == hand.cards[2].val) and ((hand.cards[1].val - hand.cards[0].val) == 9):
		hand_confidences[6] += -35
	
	# Mutation Resistance: 100.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0):
		hand_confidences[7] += 50
	
	# Mutation Resistance: 419.141539791%
	if (hand.cards[2].suit == hand.cards[0].suit):
		hand_confidences[7] += -70
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].suit != hand.cards[3].suit) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 2) and (hand.cards[3].suit != hand.cards[2].suit) and ((hand.cards[4].val - hand.cards[3].val) == -3):
		hand_confidences[7] += 85
	
	# Mutation Resistance: 100.0%
	if (hand.cards[1].val == hand.cards[2].val) and (hand.cards[1].suit != hand.cards[3].suit) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1):
		hand_confidences[7] += 60
	
	# Mutation Resistance: 300.0%
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 1):
		hand_confidences[7] += -75
	
	# Mutation Resistance: 100.0%
	if (hand.cards[1].val == hand.cards[2].val) and (hand.cards[1].suit != hand.cards[3].suit) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1):
		hand_confidences[7] += 10
	
	# Mutation Resistance: 2.65661915519%
	if (hand.cards[0].val != hand.cards[3].val) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 5]) == 1) and (hand.cards[4].val != hand.cards[3].val) and ((hand.cards[4].val - hand.cards[0].val) == 10):
		hand_confidences[7] += -90
	
	# Mutation Resistance: 200.0%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 2):
		hand_confidences[7] += -55
	
	# Mutation Resistance: 16.6666666667%
	if ((hand.cards[0].val - hand.cards[4].val) == -10) and (hand.cards[3].val == hand.cards[1].val) and (hand.cards[4].val > 9):
		hand_confidences[7] += 30
	
	# Mutation Resistance: 9.79612928615%
	if (hand.cards[3].val == hand.cards[1].val) and (hand.cards[3].val != hand.cards[0].val) and (hand.cards[4].suit == hand.cards[2].suit):
		hand_confidences[7] += -55
	
	# Mutation Resistance: 1.15960475181%
	if (hand.cards[1].suit == hand.cards[3].suit) and (hand.cards[3].val != hand.cards[0].val) and ((hand.cards[2].val - hand.cards[4].val) == 2) and (hand.cards[1].val != hand.cards[4].val) and ((hand.cards[2].val - hand.cards[0].val) == 4) and (hand.cards[4].suit != hand.cards[0].suit) and (hand.cards[1].val != hand.cards[0].val):
		hand_confidences[8] += -90
	
	# Mutation Resistance: 110.082254686%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 2):
		hand_confidences[8] += -50
	
	# Mutation Resistance: 100.0%
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(1) == 0) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 1) and (hand.cards[2].val != hand.cards[0].val):
		hand_confidences[8] += 55
	
	# Mutation Resistance: 83.5287456882%
	if ((hand.cards[2].val - hand.cards[0].val) == -1) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0):
		hand_confidences[8] += -10
	
	# Mutation Resistance: 0.0%
	if ((hand.cards[2].val - hand.cards[0].val) == 4) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 1) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 2) and ((hand.cards[1].val - hand.cards[0].val) == -7) and (hand.cards[4].suit != hand.cards[2].suit):
		hand_confidences[8] += -30
	
	# Mutation Resistance: 83.5287456882%
	if ((hand.cards[2].val - hand.cards[0].val) == -1) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0):
		hand_confidences[8] += -65
	
	# Mutation Resistance: 100.0%
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(1) == 0) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 1) and (hand.cards[2].val != hand.cards[0].val):
		hand_confidences[8] += 25
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val < 7) and (hand.cards[3].val < 11) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 3]) == 3) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 5) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 3]) == 3) and (hand.cards[1].suit != hand.cards[0].suit) and (hand.cards[4].val != hand.cards[3].val) and ((hand.cards[1].val - hand.cards[3].val) == -3) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1) and (hand.cards[2].val == hand.cards[0].val):
		hand_confidences[8] += -40
	
	# Mutation Resistance: 1.02169422211%
	if (hand.cards[4].val < 2) and (hand.cards[4].suit != hand.cards[1].suit) and ((hand.cards[1].val - hand.cards[2].val) == 7):
		hand_confidences[8] += -50
	
	# Mutation Resistance: 159.696127132%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 3]) == 1):
		hand_confidences[8] += -55
	
	# Mutation Resistance: 69.7120481393%
	if ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 9):
		hand_confidences[8] += -25
	
	# Mutation Resistance: 461.973073834%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0) and (hand.cards[4].val < 10):
		hand_confidences[8] += -25
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val < 7) and (hand.cards[2].val != hand.cards[0].val) and (hand.cards[1].val != hand.cards[4].val) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0) and ((hand.cards[1].val - hand.cards[2].val) == -8) and (hand.cards[0].val != hand.cards[3].val) and (hand.cards[1].val == hand.cards[4].val):
		hand_confidences[8] += 90
	
	# Mutation Resistance: 100.0%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4):
		hand_confidences[8] += 85
	
	# Mutation Resistance: 560.625166037%
	if (hand.cards[3].suit != hand.cards[2].suit):
		hand_confidences[9] += -65
	
	# Mutation Resistance: 197.802530981%
	if (hand.cards[0].val > 8) and (hand.cards[4].suit != hand.cards[3].suit):
		hand_confidences[9] += -20
	
	# Mutation Resistance: 80.6613992761%
	if ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 6):
		hand_confidences[9] += -60
	
	# Mutation Resistance: 80.6613992761%
	if ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 6):
		hand_confidences[9] += -55
	
	# Mutation Resistance: 268.779377998%
	if (hand.cards[1].val < 11) and (hand.cards[2].val != hand.cards[4].val) and (hand.cards[3].val < 6):
		hand_confidences[9] += -85
	
	# Mutation Resistance: 100.0%
	if (hand.cards[4].suit == hand.cards[1].suit) and (hand.cards[0].suit == hand.cards[2].suit) and (hand.cards[0].val != hand.cards[3].val) and (hand.cards[1].val > 3):
		hand_confidences[9] += 95
	
	# Mutation Resistance: 22.8026533997%
	if (hand.cards[0].val < 8) and (hand.cards[1].val == hand.cards[0].val) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0) and (hand.cards[4].val != hand.cards[0].val) and (hand.cards[0].suit != hand.cards[3].suit) and (hand.cards[4].val > 10) and (hand.cards[3].val == hand.cards[2].val):
		hand_confidences[9] += -30
	
	# Mutation Resistance: 197.802530981%
	if (hand.cards[4].suit != hand.cards[3].suit) and (hand.cards[0].val > 8):
		hand_confidences[9] += -40
	
	# Mutation Resistance: 197.802530981%
	if (hand.cards[4].suit != hand.cards[3].suit) and (hand.cards[0].val > 8):
		hand_confidences[9] += -50
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val != hand.cards[2].val) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 6) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(1) == 3) and (hand.cards[1].val == hand.cards[2].val) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 4) and (hand.cards[3].suit == hand.cards[1].suit) and (hand.cards[4].suit != hand.cards[2].suit) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 6) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 10):
		hand_confidences[9] += -25
	
	# Mutation Resistance: 191.272142479%
	if (hand.cards[0].val != hand.cards[3].val) and (hand.cards[3].val < 9) and (hand.cards[4].suit == hand.cards[1].suit):
		hand_confidences[9] += -85
	
	# Mutation Resistance: 80.6613992761%
	if ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 6):
		hand_confidences[9] += -60
	
	# Mutation Resistance: 100.0%
	if (hand.cards[2].val != hand.cards[1].val) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 3):
		hand_confidences[9] += 55
	
	# Mutation Resistance: 0.0%
	if ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 5) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 2]) == 2) and (hand.cards[2].suit == hand.cards[0].suit) and (hand.cards[3].val != hand.cards[1].val):
		hand_confidences[9] += 35
	
	# Mutation Resistance: 268.779377998%
	if (hand.cards[2].val != hand.cards[4].val) and (hand.cards[1].val < 11) and (hand.cards[3].val < 6):
		hand_confidences[9] += -80
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val < 5) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(3) == 1) and ((hand.cards[0].val - hand.cards[4].val) == 12):
		hand_confidences[9] += 45
	
	# Mutation Resistance: 268.779377998%
	if (hand.cards[2].val != hand.cards[4].val) and (hand.cards[3].val < 6) and (hand.cards[1].val < 11):
		hand_confidences[9] += -80
	
	# Mutation Resistance: 197.802530981%
	if (hand.cards[4].suit != hand.cards[3].suit) and (hand.cards[0].val > 8):
		hand_confidences[9] += -50
	
	# Mutation Resistance: 197.802530981%
	if (hand.cards[0].val > 8) and (hand.cards[4].suit != hand.cards[3].suit):
		hand_confidences[9] += -15
	
	# Mutation Resistance: 211.138192494%
	if (hand.cards[3].suit != hand.cards[2].suit) and (hand.cards[3].val < 11) and (hand.cards[3].val < 6):
		hand_confidences[9] += -55
	
	# Mutation Resistance: 197.802530981%
	if (hand.cards[0].val > 8) and (hand.cards[4].suit != hand.cards[3].suit):
		hand_confidences[9] += -50
	
	# Mutation Resistance: 197.802530981%
	if (hand.cards[0].val > 8) and (hand.cards[4].suit != hand.cards[3].suit):
		hand_confidences[9] += -95
	
	if max(hand_confidences) >= 100:
		hand.assigned_class = hand_confidences.index(max(hand_confidences))
	else:
		hand.assigned_class = 0