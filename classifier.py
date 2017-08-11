#Class 0 fitness: 949.12
#Class 1 fitness: 1327.87
#Class 2 fitness: 903.60
#Class 3 fitness: 1194.00
#Class 4 fitness: 1094.26
#Class 5 fitness: 1053.92
#Class 6 fitness: 967.67
#Class 7 fitness: 1371.09
#Class 8 fitness: 1199.80
#Class 9 fitness: 1178.79
# Fitness: 391.106742407
def classify(hand):
	hand_confidences = [0 for i in range(10)]
	
	# Mutation Resistance: 417.059182353%
	if (hand.cards[4].suit == hand.cards[0].suit):
		hand_confidences[0] += -90
	
	# Mutation Resistance: 53.9422076363%
	if (hand.cards[1].val < 8):
		hand_confidences[0] += 70
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val == hand.cards[0].val) and (hand.cards[4].val > 2) and (hand.cards[2].val != hand.cards[3].val) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 11]) == 1) and (hand.cards[4].suit == hand.cards[3].suit) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 10) and (hand.cards[1].suit != hand.cards[0].suit) and ((hand.cards[4].val - hand.cards[3].val) == -11) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 1) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0):
		hand_confidences[0] += -20
	
	# Mutation Resistance: 0.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 6]) == 2) and ((hand.cards[4].val - hand.cards[3].val) == -8):
		hand_confidences[0] += -95
	
	# Mutation Resistance: 40.1385401053%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 6]) == 1) and (hand.cards[4].suit != hand.cards[1].suit) and (hand.cards[0].val < 12):
		hand_confidences[0] += -30
	
	# Mutation Resistance: 70.8299874596%
	if (hand.cards[3].val < 6) and (hand.cards[0].val < 3) and (hand.cards[1].suit == hand.cards[2].suit):
		hand_confidences[0] += -45
	
	# Mutation Resistance: 1.26470823661%
	if (hand.cards[3].suit != hand.cards[0].suit) and (hand.cards[0].suit == hand.cards[4].suit) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 9) and (hand.cards[0].suit == hand.cards[4].suit) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0) and (hand.cards[2].val < 10) and (hand.cards[2].val != hand.cards[4].val):
		hand_confidences[0] += 75
	
	# Mutation Resistance: 0.0%
	if ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 8) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(4) == 1) and (hand.cards[2].val < 12) and (hand.cards[3].val != hand.cards[2].val):
		hand_confidences[0] += 10
	
	# Mutation Resistance: 0.500047174262%
	if (hand.cards[3].suit != hand.cards[4].suit) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 3]) == 3):
		hand_confidences[0] += -60
	
	# Mutation Resistance: 35.8920995758%
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 1) and (hand.cards[4].val != hand.cards[3].val) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0) and (hand.cards[4].val != hand.cards[2].val):
		hand_confidences[0] += 65
	
	# Mutation Resistance: 711.837741119%
	if (hand.cards[4].val != hand.cards[2].val) and (hand.cards[4].val != hand.cards[1].val):
		hand_confidences[1] += -25
	
	# Mutation Resistance: 700.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0):
		hand_confidences[1] += -95
	
	# Mutation Resistance: 0.0%
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 0) and (hand.cards[2].val < 12) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 5]) == 2):
		hand_confidences[1] += -90
	
	# Mutation Resistance: 800.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0):
		hand_confidences[1] += -5
	
	# Mutation Resistance: 800.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0):
		hand_confidences[1] += -5
	
	# Mutation Resistance: 89.7160109444%
	if (hand.cards[4].val != hand.cards[0].val) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 1):
		hand_confidences[1] += 100
	
	# Mutation Resistance: 800.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0):
		hand_confidences[1] += -5
	
	# Mutation Resistance: 0.0%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 3]) == 3) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 8]) == 1) and (hand.cards[4].val != hand.cards[1].val):
		hand_confidences[1] += -45
	
	# Mutation Resistance: 119.131653006%
	if (hand.cards[3].val > 5) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 9]) == 1):
		hand_confidences[1] += -85
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].suit == hand.cards[2].suit) and (hand.cards[1].suit != hand.cards[4].suit) and (hand.cards[3].suit == hand.cards[1].suit) and (hand.cards[1].suit == hand.cards[4].suit):
		hand_confidences[1] += -60
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val < 3) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0) and (hand.cards[4].suit != hand.cards[2].suit) and (hand.cards[3].val > 1) and (hand.cards[2].val != hand.cards[1].val) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 1) and (hand.cards[1].val == hand.cards[3].val) and (hand.cards[3].val != hand.cards[1].val):
		hand_confidences[1] += -20
	
	# Mutation Resistance: 89.7160109444%
	if (hand.cards[4].val != hand.cards[0].val) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 1):
		hand_confidences[1] += 85
	
	# Mutation Resistance: 92.0652891782%
	if (hand.cards[0].val > 1):
		hand_confidences[1] += 90
	
	# Mutation Resistance: 187.096774194%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4):
		hand_confidences[1] += -60
	
	# Mutation Resistance: 22.9172563449%
	if (hand.cards[0].val != hand.cards[3].val) and (hand.cards[0].suit == hand.cards[3].suit):
		hand_confidences[1] += 25
	
	# Mutation Resistance: 81.5057243205%
	if (hand.cards[1].suit == hand.cards[2].suit) and (hand.cards[4].suit != hand.cards[2].suit) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 0):
		hand_confidences[1] += -75
	
	# Mutation Resistance: 14.5296726106%
	if (hand.cards[0].val != hand.cards[3].val) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 9):
		hand_confidences[1] += 65
	
	# Mutation Resistance: 711.837741119%
	if (hand.cards[4].val != hand.cards[2].val) and (hand.cards[4].val != hand.cards[1].val):
		hand_confidences[1] += -15
	
	# Mutation Resistance: 11.200432086%
	if (hand.cards[1].val < 7) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0) and ((hand.cards[1].val - hand.cards[4].val) == -9):
		hand_confidences[1] += -55
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].suit == hand.cards[2].suit) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 1) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 10) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 6) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 1) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 5) and (hand.cards[4].val > 7) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0) and (hand.cards[3].val == hand.cards[1].val) and ((hand.cards[1].val - hand.cards[0].val) == 2) and (hand.cards[3].suit != hand.cards[0].suit) and (hand.cards[0].suit == hand.cards[3].suit) and ((hand.cards[4].val - hand.cards[1].val) == 9) and (hand.cards[4].suit == hand.cards[2].suit) and (hand.cards[3].suit == hand.cards[4].suit):
		hand_confidences[1] += -40
	
	# Mutation Resistance: 80.9286898839%
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[2] += 45
	
	# Mutation Resistance: 1.32669983416%
	if (hand.cards[1].val > 1) and (hand.cards[1].suit == hand.cards[0].suit) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 9) and (hand.cards[4].val < 6) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0):
		hand_confidences[2] += 60
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val != hand.cards[4].val) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 3) and (hand.cards[4].suit == hand.cards[2].suit) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 1) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(1) == 0):
		hand_confidences[2] += 5
	
	# Mutation Resistance: 0.0%
	if ((hand.cards[4].val - hand.cards[2].val) == 8) and (hand.cards[4].val < 5) and (hand.cards[1].suit == hand.cards[2].suit) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(4) == 1) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 5]) == 1) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 3]) == 4) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1) and (hand.cards[1].val != hand.cards[0].val) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 7]) == 1):
		hand_confidences[2] += 10
	
	# Mutation Resistance: 1.43819519934%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 5]) == 2) and (hand.cards[3].val < 12) and (hand.cards[4].suit != hand.cards[1].suit):
		hand_confidences[2] += -70
	
	# Mutation Resistance: 0.0%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 2]) == 4) and (hand.cards[2].val < 3) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0) and ((hand.cards[2].val - hand.cards[1].val) == 5) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(1) == 4) and (hand.cards[0].suit != hand.cards[4].suit) and (hand.cards[1].suit != hand.cards[0].suit) and ((hand.cards[0].val - hand.cards[2].val) == 6):
		hand_confidences[2] += 55
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val < 3) and ((hand.cards[3].val - hand.cards[4].val) == 12) and (hand.cards[4].suit == hand.cards[2].suit) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 4]) == 2) and (hand.cards[1].val == hand.cards[2].val) and (hand.cards[2].val != hand.cards[3].val) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 3]) == 4):
		hand_confidences[3] += -20
	
	# Mutation Resistance: 406.966798417%
	if (hand.cards[1].suit == hand.cards[3].suit):
		hand_confidences[3] += -15
	
	# Mutation Resistance: 124.495228439%
	if (hand.cards[4].val > 8) and (hand.cards[4].val != hand.cards[1].val) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0) and (hand.cards[0].suit == hand.cards[3].suit):
		hand_confidences[3] += -85
	
	# Mutation Resistance: 0.040022412551%
	if (hand.cards[2].val != hand.cards[3].val) and (hand.cards[3].val != hand.cards[0].val) and (hand.cards[4].val < 13) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 3]) == 4) and (hand.cards[2].val != hand.cards[3].val) and (hand.cards[1].val < 6) and (hand.cards[0].val != hand.cards[4].val) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 12):
		hand_confidences[3] += -60
	
	# Mutation Resistance: 1.36452241715%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 10]) == 1) and (hand.cards[0].val > 8):
		hand_confidences[3] += 65
	
	# Mutation Resistance: 100.0%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 2):
		hand_confidences[3] += 55
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val != hand.cards[3].val) and (hand.cards[3].val < 7) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 0) and (hand.cards[1].val > 5) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0) and (hand.cards[2].suit == hand.cards[1].suit) and (hand.cards[1].val != hand.cards[2].val) and (hand.cards[3].val > 4):
		hand_confidences[3] += -65
	
	# Mutation Resistance: 9.19493357408%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 2]) == 1) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 5):
		hand_confidences[3] += -65
	
	# Mutation Resistance: 0.0%
	if ((hand.cards[2].val - hand.cards[0].val) == 12) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 6]) == 1) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 6]) == 2) and ((hand.cards[3].val - hand.cards[4].val) == 5) and (hand.cards[1].suit == hand.cards[2].suit) and (hand.cards[0].val > 10):
		hand_confidences[3] += 80
	
	# Mutation Resistance: 84.2105263158%
	if (hand.cards[2].suit != hand.cards[0].suit):
		hand_confidences[3] += 70
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val < 5) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 10) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 10) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 7) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 2):
		hand_confidences[4] += 20
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val != hand.cards[2].val) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 12) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 5) and (hand.cards[0].val != hand.cards[4].val) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0):
		hand_confidences[4] += 30
	
	# Mutation Resistance: 35.2824013304%
	if ((hand.cards[3].val - hand.cards[2].val) == 5):
		hand_confidences[4] += -60
	
	# Mutation Resistance: 100.0%
	if (hand.cards[2].val != hand.cards[4].val):
		hand_confidences[4] += 40
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].suit == hand.cards[4].suit) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 9) and ((hand.cards[3].val - hand.cards[1].val) == -9) and (hand.cards[1].val < 5) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 8):
		hand_confidences[4] += -20
	
	# Mutation Resistance: 11.0769166587%
	if (hand.cards[4].suit != hand.cards[2].suit) and ((hand.cards[1].val - hand.cards[3].val) == -8):
		hand_confidences[4] += -20
	
	# Mutation Resistance: 36.147338315%
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 1) and (hand.cards[2].suit == hand.cards[3].suit):
		hand_confidences[4] += -15
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].suit != hand.cards[1].suit) and (hand.cards[4].val != hand.cards[3].val) and (hand.cards[2].suit != hand.cards[1].suit) and (hand.cards[2].val == hand.cards[3].val) and (hand.cards[0].val == hand.cards[2].val) and (hand.cards[4].suit != hand.cards[0].suit) and (hand.cards[4].suit == hand.cards[0].suit):
		hand_confidences[4] += -20
	
	# Mutation Resistance: 0.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 0) and (hand.cards[2].suit != hand.cards[4].suit) and (hand.cards[4].val == hand.cards[3].val) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 9]) == 1):
		hand_confidences[4] += 95
	
	# Mutation Resistance: 391.796182055%
	if (hand.cards[2].suit == hand.cards[1].suit):
		hand_confidences[4] += -70
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val != hand.cards[1].val) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 3) and (hand.cards[4].val < 3) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4) and (hand.cards[0].val > 1) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 2) and (hand.cards[3].val == hand.cards[4].val) and (hand.cards[1].val < 9) and (hand.cards[0].val == hand.cards[4].val) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0):
		hand_confidences[4] += 70
	
	# Mutation Resistance: 0.0%
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(1) == 0) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0) and ((hand.cards[4].val - hand.cards[3].val) == 6) and ((hand.cards[2].val - hand.cards[3].val) == 4) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0) and (hand.cards[1].val == hand.cards[3].val):
		hand_confidences[4] += 50
	
	# Mutation Resistance: 0.0%
	if ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 4) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(4) == 1) and ((hand.cards[3].val - hand.cards[1].val) == 3) and (hand.cards[3].suit == hand.cards[1].suit) and (hand.cards[0].suit == hand.cards[3].suit) and ((hand.cards[4].val - hand.cards[0].val) == -3) and (hand.cards[0].val < 7) and (hand.cards[3].val < 6):
		hand_confidences[4] += -10
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].suit == hand.cards[1].suit) and ((hand.cards[0].val - hand.cards[1].val) == 5) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(2) == 2) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0) and (hand.cards[4].val == hand.cards[3].val) and (hand.cards[0].val != hand.cards[2].val) and (hand.cards[2].suit == hand.cards[0].suit) and (hand.cards[0].suit == hand.cards[3].suit) and (hand.cards[2].val > 7) and (hand.cards[4].val == hand.cards[2].val):
		hand_confidences[4] += 95
	
	# Mutation Resistance: 0.0%
	if ((hand.cards[0].val - hand.cards[1].val) == 7) and (hand.cards[1].val == hand.cards[3].val) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 2) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 4) and (hand.cards[0].val < 6) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(4) == 1) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0):
		hand_confidences[4] += 70
	
	# Mutation Resistance: 100.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 5):
		hand_confidences[4] += 25
	
	# Mutation Resistance: 0.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(3) == 1) and (hand.cards[4].val == hand.cards[3].val) and ((hand.cards[3].val - hand.cards[1].val) == -3) and (hand.cards[4].suit == hand.cards[2].suit) and (hand.cards[4].val > 11) and (hand.cards[4].val != hand.cards[3].val) and ((hand.cards[1].val - hand.cards[2].val) == -10):
		hand_confidences[4] += -25
	
	# Mutation Resistance: 100.0%
	if (hand.cards[0].val != hand.cards[1].val):
		hand_confidences[4] += 65
	
	# Mutation Resistance: 100.498165062%
	if (hand.cards[2].val != hand.cards[0].val) and (hand.cards[0].val != hand.cards[2].val) and (hand.cards[3].val == hand.cards[4].val):
		hand_confidences[4] += -30
	
	# Mutation Resistance: 2.76943032608%
	if ((hand.cards[3].val - hand.cards[4].val) == 8) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 1):
		hand_confidences[5] += -45
	
	# Mutation Resistance: 558.206966691%
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -65
	
	# Mutation Resistance: 0.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0) and (hand.cards[0].suit == hand.cards[1].suit) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 4]) == 1) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1) and ((hand.cards[4].val - hand.cards[3].val) == -7) and (hand.cards[4].val == hand.cards[1].val):
		hand_confidences[5] += 5
	
	# Mutation Resistance: 0.0%
	if ((hand.cards[1].val - hand.cards[2].val) == 2) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 2) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 3):
		hand_confidences[5] += -90
	
	# Mutation Resistance: 100.0%
	if (hand.cards[0].val != hand.cards[1].val):
		hand_confidences[5] += 80
	
	# Mutation Resistance: 96.2962962963%
	if (hand.cards[1].val < 13) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0):
		hand_confidences[5] += 75
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val < 6) and (hand.cards[3].suit != hand.cards[1].suit):
		hand_confidences[5] += 15
	
	# Mutation Resistance: 71.6580091638%
	if ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 8):
		hand_confidences[5] += -95
	
	# Mutation Resistance: 65.8869395712%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 2) and (hand.cards[0].suit != hand.cards[3].suit) and (hand.cards[1].suit != hand.cards[2].suit):
		hand_confidences[5] += -30
	
	# Mutation Resistance: 0.0%
	if ((hand.cards[4].val - hand.cards[0].val) == 8) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0) and (hand.cards[3].val < 7) and ((hand.cards[0].val - hand.cards[2].val) == -9) and (hand.cards[2].suit != hand.cards[0].suit) and (hand.cards[2].val < 11) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 6):
		hand_confidences[5] += 60
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val == hand.cards[3].val) and (hand.cards[0].val > 10) and (hand.cards[2].suit != hand.cards[0].suit) and (hand.cards[3].suit == hand.cards[1].suit) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 0) and ((hand.cards[0].val - hand.cards[3].val) == -3) and (hand.cards[3].val < 4) and (hand.cards[1].val == hand.cards[4].val) and (hand.cards[4].suit == hand.cards[0].suit):
		hand_confidences[5] += 50
	
	# Mutation Resistance: 29.8488110765%
	if (hand.cards[4].val > 7) and (hand.cards[1].val != hand.cards[2].val) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0) and (hand.cards[1].suit != hand.cards[4].suit) and (hand.cards[0].val != hand.cards[2].val) and (hand.cards[0].val > 11):
		hand_confidences[5] += -35
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val != hand.cards[1].val) and (hand.cards[0].suit == hand.cards[4].suit) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 3]) == 3) and (hand.cards[4].val > 1) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 3) and (hand.cards[0].val == hand.cards[1].val) and (hand.cards[3].suit != hand.cards[4].suit) and (hand.cards[2].val != hand.cards[3].val) and (hand.cards[3].val != hand.cards[0].val):
		hand_confidences[5] += 35
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val < 10) and (hand.cards[1].val < 11) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0) and (hand.cards[1].val == hand.cards[0].val) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0) and (hand.cards[1].val > 9) and (hand.cards[0].val > 11):
		hand_confidences[5] += 65
	
	# Mutation Resistance: 0.0%
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 1) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 0) and ((hand.cards[0].val - hand.cards[2].val) == -4) and ((hand.cards[4].val - hand.cards[3].val) == -6) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1) and (hand.cards[0].suit != hand.cards[2].suit):
		hand_confidences[6] += -20
	
	# Mutation Resistance: 41.6666666667%
	if (hand.cards[2].val == hand.cards[0].val):
		hand_confidences[6] += 90
	
	# Mutation Resistance: 0.0%
	if ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 8) and (hand.cards[2].val > 4) and (hand.cards[3].suit == hand.cards[4].suit) and (hand.cards[4].suit == hand.cards[1].suit):
		hand_confidences[6] += 65
	
	# Mutation Resistance: 0.0%
	if ((hand.cards[3].val - hand.cards[0].val) == 3) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 1) and ((hand.cards[1].val - hand.cards[2].val) == -6) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 4):
		hand_confidences[6] += 40
	
	# Mutation Resistance: 47.2222222222%
	if (hand.cards[1].val < 7) and (hand.cards[0].suit != hand.cards[2].suit) and (hand.cards[1].val < 9):
		hand_confidences[6] += 75
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val != hand.cards[1].val) and (hand.cards[0].val == hand.cards[3].val) and ((hand.cards[4].val - hand.cards[2].val) == -4) and (hand.cards[2].val < 13) and (hand.cards[3].val == hand.cards[2].val):
		hand_confidences[7] += 30
	
	# Mutation Resistance: 1.50014152279%
	if ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 7) and (hand.cards[2].val != hand.cards[4].val) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 3]) == 2) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0):
		hand_confidences[7] += -15
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].suit != hand.cards[2].suit) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 5) and (hand.cards[3].suit != hand.cards[2].suit) and (hand.cards[0].val < 7):
		hand_confidences[7] += 60
	
	# Mutation Resistance: 100.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0):
		hand_confidences[7] += 50
	
	# Mutation Resistance: 83.3333333333%
	if (hand.cards[4].val != hand.cards[3].val):
		hand_confidences[7] += 30
	
	# Mutation Resistance: 100.0%
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1) and (hand.cards[1].val == hand.cards[2].val) and (hand.cards[1].suit != hand.cards[3].suit):
		hand_confidences[7] += 80
	
	# Mutation Resistance: 87.9695803947%
	if (hand.cards[0].suit == hand.cards[1].suit) and (hand.cards[1].suit != hand.cards[2].suit) and (hand.cards[1].val != hand.cards[4].val):
		hand_confidences[7] += -100
	
	# Mutation Resistance: 0.0%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 3]) == 2) and (hand.cards[1].suit != hand.cards[0].suit) and (hand.cards[3].suit == hand.cards[1].suit) and (hand.cards[4].val != hand.cards[1].val) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 7) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4) and (hand.cards[1].val == hand.cards[0].val) and (hand.cards[2].val == hand.cards[0].val):
		hand_confidences[8] += 100
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].suit != hand.cards[0].suit) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(4) == 1) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(1) == 2) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 0) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 1) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 3):
		hand_confidences[8] += 5
	
	# Mutation Resistance: 0.0%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 4) and (hand.cards[2].val < 4) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 4):
		hand_confidences[8] += -55
	
	# Mutation Resistance: 100.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0):
		hand_confidences[8] += 70
	
	# Mutation Resistance: 0.0%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 8]) == 1) and (hand.cards[3].val < 10) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 6]) == 1) and (hand.cards[1].val < 4) and (hand.cards[4].val > 3):
		hand_confidences[8] += 65
	
	# Mutation Resistance: 0.0%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 2]) == 4) and (hand.cards[1].suit == hand.cards[4].suit) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 11) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 8]) == 1) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 2) and (hand.cards[4].suit != hand.cards[0].suit) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0) and (hand.cards[3].val > 11):
		hand_confidences[8] += -90
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val != hand.cards[1].val) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 3]) == 2) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 11) and (hand.cards[3].val < 5) and (hand.cards[4].suit == hand.cards[3].suit) and (hand.cards[0].suit != hand.cards[2].suit) and ((hand.cards[2].val - hand.cards[4].val) == 1) and (hand.cards[0].suit == hand.cards[4].suit):
		hand_confidences[8] += 30
	
	# Mutation Resistance: 77.4586480353%
	if (hand.cards[0].val != hand.cards[4].val) and (hand.cards[2].val == hand.cards[4].val) and (hand.cards[2].suit != hand.cards[1].suit) and (hand.cards[2].suit != hand.cards[3].suit):
		hand_confidences[8] += -55
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val < 10) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 10) and (hand.cards[4].val != hand.cards[0].val) and (hand.cards[4].suit != hand.cards[3].suit) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 5) and ((hand.cards[0].val - hand.cards[1].val) == -12) and (hand.cards[2].val < 8):
		hand_confidences[8] += 65
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val != hand.cards[4].val) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 8) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(1) == 5) and (hand.cards[0].val < 7) and (hand.cards[2].suit != hand.cards[0].suit) and (hand.cards[3].suit == hand.cards[2].suit) and (hand.cards[3].val < 3) and (hand.cards[1].val == hand.cards[4].val) and ((hand.cards[2].val - hand.cards[0].val) == 4):
		hand_confidences[8] += -10
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val < 12) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 1) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 3) and (hand.cards[2].val > 1) and ((hand.cards[4].val - hand.cards[3].val) == 11) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 5) and ((hand.cards[1].val - hand.cards[0].val) == -2) and (hand.cards[4].val < 7):
		hand_confidences[8] += 70
	
	# Mutation Resistance: 0.0%
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 3]) == 4) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 6]) == 2) and ((hand.cards[3].val - hand.cards[0].val) == -5) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 2]) == 4) and (hand.cards[3].val > 6) and (hand.cards[2].suit != hand.cards[0].suit) and (hand.cards[2].val < 13) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(3) == 1) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 2]) == 3) and (hand.cards[0].val > 12):
		hand_confidences[8] += -30
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].suit == hand.cards[1].suit) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 6]) == 2) and (hand.cards[2].val != hand.cards[1].val) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 5]) == 2) and (hand.cards[0].suit == hand.cards[3].suit) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 1) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 3]) == 1) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 1) and (hand.cards[3].val == hand.cards[0].val) and (hand.cards[0].val < 9):
		hand_confidences[8] += -90
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val != hand.cards[0].val) and (hand.cards[3].suit == hand.cards[1].suit) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 2]) == 4) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0):
		hand_confidences[8] += 50
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val < 6) and (hand.cards[0].val == hand.cards[1].val) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 7) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0) and ((hand.cards[4].val - hand.cards[3].val) == -1) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 11) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 3]) == 4):
		hand_confidences[8] += 75
	
	# Mutation Resistance: 100.0%
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 1) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(1) == 0) and (hand.cards[2].val != hand.cards[0].val):
		hand_confidences[8] += 70
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val == hand.cards[0].val) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0) and ((hand.cards[4].val - hand.cards[1].val) == -12) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0) and (hand.cards[0].val != hand.cards[1].val) and (hand.cards[1].suit != hand.cards[3].suit) and (hand.cards[1].val > 6):
		hand_confidences[9] += 25
	
	# Mutation Resistance: 0.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(1) == 5) and (hand.cards[3].val == hand.cards[4].val):
		hand_confidences[9] += 10
	
	# Mutation Resistance: 0.250751150371%
	if (hand.cards[2].val != hand.cards[0].val) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0) and (hand.cards[3].suit == hand.cards[2].suit) and (hand.cards[1].suit != hand.cards[2].suit) and (hand.cards[0].val > 1) and (hand.cards[2].val > 3) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 9) and (hand.cards[1].val > 10) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 0) and (hand.cards[0].val == hand.cards[3].val):
		hand_confidences[9] += -30
	
	# Mutation Resistance: 0.0%
	if ((hand.cards[2].val - hand.cards[3].val) == -7) and (hand.cards[0].val < 13) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 3) and (hand.cards[3].val != hand.cards[0].val) and (hand.cards[0].val > 7) and (hand.cards[3].val == hand.cards[4].val) and (hand.cards[0].val == hand.cards[2].val):
		hand_confidences[9] += 75
	
	# Mutation Resistance: 81.420623512%
	if ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 10) and (hand.cards[2].val != hand.cards[0].val):
		hand_confidences[9] += -5
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].suit != hand.cards[4].suit) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 1) and (hand.cards[3].val != hand.cards[1].val) and (hand.cards[2].suit == hand.cards[1].suit) and (hand.cards[4].suit == hand.cards[3].suit):
		hand_confidences[9] += 15
	
	# Mutation Resistance: 100.0%
	if (hand.cards[4].val != hand.cards[0].val):
		hand_confidences[9] += 65
	
	# Mutation Resistance: 560.625166037%
	if (hand.cards[3].suit != hand.cards[2].suit):
		hand_confidences[9] += -55
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val == hand.cards[4].val) and (hand.cards[1].suit == hand.cards[0].suit) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0) and (hand.cards[4].val < 6) and (hand.cards[4].val < 12):
		hand_confidences[9] += 20
	
	# Mutation Resistance: 0.0%
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(1) == 4) and (hand.cards[2].suit != hand.cards[4].suit) and (hand.cards[4].suit != hand.cards[2].suit) and (hand.cards[4].val < 9) and (hand.cards[2].suit != hand.cards[3].suit) and (hand.cards[0].val != hand.cards[4].val) and (hand.cards[0].suit != hand.cards[1].suit) and (hand.cards[4].val != hand.cards[3].val) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 9) and (hand.cards[4].val < 11):
		hand_confidences[9] += -80
	
	# Mutation Resistance: 0.0%
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0) and (hand.cards[1].val > 8) and (hand.cards[0].val == hand.cards[1].val):
		hand_confidences[9] += 70
	
	# Mutation Resistance: 0.0%
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0) and (hand.cards[1].val == hand.cards[2].val) and (hand.cards[3].suit != hand.cards[4].suit) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 2]) == 1) and ((hand.cards[4].val - hand.cards[1].val) == -7):
		hand_confidences[9] += 90
	
	# Mutation Resistance: 1.0378337579%
	if ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 10) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 3) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(1) == 1) and (hand.cards[1].suit != hand.cards[0].suit) and (hand.cards[3].val != hand.cards[2].val) and (hand.cards[0].suit == hand.cards[4].suit):
		hand_confidences[9] += -45
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val != hand.cards[0].val) and (hand.cards[1].val > 9) and (hand.cards[1].suit == hand.cards[2].suit) and (hand.cards[0].suit != hand.cards[4].suit) and ((hand.cards[4].val - hand.cards[1].val) == 2) and ((hand.cards[2].val - hand.cards[3].val) == 1):
		hand_confidences[9] += 45
	
	# Mutation Resistance: 60.0%
	if (hand.cards[3].val > 11):
		hand_confidences[9] += 30
	
	# Mutation Resistance: 0.0%
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 1) and (hand.cards[4].val == hand.cards[0].val) and (hand.cards[1].val < 10) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0) and (hand.cards[4].val == hand.cards[2].val) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 1):
		hand_confidences[9] += -30
	
	# Mutation Resistance: 0.0%
	if (hand.cards[4].val > 10) and (hand.cards[4].suit == hand.cards[0].suit) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 1) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 6) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 3) and ((hand.cards[0].val - hand.cards[1].val) == 4) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 4) and (hand.cards[2].val != hand.cards[3].val) and ((hand.cards[3].val - hand.cards[4].val) == -8) and (hand.cards[0].val > 12):
		hand_confidences[9] += 45
	
	# Mutation Resistance: 100.0%
	if (hand.cards[1].suit == hand.cards[4].suit) and (hand.cards[0].val != hand.cards[3].val):
		hand_confidences[9] += 20
	
	# Mutation Resistance: 0.0%
	if ((hand.cards[0].val - hand.cards[1].val) == -7) and (hand.cards[1].suit == hand.cards[2].suit) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 1) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 3) and (hand.cards[1].suit == hand.cards[3].suit) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 11]) == 1):
		hand_confidences[9] += -30
	
	if max(hand_confidences) >= 100:
		hand.assigned_class = hand_confidences.index(max(hand_confidences))
	else:
		hand.assigned_class = 2