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
	gene_id =  0
	if ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 4):
		hand_confidences[0] += -25
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  1
	if (hand.cards[0].val != hand.cards[2].val):
		hand_confidences[0] += 15
		hand.genes.append(gene_id)

	# Mutation Resistance: 231.087363494%
	gene_id =  2
	if ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 4):
		hand_confidences[0] += -95
		hand.genes.append(gene_id)

	# Mutation Resistance: 231.087363494%
	gene_id =  3
	if ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 4):
		hand_confidences[0] += -15
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  4
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 0) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 2):
		hand_confidences[0] += -25
		hand.genes.append(gene_id)

	# Mutation Resistance: 75.338189386%
	gene_id =  5
	if (hand.cards[1].suit != hand.cards[3].suit):
		hand_confidences[0] += 25
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  6
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 0) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 2):
		hand_confidences[0] += -35
		hand.genes.append(gene_id)

	# Mutation Resistance: 200.0%
	gene_id =  7
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1):
		hand_confidences[0] += -15
		hand.genes.append(gene_id)

	# Mutation Resistance: 200.0%
	gene_id =  8
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1):
		hand_confidences[0] += -20
		hand.genes.append(gene_id)

	# Mutation Resistance: 128.909491102%
	gene_id =  9
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 9]) == 1):
		hand_confidences[0] += -85
		hand.genes.append(gene_id)

	# Mutation Resistance: 200.0%
	gene_id =  10
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 1):
		hand_confidences[0] += -75
		hand.genes.append(gene_id)

	# Mutation Resistance: 128.27594284%
	gene_id =  11
	if (hand.cards[4].val == hand.cards[3].val):
		hand_confidences[0] += -85
		hand.genes.append(gene_id)

	# Mutation Resistance: 231.087363494%
	gene_id =  12
	if ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 4):
		hand_confidences[0] += -30
		hand.genes.append(gene_id)

	# Mutation Resistance: 128.27594284%
	gene_id =  13
	if (hand.cards[4].val == hand.cards[3].val):
		hand_confidences[0] += -60
		hand.genes.append(gene_id)

	# Mutation Resistance: 128.909491102%
	gene_id =  14
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 9]) == 1):
		hand_confidences[0] += -85
		hand.genes.append(gene_id)

	# Mutation Resistance: 128.909491102%
	gene_id =  15
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 9]) == 1):
		hand_confidences[0] += -85
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  16
	if (hand.cards[0].val == hand.cards[2].val):
		hand_confidences[0] += 35
		hand.genes.append(gene_id)

	# Mutation Resistance: 128.27594284%
	gene_id =  17
	if (hand.cards[4].val == hand.cards[3].val):
		hand_confidences[0] += -75
		hand.genes.append(gene_id)

	# Mutation Resistance: 128.27594284%
	gene_id =  18
	if (hand.cards[4].val == hand.cards[3].val):
		hand_confidences[0] += -100
		hand.genes.append(gene_id)

	# Mutation Resistance: 128.909491102%
	gene_id =  19
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 9]) == 1):
		hand_confidences[0] += -75
		hand.genes.append(gene_id)

	# Mutation Resistance: 179.490713226%
	gene_id =  20
	if (hand.cards[1].val == hand.cards[0].val):
		hand_confidences[0] += -95
		hand.genes.append(gene_id)

	# Mutation Resistance: 200.0%
	gene_id =  21
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 1):
		hand_confidences[0] += -20
		hand.genes.append(gene_id)

	# Mutation Resistance: 128.27594284%
	gene_id =  22
	if (hand.cards[4].val == hand.cards[3].val):
		hand_confidences[0] += -95
		hand.genes.append(gene_id)

	# Mutation Resistance: 200.0%
	gene_id =  23
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1):
		hand_confidences[0] += -80
		hand.genes.append(gene_id)

	# Mutation Resistance: 200.0%
	gene_id =  24
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 1):
		hand_confidences[0] += -100
		hand.genes.append(gene_id)

	# Mutation Resistance: 64.5161290323%
	gene_id =  25
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4) and (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[0] += -75
		hand.genes.append(gene_id)

	# Mutation Resistance: 231.087363494%
	gene_id =  26
	if ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 4):
		hand_confidences[0] += -20
		hand.genes.append(gene_id)

	# Mutation Resistance: 200.0%
	gene_id =  27
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1):
		hand_confidences[0] += -40
		hand.genes.append(gene_id)

	# Mutation Resistance: 75.2501400784%
	gene_id =  28
	if (hand.cards[4].suit != hand.cards[3].suit):
		hand_confidences[0] += 65
		hand.genes.append(gene_id)

	# Mutation Resistance: 333.05234099%
	gene_id =  29
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(1) == 0):
		hand_confidences[0] += -80
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  30
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 0) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 2):
		hand_confidences[0] += -95
		hand.genes.append(gene_id)

	# Mutation Resistance: 200.0%
	gene_id =  31
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1):
		hand_confidences[0] += -75
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  32
	if (hand.cards[0].val != hand.cards[2].val):
		hand_confidences[0] += 65
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  33
	if (hand.cards[0].val != hand.cards[2].val):
		hand_confidences[0] += 75
		hand.genes.append(gene_id)

	# Mutation Resistance: 5.27495397423%
	gene_id =  34
	if (hand.cards[3].suit != hand.cards[1].suit) and ((hand.cards[0].val - hand.cards[3].val) == -2):
		hand_confidences[0] += 10
		hand.genes.append(gene_id)

	# Mutation Resistance: 89.7160109444%
	gene_id =  35
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 1) and (hand.cards[4].val != hand.cards[0].val):
		hand_confidences[1] += 85
		hand.genes.append(gene_id)

	# Mutation Resistance: 700.0%
	gene_id =  36
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0):
		hand_confidences[1] += -5
		hand.genes.append(gene_id)

	# Mutation Resistance: 89.7160109444%
	gene_id =  37
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 1) and (hand.cards[4].val != hand.cards[0].val):
		hand_confidences[1] += 30
		hand.genes.append(gene_id)

	# Mutation Resistance: 90.1783187093%
	gene_id =  38
	if (hand.cards[0].val != hand.cards[3].val) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 3):
		hand_confidences[1] += 75
		hand.genes.append(gene_id)

	# Mutation Resistance: 93.6623024037%
	gene_id =  39
	if (hand.cards[0].val > 1) and (hand.cards[1].val > 8) and (hand.cards[0].suit == hand.cards[3].suit) and (hand.cards[2].val < 13) and (hand.cards[3].val > 8):
		hand_confidences[1] += -25
		hand.genes.append(gene_id)

	# Mutation Resistance: 89.7160109444%
	gene_id =  40
	if (hand.cards[4].val != hand.cards[0].val) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 1):
		hand_confidences[1] += 35
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  41
	if ((hand.cards[0].val - hand.cards[4].val) == -2) and (hand.cards[1].suit != hand.cards[3].suit) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 3) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 5) and (hand.cards[2].suit != hand.cards[3].suit) and (hand.cards[4].val == hand.cards[0].val):
		hand_confidences[1] += -65
		hand.genes.append(gene_id)

	# Mutation Resistance: 700.0%
	gene_id =  42
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0):
		hand_confidences[1] += -90
		hand.genes.append(gene_id)

	# Mutation Resistance: 89.7160109444%
	gene_id =  43
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 1) and (hand.cards[4].val != hand.cards[0].val):
		hand_confidences[1] += 80
		hand.genes.append(gene_id)

	# Mutation Resistance: 90.1783187093%
	gene_id =  44
	if (hand.cards[0].val != hand.cards[3].val) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 3):
		hand_confidences[1] += 100
		hand.genes.append(gene_id)

	# Mutation Resistance: 81.5057243205%
	gene_id =  45
	if (hand.cards[4].suit != hand.cards[2].suit) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 0) and (hand.cards[1].suit == hand.cards[2].suit):
		hand_confidences[1] += -20
		hand.genes.append(gene_id)

	# Mutation Resistance: 186.695602973%
	gene_id =  46
	if (hand.cards[1].val == hand.cards[2].val):
		hand_confidences[2] += -25
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  47
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 1):
		hand_confidences[2] += 60
		hand.genes.append(gene_id)

	# Mutation Resistance: 300.0%
	gene_id =  48
	if (hand.cards[2].suit == hand.cards[1].suit) and (hand.cards[2].val != hand.cards[3].val) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 1) and (hand.cards[0].suit == hand.cards[4].suit):
		hand_confidences[2] += -20
		hand.genes.append(gene_id)

	# Mutation Resistance: 87.1832358674%
	gene_id =  49
	if (hand.cards[1].val == hand.cards[2].val) and (hand.cards[0].val == hand.cards[1].val) and (hand.cards[0].val < 11):
		hand_confidences[2] += -60
		hand.genes.append(gene_id)

	# Mutation Resistance: 186.695602973%
	gene_id =  50
	if (hand.cards[1].val == hand.cards[2].val):
		hand_confidences[2] += -35
		hand.genes.append(gene_id)

	# Mutation Resistance: 186.695602973%
	gene_id =  51
	if (hand.cards[1].val == hand.cards[2].val):
		hand_confidences[2] += -75
		hand.genes.append(gene_id)

	# Mutation Resistance: 186.695602973%
	gene_id =  52
	if (hand.cards[1].val == hand.cards[2].val):
		hand_confidences[2] += -20
		hand.genes.append(gene_id)

	# Mutation Resistance: 72.4906426625%
	gene_id =  53
	if (hand.cards[3].suit == hand.cards[0].suit) and (hand.cards[4].suit != hand.cards[1].suit) and (hand.cards[2].suit != hand.cards[1].suit):
		hand_confidences[2] += -15
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  54
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 1):
		hand_confidences[2] += 5
		hand.genes.append(gene_id)

	# Mutation Resistance: 66.6666666667%
	gene_id =  55
	if (hand.cards[2].val > 4) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(4) == 1) and (hand.cards[3].suit != hand.cards[4].suit):
		hand_confidences[2] += -70
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  56
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 1):
		hand_confidences[2] += 85
		hand.genes.append(gene_id)

	# Mutation Resistance: 77.3631840796%
	gene_id =  57
	if (hand.cards[4].val < 11) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 1):
		hand_confidences[2] += 20
		hand.genes.append(gene_id)

	# Mutation Resistance: 326.016113872%
	gene_id =  58
	if (hand.cards[3].val != hand.cards[4].val) and (hand.cards[4].suit == hand.cards[2].suit) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0):
		hand_confidences[2] += -35
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  59
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 1):
		hand_confidences[2] += 30
		hand.genes.append(gene_id)

	# Mutation Resistance: 153.28679082%
	gene_id =  60
	if (hand.cards[3].val == hand.cards[2].val):
		hand_confidences[2] += -55
		hand.genes.append(gene_id)

	# Mutation Resistance: 186.695602973%
	gene_id =  61
	if (hand.cards[1].val == hand.cards[2].val):
		hand_confidences[2] += -45
		hand.genes.append(gene_id)

	# Mutation Resistance: 79.1873963516%
	gene_id =  62
	if (hand.cards[3].val != hand.cards[1].val):
		hand_confidences[2] += 35
		hand.genes.append(gene_id)

	# Mutation Resistance: 148.260754565%
	gene_id =  63
	if (hand.cards[0].val < 8) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0) and (hand.cards[4].val < 10):
		hand_confidences[2] += -50
		hand.genes.append(gene_id)

	# Mutation Resistance: 186.695602973%
	gene_id =  64
	if (hand.cards[1].val == hand.cards[2].val):
		hand_confidences[2] += -20
		hand.genes.append(gene_id)

	# Mutation Resistance: 187.096774194%
	gene_id =  65
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4):
		hand_confidences[2] += -15
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  66
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 1):
		hand_confidences[2] += 15
		hand.genes.append(gene_id)

	# Mutation Resistance: 153.28679082%
	gene_id =  67
	if (hand.cards[3].val == hand.cards[2].val):
		hand_confidences[2] += -90
		hand.genes.append(gene_id)

	# Mutation Resistance: 300.0%
	gene_id =  68
	if (hand.cards[2].suit == hand.cards[1].suit) and (hand.cards[0].suit == hand.cards[4].suit) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 1) and (hand.cards[2].val != hand.cards[3].val):
		hand_confidences[2] += -70
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  69
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 1):
		hand_confidences[2] += 90
		hand.genes.append(gene_id)

	# Mutation Resistance: 95.6649198396%
	gene_id =  70
	if (hand.cards[0].val != hand.cards[4].val) and (hand.cards[0].suit != hand.cards[4].suit) and (hand.cards[2].val == hand.cards[0].val):
		hand_confidences[2] += -65
		hand.genes.append(gene_id)

	# Mutation Resistance: 187.096774194%
	gene_id =  71
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4):
		hand_confidences[2] += -85
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  72
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 1):
		hand_confidences[2] += 85
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  73
	if (hand.cards[4].val > 3) and (hand.cards[2].val != hand.cards[1].val) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 3]) == 4) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 4]) == 1) and ((hand.cards[4].val - hand.cards[3].val) == 5) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 10) and (hand.cards[1].val == hand.cards[2].val) and (hand.cards[1].val > 7) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 1) and (hand.cards[4].suit == hand.cards[1].suit) and (hand.cards[3].val < 10) and (hand.cards[2].val != hand.cards[0].val) and (hand.cards[3].suit != hand.cards[0].suit) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 1):
		hand_confidences[2] += -20
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  74
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 1) and ((hand.cards[0].val - hand.cards[3].val) == 5) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0) and ((hand.cards[2].val - hand.cards[0].val) == -3) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 1) and ((hand.cards[3].val - hand.cards[2].val) == 12) and (hand.cards[1].val > 12) and (hand.cards[2].val < 3) and (hand.cards[3].val < 11) and ((hand.cards[2].val - hand.cards[3].val) == -1) and (hand.cards[1].val == hand.cards[0].val):
		hand_confidences[2] += -10
		hand.genes.append(gene_id)

	# Mutation Resistance: 2.39645249552%
	gene_id =  75
	if (hand.cards[4].val == hand.cards[3].val) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0):
		hand_confidences[2] += -80
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  76
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 2) and ((hand.cards[2].val - hand.cards[4].val) == -4) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 2) and ((hand.cards[0].val - hand.cards[1].val) == -4) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 10]) == 1):
		hand_confidences[2] += -85
		hand.genes.append(gene_id)

	# Mutation Resistance: 458.903535492%
	gene_id =  77
	if (hand.cards[1].val < 8):
		hand_confidences[3] += -20
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  78
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 2):
		hand_confidences[3] += 75
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  79
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 2):
		hand_confidences[3] += 65
		hand.genes.append(gene_id)

	# Mutation Resistance: 90.0584795322%
	gene_id =  80
	if (hand.cards[4].val > 1):
		hand_confidences[3] += 60
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  81
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 2):
		hand_confidences[3] += 5
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  82
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 2):
		hand_confidences[3] += 40
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  83
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 2):
		hand_confidences[3] += 80
		hand.genes.append(gene_id)

	# Mutation Resistance: 113.908285282%
	gene_id =  84
	if (hand.cards[4].val > 10) and (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[3] += -5
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  85
	if (hand.cards[1].suit == hand.cards[3].suit) and (hand.cards[1].val == hand.cards[3].val) and (hand.cards[3].suit != hand.cards[2].suit) and (hand.cards[0].suit == hand.cards[1].suit):
		hand_confidences[3] += 25
		hand.genes.append(gene_id)

	# Mutation Resistance: 115.053763441%
	gene_id =  86
	if (hand.cards[1].suit == hand.cards[4].suit) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0) and (hand.cards[1].val != hand.cards[4].val):
		hand_confidences[3] += -50
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  87
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 2):
		hand_confidences[3] += 40
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  88
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 2):
		hand_confidences[3] += 20
		hand.genes.append(gene_id)

	# Mutation Resistance: 4.82053691423%
	gene_id =  89
	if (hand.cards[1].val < 2) and (hand.cards[1].val < 13) and (hand.cards[2].suit != hand.cards[3].suit) and (hand.cards[4].suit == hand.cards[1].suit):
		hand_confidences[3] += -100
		hand.genes.append(gene_id)

	# Mutation Resistance: 115.053763441%
	gene_id =  90
	if (hand.cards[1].val != hand.cards[4].val) and (hand.cards[1].suit == hand.cards[4].suit) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4):
		hand_confidences[3] += -60
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  91
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 2]) == 3) and (hand.cards[0].suit == hand.cards[1].suit) and (hand.cards[4].val == hand.cards[0].val) and (hand.cards[1].val == hand.cards[0].val) and (hand.cards[3].suit == hand.cards[2].suit) and (hand.cards[3].val > 3) and (hand.cards[3].suit == hand.cards[1].suit) and (hand.cards[3].suit != hand.cards[0].suit):
		hand_confidences[3] += 100
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  92
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 2):
		hand_confidences[3] += 85
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  93
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 2):
		hand_confidences[3] += 35
		hand.genes.append(gene_id)

	# Mutation Resistance: 889.223155646%
	gene_id =  94
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0):
		hand_confidences[3] += -95
		hand.genes.append(gene_id)

	# Mutation Resistance: 743.316844313%
	gene_id =  95
	if (hand.cards[3].val < 12):
		hand_confidences[3] += -100
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  96
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 2):
		hand_confidences[3] += 50
		hand.genes.append(gene_id)

	# Mutation Resistance: 771.058708019%
	gene_id =  97
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0):
		hand_confidences[3] += -65
		hand.genes.append(gene_id)

	# Mutation Resistance: 115.053763441%
	gene_id =  98
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4) and (hand.cards[0].val < 10) and (hand.cards[3].suit == hand.cards[2].suit):
		hand_confidences[3] += -20
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  99
	if (hand.cards[1].val != hand.cards[3].val) and (hand.cards[0].val > 1) and (hand.cards[2].val == hand.cards[1].val) and (hand.cards[2].val > 4) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0) and (hand.cards[1].val == hand.cards[3].val) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 10):
		hand_confidences[3] += -95
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  100
	if ((hand.cards[1].val - hand.cards[4].val) == -12) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4) and (hand.cards[4].val < 9) and (hand.cards[2].val > 9):
		hand_confidences[3] += -80
		hand.genes.append(gene_id)

	# Mutation Resistance: 5.06822612086%
	gene_id =  101
	if (hand.cards[1].val == hand.cards[4].val) and (hand.cards[3].suit != hand.cards[0].suit) and (hand.cards[2].suit == hand.cards[0].suit):
		hand_confidences[3] += 5
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  102
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 5):
		hand_confidences[4] += 100
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  103
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 5):
		hand_confidences[4] += 75
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  104
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 3):
		hand_confidences[4] += -15
		hand.genes.append(gene_id)

	# Mutation Resistance: 691.662605983%
	gene_id =  105
	if (hand.cards[2].val != hand.cards[1].val):
		hand_confidences[4] += -45
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  106
	if (hand.cards[1].val == hand.cards[3].val) and (hand.cards[2].val < 3) and (hand.cards[1].suit != hand.cards[3].suit) and (hand.cards[4].val > 10) and (hand.cards[2].val != hand.cards[0].val) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 1):
		hand_confidences[4] += -100
		hand.genes.append(gene_id)

	# Mutation Resistance: 147.606985838%
	gene_id =  107
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 5) and (hand.cards[3].val < 7):
		hand_confidences[4] += -10
		hand.genes.append(gene_id)

	# Mutation Resistance: 12.9032258065%
	gene_id =  108
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 3):
		hand_confidences[4] += 85
		hand.genes.append(gene_id)

	# Mutation Resistance: 129.243389163%
	gene_id =  109
	if (hand.cards[0].suit == hand.cards[1].suit) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0) and (hand.cards[2].val < 11) and (hand.cards[1].val != hand.cards[2].val) and (hand.cards[0].val < 8):
		hand_confidences[4] += -55
		hand.genes.append(gene_id)

	# Mutation Resistance: 67.7419354839%
	gene_id =  110
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4) and (hand.cards[0].suit != hand.cards[1].suit):
		hand_confidences[4] += 10
		hand.genes.append(gene_id)

	# Mutation Resistance: 389.600875379%
	gene_id =  111
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0) and (hand.cards[1].suit == hand.cards[4].suit):
		hand_confidences[4] += -70
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  112
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 3) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1):
		hand_confidences[4] += -40
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  113
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 3) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1):
		hand_confidences[4] += -65
		hand.genes.append(gene_id)

	# Mutation Resistance: 127.697547769%
	gene_id =  114
	if (hand.cards[1].val == hand.cards[4].val):
		hand_confidences[4] += -5
		hand.genes.append(gene_id)

	# Mutation Resistance: 79.9999743479%
	gene_id =  115
	if (hand.cards[3].val == hand.cards[1].val) and (hand.cards[4].val > 8):
		hand_confidences[4] += -75
		hand.genes.append(gene_id)

	# Mutation Resistance: 63.4408602151%
	gene_id =  116
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4) and (hand.cards[0].suit != hand.cards[3].suit):
		hand_confidences[4] += 65
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  117
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 5):
		hand_confidences[4] += 30
		hand.genes.append(gene_id)

	# Mutation Resistance: 161.28170053%
	gene_id =  118
	if (hand.cards[2].val > 8) and (hand.cards[1].val < 10):
		hand_confidences[4] += -35
		hand.genes.append(gene_id)

	# Mutation Resistance: 389.600875379%
	gene_id =  119
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0) and (hand.cards[1].suit == hand.cards[4].suit):
		hand_confidences[4] += -90
		hand.genes.append(gene_id)

	# Mutation Resistance: 64.5161290323%
	gene_id =  120
	if (hand.cards[0].suit != hand.cards[4].suit) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4):
		hand_confidences[4] += 60
		hand.genes.append(gene_id)

	# Mutation Resistance: 72.0430107527%
	gene_id =  121
	if (hand.cards[1].suit != hand.cards[4].suit) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4):
		hand_confidences[4] += 95
		hand.genes.append(gene_id)

	# Mutation Resistance: 691.662605983%
	gene_id =  122
	if (hand.cards[2].val != hand.cards[1].val):
		hand_confidences[4] += -70
		hand.genes.append(gene_id)

	# Mutation Resistance: 499.738098135%
	gene_id =  123
	if (hand.cards[3].suit != hand.cards[0].suit):
		hand_confidences[4] += -35
		hand.genes.append(gene_id)

	# Mutation Resistance: 64.5161290323%
	gene_id =  124
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4) and (hand.cards[0].suit != hand.cards[4].suit):
		hand_confidences[4] += 80
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  125
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 5):
		hand_confidences[4] += 5
		hand.genes.append(gene_id)

	# Mutation Resistance: 67.7419354839%
	gene_id =  126
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4) and (hand.cards[0].suit != hand.cards[1].suit):
		hand_confidences[4] += 85
		hand.genes.append(gene_id)

	# Mutation Resistance: 389.600875379%
	gene_id =  127
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0) and (hand.cards[1].suit == hand.cards[4].suit):
		hand_confidences[4] += -85
		hand.genes.append(gene_id)

	# Mutation Resistance: 79.9999743479%
	gene_id =  128
	if (hand.cards[3].val == hand.cards[1].val) and (hand.cards[4].val > 8):
		hand_confidences[4] += -25
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  129
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 2) and (hand.cards[0].suit != hand.cards[3].suit):
		hand_confidences[4] += 25
		hand.genes.append(gene_id)

	# Mutation Resistance: 691.662605983%
	gene_id =  130
	if (hand.cards[2].val != hand.cards[1].val):
		hand_confidences[4] += -25
		hand.genes.append(gene_id)

	# Mutation Resistance: 68.8172043011%
	gene_id =  131
	if (hand.cards[2].suit != hand.cards[3].suit) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4):
		hand_confidences[4] += 75
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  132
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 5):
		hand_confidences[4] += 30
		hand.genes.append(gene_id)

	# Mutation Resistance: 12.9032258065%
	gene_id =  133
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 3):
		hand_confidences[4] += 75
		hand.genes.append(gene_id)

	# Mutation Resistance: 67.7419354839%
	gene_id =  134
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4) and (hand.cards[0].suit != hand.cards[1].suit):
		hand_confidences[4] += 15
		hand.genes.append(gene_id)

	# Mutation Resistance: 3.66515376335%
	gene_id =  135
	if (hand.cards[2].suit != hand.cards[0].suit) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 11]) == 1):
		hand_confidences[4] += -10
		hand.genes.append(gene_id)

	# Mutation Resistance: 67.7419354839%
	gene_id =  136
	if (hand.cards[0].suit != hand.cards[1].suit) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4):
		hand_confidences[4] += 35
		hand.genes.append(gene_id)

	# Mutation Resistance: 208.337394017%
	gene_id =  137
	if (hand.cards[2].val == hand.cards[1].val):
		hand_confidences[4] += -100
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  138
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 3):
		hand_confidences[4] += -70
		hand.genes.append(gene_id)

	# Mutation Resistance: 389.600875379%
	gene_id =  139
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0) and (hand.cards[1].suit == hand.cards[4].suit):
		hand_confidences[4] += -40
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  140
	if (hand.cards[2].suit == hand.cards[4].suit) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 11]) == 1) and (hand.cards[3].suit != hand.cards[4].suit) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 5) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 2]) == 4) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 5) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 6) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 12]) == 1) and (hand.cards[2].suit != hand.cards[0].suit) and (hand.cards[0].suit == hand.cards[1].suit) and (hand.cards[2].val > 7) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(1) == 0) and (hand.cards[4].val < 4):
		hand_confidences[4] += -20
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  141
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 3):
		hand_confidences[4] += -60
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  142
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 3):
		hand_confidences[4] += -30
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  143
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 5):
		hand_confidences[4] += 50
		hand.genes.append(gene_id)

	# Mutation Resistance: 691.662605983%
	gene_id =  144
	if (hand.cards[2].val != hand.cards[1].val):
		hand_confidences[4] += -65
		hand.genes.append(gene_id)

	# Mutation Resistance: 79.9999743479%
	gene_id =  145
	if (hand.cards[3].val == hand.cards[1].val) and (hand.cards[4].val > 8):
		hand_confidences[4] += -85
		hand.genes.append(gene_id)

	# Mutation Resistance: 147.606985838%
	gene_id =  146
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 5) and (hand.cards[3].val < 7):
		hand_confidences[4] += -5
		hand.genes.append(gene_id)

	# Mutation Resistance: 67.7419354839%
	gene_id =  147
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4) and (hand.cards[0].suit != hand.cards[1].suit):
		hand_confidences[4] += 90
		hand.genes.append(gene_id)

	# Mutation Resistance: 67.7419354839%
	gene_id =  148
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4) and (hand.cards[0].suit != hand.cards[1].suit):
		hand_confidences[4] += 20
		hand.genes.append(gene_id)

	# Mutation Resistance: 147.606985838%
	gene_id =  149
	if (hand.cards[3].val < 7) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 5):
		hand_confidences[4] += -75
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  150
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0) and (hand.cards[4].suit != hand.cards[3].suit) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 6]) == 2) and (hand.cards[4].val == hand.cards[1].val) and (hand.cards[1].val != hand.cards[2].val) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 9) and (hand.cards[0].val == hand.cards[1].val) and (hand.cards[3].suit != hand.cards[4].suit) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 1):
		hand_confidences[4] += 80
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  151
	if (hand.cards[2].val > 10) and (hand.cards[0].val == hand.cards[1].val) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 1) and (hand.cards[3].val == hand.cards[0].val) and (hand.cards[4].suit != hand.cards[3].suit) and (hand.cards[1].val != hand.cards[3].val) and (hand.cards[4].val != hand.cards[3].val):
		hand_confidences[4] += -90
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  152
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 0) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(4) == 1):
		hand_confidences[5] += -95
		hand.genes.append(gene_id)

	# Mutation Resistance: 558.206966691%
	gene_id =  153
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -25
		hand.genes.append(gene_id)

	# Mutation Resistance: 558.206966691%
	gene_id =  154
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -55
		hand.genes.append(gene_id)

	# Mutation Resistance: 558.206966691%
	gene_id =  155
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -10
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  156
	if (hand.cards[4].suit == hand.cards[3].suit):
		hand_confidences[5] += 15
		hand.genes.append(gene_id)

	# Mutation Resistance: 155.6297773%
	gene_id =  157
	if (hand.cards[0].val == hand.cards[3].val) and (hand.cards[3].val < 12):
		hand_confidences[5] += -60
		hand.genes.append(gene_id)

	# Mutation Resistance: 127.697547769%
	gene_id =  158
	if (hand.cards[4].val == hand.cards[1].val):
		hand_confidences[5] += -85
		hand.genes.append(gene_id)

	# Mutation Resistance: 558.206966691%
	gene_id =  159
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -80
		hand.genes.append(gene_id)

	# Mutation Resistance: 137.4923716%
	gene_id =  160
	if (hand.cards[0].val == hand.cards[1].val) and (hand.cards[2].val != hand.cards[4].val):
		hand_confidences[5] += -100
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  161
	if (hand.cards[4].suit == hand.cards[3].suit):
		hand_confidences[5] += 75
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  162
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(4) == 1) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 0):
		hand_confidences[5] += -30
		hand.genes.append(gene_id)

	# Mutation Resistance: 559.353910415%
	gene_id =  163
	if (hand.cards[2].suit != hand.cards[4].suit):
		hand_confidences[5] += -35
		hand.genes.append(gene_id)

	# Mutation Resistance: 187.096774194%
	gene_id =  164
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4) and (hand.cards[1].val != hand.cards[0].val):
		hand_confidences[5] += -90
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  165
	if (hand.cards[0].val > 4) and (hand.cards[0].suit == hand.cards[1].suit) and (hand.cards[2].val != hand.cards[4].val) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 2) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 3]) == 3) and (hand.cards[1].val > 1) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 6]) == 2) and (hand.cards[0].val == hand.cards[4].val):
		hand_confidences[5] += -25
		hand.genes.append(gene_id)

	# Mutation Resistance: 475.852879877%
	gene_id =  166
	if (hand.cards[4].val != hand.cards[0].val) and (hand.cards[0].suit != hand.cards[2].suit):
		hand_confidences[5] += -65
		hand.genes.append(gene_id)

	# Mutation Resistance: 558.206966691%
	gene_id =  167
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -60
		hand.genes.append(gene_id)

	# Mutation Resistance: 569.630571253%
	gene_id =  168
	if (hand.cards[3].suit != hand.cards[0].suit):
		hand_confidences[5] += -40
		hand.genes.append(gene_id)

	# Mutation Resistance: 42.5925925926%
	gene_id =  169
	if (hand.cards[2].val != hand.cards[4].val) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 2):
		hand_confidences[5] += 80
		hand.genes.append(gene_id)

	# Mutation Resistance: 559.353910415%
	gene_id =  170
	if (hand.cards[2].suit != hand.cards[4].suit):
		hand_confidences[5] += -75
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  171
	if (hand.cards[3].val != hand.cards[0].val) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 2]) == 4) and (hand.cards[1].val < 3):
		hand_confidences[5] += 30
		hand.genes.append(gene_id)

	# Mutation Resistance: 600.906646657%
	gene_id =  172
	if (hand.cards[4].val > 3) and (hand.cards[4].val != hand.cards[0].val):
		hand_confidences[5] += -10
		hand.genes.append(gene_id)

	# Mutation Resistance: 14.3005731576%
	gene_id =  173
	if ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 2) and (hand.cards[0].val != hand.cards[3].val):
		hand_confidences[5] += -10
		hand.genes.append(gene_id)

	# Mutation Resistance: 174.099394469%
	gene_id =  174
	if (hand.cards[2].val == hand.cards[3].val):
		hand_confidences[5] += -75
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  175
	if ((hand.cards[4].val - hand.cards[0].val) == -8) and (hand.cards[3].suit == hand.cards[0].suit) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 1) and ((hand.cards[3].val - hand.cards[4].val) == 5) and (hand.cards[1].val > 3) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 12]) == 1) and (hand.cards[3].suit == hand.cards[2].suit):
		hand_confidences[5] += -75
		hand.genes.append(gene_id)

	# Mutation Resistance: 109.138635299%
	gene_id =  176
	if (hand.cards[2].val != hand.cards[0].val) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 12) and (hand.cards[1].suit == hand.cards[4].suit):
		hand_confidences[5] += -5
		hand.genes.append(gene_id)

	# Mutation Resistance: 329.46712745%
	gene_id =  177
	if (hand.cards[1].val > 9):
		hand_confidences[5] += -50
		hand.genes.append(gene_id)

	# Mutation Resistance: 558.206966691%
	gene_id =  178
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -40
		hand.genes.append(gene_id)

	# Mutation Resistance: 559.353910415%
	gene_id =  179
	if (hand.cards[2].suit != hand.cards[4].suit):
		hand_confidences[5] += -65
		hand.genes.append(gene_id)

	# Mutation Resistance: 53.2400230835%
	gene_id =  180
	if (hand.cards[3].val < 4) and (hand.cards[3].suit != hand.cards[1].suit) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0) and (hand.cards[4].val < 8):
		hand_confidences[5] += -25
		hand.genes.append(gene_id)

	# Mutation Resistance: 558.206966691%
	gene_id =  181
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -15
		hand.genes.append(gene_id)

	# Mutation Resistance: 103.819713867%
	gene_id =  182
	if (hand.cards[3].suit != hand.cards[1].suit) and (hand.cards[3].val > 1) and (hand.cards[0].suit == hand.cards[4].suit):
		hand_confidences[5] += -65
		hand.genes.append(gene_id)

	# Mutation Resistance: 558.206966691%
	gene_id =  183
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -65
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  184
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 4]) == 2) and (hand.cards[0].val == hand.cards[4].val) and ((hand.cards[3].val - hand.cards[1].val) == -8) and (hand.cards[4].suit != hand.cards[1].suit) and ((hand.cards[4].val - hand.cards[1].val) == 8):
		hand_confidences[5] += -30
		hand.genes.append(gene_id)

	# Mutation Resistance: 600.906646657%
	gene_id =  185
	if (hand.cards[4].val > 3) and (hand.cards[4].val != hand.cards[0].val):
		hand_confidences[5] += -10
		hand.genes.append(gene_id)

	# Mutation Resistance: 127.697547769%
	gene_id =  186
	if (hand.cards[4].val == hand.cards[1].val):
		hand_confidences[5] += -90
		hand.genes.append(gene_id)

	# Mutation Resistance: 187.096774194%
	gene_id =  187
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4) and (hand.cards[1].val != hand.cards[0].val):
		hand_confidences[5] += -20
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  188
	if (hand.cards[4].suit == hand.cards[0].suit):
		hand_confidences[5] += 25
		hand.genes.append(gene_id)

	# Mutation Resistance: 187.096774194%
	gene_id =  189
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4) and (hand.cards[1].val != hand.cards[0].val):
		hand_confidences[5] += -65
		hand.genes.append(gene_id)

	# Mutation Resistance: 329.46712745%
	gene_id =  190
	if (hand.cards[1].val > 9):
		hand_confidences[5] += -25
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  191
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 8]) == 1) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 12]) == 1) and (hand.cards[1].val != hand.cards[3].val) and (hand.cards[4].val != hand.cards[3].val) and (hand.cards[4].val != hand.cards[0].val):
		hand_confidences[5] += 45
		hand.genes.append(gene_id)

	# Mutation Resistance: 558.206966691%
	gene_id =  192
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -5
		hand.genes.append(gene_id)

	# Mutation Resistance: 558.206966691%
	gene_id =  193
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -15
		hand.genes.append(gene_id)

	# Mutation Resistance: 558.206966691%
	gene_id =  194
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -40
		hand.genes.append(gene_id)

	# Mutation Resistance: 137.4923716%
	gene_id =  195
	if (hand.cards[0].val == hand.cards[1].val) and (hand.cards[2].val != hand.cards[4].val):
		hand_confidences[5] += -40
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  196
	if (hand.cards[1].val > 10) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 3]) == 4) and (hand.cards[0].suit == hand.cards[2].suit) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 3) and (hand.cards[4].val != hand.cards[0].val) and (hand.cards[3].val != hand.cards[0].val) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0) and ((hand.cards[3].val - hand.cards[2].val) == 10) and ((hand.cards[4].val - hand.cards[2].val) == -5) and (hand.cards[4].val < 9) and ((hand.cards[4].val - hand.cards[1].val) == 2) and (hand.cards[4].suit == hand.cards[3].suit):
		hand_confidences[5] += -5
		hand.genes.append(gene_id)

	# Mutation Resistance: 558.206966691%
	gene_id =  197
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -15
		hand.genes.append(gene_id)

	# Mutation Resistance: 558.206966691%
	gene_id =  198
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -60
		hand.genes.append(gene_id)

	# Mutation Resistance: 558.206966691%
	gene_id =  199
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -55
		hand.genes.append(gene_id)

	# Mutation Resistance: 558.206966691%
	gene_id =  200
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -20
		hand.genes.append(gene_id)

	# Mutation Resistance: 103.819713867%
	gene_id =  201
	if (hand.cards[3].val > 1) and (hand.cards[3].suit != hand.cards[1].suit) and (hand.cards[0].suit == hand.cards[4].suit):
		hand_confidences[5] += -90
		hand.genes.append(gene_id)

	# Mutation Resistance: 559.353910415%
	gene_id =  202
	if (hand.cards[2].suit != hand.cards[4].suit):
		hand_confidences[5] += -35
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  203
	if (hand.cards[4].suit == hand.cards[3].suit):
		hand_confidences[5] += 90
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  204
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 2]) == 4) and ((hand.cards[0].val - hand.cards[3].val) == -7) and (hand.cards[2].suit != hand.cards[0].suit) and (hand.cards[3].suit == hand.cards[2].suit) and (hand.cards[4].suit == hand.cards[1].suit) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 0):
		hand_confidences[5] += 30
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  205
	if ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 10) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 3) and (hand.cards[3].val != hand.cards[2].val) and (hand.cards[4].val == hand.cards[1].val) and (hand.cards[3].suit == hand.cards[0].suit) and (hand.cards[0].suit != hand.cards[4].suit):
		hand_confidences[5] += 35
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  206
	if (hand.cards[4].suit == hand.cards[3].suit):
		hand_confidences[5] += 15
		hand.genes.append(gene_id)

	# Mutation Resistance: 103.819713867%
	gene_id =  207
	if (hand.cards[3].suit != hand.cards[1].suit) and (hand.cards[3].val > 1) and (hand.cards[0].suit == hand.cards[4].suit):
		hand_confidences[5] += -75
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.575775925608%
	gene_id =  208
	if (hand.cards[4].val == hand.cards[2].val) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 6]) == 1) and (hand.cards[0].val != hand.cards[2].val) and (hand.cards[1].val < 2):
		hand_confidences[5] += -35
		hand.genes.append(gene_id)

	# Mutation Resistance: 109.138635299%
	gene_id =  209
	if (hand.cards[1].suit == hand.cards[4].suit) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 12) and (hand.cards[2].val != hand.cards[0].val):
		hand_confidences[5] += -55
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  210
	if (hand.cards[2].val == hand.cards[0].val) and ((hand.cards[2].val - hand.cards[1].val) == 12) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 2) and (hand.cards[4].val == hand.cards[3].val) and ((hand.cards[2].val - hand.cards[4].val) == 10) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0) and (hand.cards[1].val != hand.cards[2].val) and (hand.cards[3].val != hand.cards[0].val) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 1) and (hand.cards[3].val > 9) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(4) == 1) and (hand.cards[1].val != hand.cards[4].val) and (hand.cards[2].suit == hand.cards[0].suit):
		hand_confidences[5] += -20
		hand.genes.append(gene_id)

	# Mutation Resistance: 558.206966691%
	gene_id =  211
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -55
		hand.genes.append(gene_id)

	# Mutation Resistance: 137.4923716%
	gene_id =  212
	if (hand.cards[0].val == hand.cards[1].val) and (hand.cards[2].val != hand.cards[4].val):
		hand_confidences[5] += -40
		hand.genes.append(gene_id)

	# Mutation Resistance: 137.4923716%
	gene_id =  213
	if (hand.cards[2].val != hand.cards[4].val) and (hand.cards[0].val == hand.cards[1].val):
		hand_confidences[5] += -75
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  214
	if (hand.cards[3].val == hand.cards[2].val) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 1):
		hand_confidences[5] += 35
		hand.genes.append(gene_id)

	# Mutation Resistance: 558.206966691%
	gene_id =  215
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -95
		hand.genes.append(gene_id)

	# Mutation Resistance: 559.353910415%
	gene_id =  216
	if (hand.cards[2].suit != hand.cards[4].suit):
		hand_confidences[5] += -55
		hand.genes.append(gene_id)

	# Mutation Resistance: 127.697547769%
	gene_id =  217
	if (hand.cards[4].val == hand.cards[1].val):
		hand_confidences[5] += -75
		hand.genes.append(gene_id)

	# Mutation Resistance: 558.206966691%
	gene_id =  218
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -80
		hand.genes.append(gene_id)

	# Mutation Resistance: 137.4923716%
	gene_id =  219
	if (hand.cards[2].val != hand.cards[4].val) and (hand.cards[0].val == hand.cards[1].val):
		hand_confidences[5] += -5
		hand.genes.append(gene_id)

	# Mutation Resistance: 558.206966691%
	gene_id =  220
	if (hand.cards[4].suit != hand.cards[0].suit):
		hand_confidences[5] += -45
		hand.genes.append(gene_id)

	# Mutation Resistance: 434.776594029%
	gene_id =  221
	if (hand.cards[1].suit == hand.cards[4].suit):
		hand_confidences[6] += -15
		hand.genes.append(gene_id)

	# Mutation Resistance: 388.232310643%
	gene_id =  222
	if (hand.cards[3].val > 8):
		hand_confidences[6] += -40
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  223
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 2):
		hand_confidences[6] += -100
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  224
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(3) == 1):
		hand_confidences[6] += 70
		hand.genes.append(gene_id)

	# Mutation Resistance: 148.307280953%
	gene_id =  225
	if (hand.cards[3].suit != hand.cards[4].suit) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 1):
		hand_confidences[6] += -35
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  226
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 2):
		hand_confidences[6] += -55
		hand.genes.append(gene_id)

	# Mutation Resistance: 110.997986265%
	gene_id =  227
	if (hand.cards[1].val != hand.cards[0].val) and (hand.cards[2].val < 3):
		hand_confidences[6] += -5
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  228
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(3) == 1):
		hand_confidences[6] += 85
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  229
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 2):
		hand_confidences[6] += -50
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  230
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(3) == 1):
		hand_confidences[6] += 60
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  231
	if ((hand.cards[0].val - hand.cards[2].val) == 7) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 2) and (hand.cards[1].val > 9) and (hand.cards[4].val == hand.cards[3].val):
		hand_confidences[6] += -5
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  232
	if (hand.cards[3].suit == hand.cards[0].suit) and (hand.cards[4].val != hand.cards[3].val) and (hand.cards[2].val > 2) and (hand.cards[4].val == hand.cards[1].val) and (hand.cards[2].suit != hand.cards[3].suit) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 3]) == 3) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1) and (hand.cards[0].suit == hand.cards[1].suit):
		hand_confidences[6] += 50
		hand.genes.append(gene_id)

	# Mutation Resistance: 9.94152046784%
	gene_id =  233
	if (hand.cards[2].suit != hand.cards[0].suit) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(3) == 1) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(3) == 1) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(3) == 1) and (hand.cards[2].suit != hand.cards[4].suit):
		hand_confidences[6] += -100
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  234
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 1) and (hand.cards[2].suit != hand.cards[3].suit) and (hand.cards[3].suit == hand.cards[2].suit):
		hand_confidences[6] += 50
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  235
	if (hand.cards[1].val == hand.cards[2].val) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 6]) == 1) and (hand.cards[1].val < 5) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 0) and (hand.cards[3].val < 8) and ((hand.cards[1].val - hand.cards[2].val) == 8):
		hand_confidences[6] += 80
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  236
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(4) == 1) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 12) and (hand.cards[2].suit != hand.cards[4].suit) and (hand.cards[0].val == hand.cards[2].val) and ((hand.cards[1].val - hand.cards[0].val) == 9):
		hand_confidences[6] += -35
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  237
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0):
		hand_confidences[7] += 50
		hand.genes.append(gene_id)

	# Mutation Resistance: 419.141539791%
	gene_id =  238
	if (hand.cards[2].suit == hand.cards[0].suit):
		hand_confidences[7] += -70
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  239
	if (hand.cards[1].suit != hand.cards[3].suit) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 2) and (hand.cards[3].suit != hand.cards[2].suit) and ((hand.cards[4].val - hand.cards[3].val) == -3):
		hand_confidences[7] += 85
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  240
	if (hand.cards[1].val == hand.cards[2].val) and (hand.cards[1].suit != hand.cards[3].suit) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1):
		hand_confidences[7] += 60
		hand.genes.append(gene_id)

	# Mutation Resistance: 300.0%
	gene_id =  241
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 1):
		hand_confidences[7] += -75
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  242
	if (hand.cards[1].val == hand.cards[2].val) and (hand.cards[1].suit != hand.cards[3].suit) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1):
		hand_confidences[7] += 10
		hand.genes.append(gene_id)

	# Mutation Resistance: 2.65661915519%
	gene_id =  243
	if (hand.cards[0].val != hand.cards[3].val) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 5]) == 1) and (hand.cards[4].val != hand.cards[3].val) and ((hand.cards[4].val - hand.cards[0].val) == 10):
		hand_confidences[7] += -90
		hand.genes.append(gene_id)

	# Mutation Resistance: 200.0%
	gene_id =  244
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 0]) == 2):
		hand_confidences[7] += -55
		hand.genes.append(gene_id)

	# Mutation Resistance: 16.6666666667%
	gene_id =  245
	if ((hand.cards[0].val - hand.cards[4].val) == -10) and (hand.cards[3].val == hand.cards[1].val) and (hand.cards[4].val > 9):
		hand_confidences[7] += 30
		hand.genes.append(gene_id)

	# Mutation Resistance: 9.79612928615%
	gene_id =  246
	if (hand.cards[3].val == hand.cards[1].val) and (hand.cards[3].val != hand.cards[0].val) and (hand.cards[4].suit == hand.cards[2].suit):
		hand_confidences[7] += -55
		hand.genes.append(gene_id)

	# Mutation Resistance: 1.15960475181%
	gene_id =  247
	if (hand.cards[1].suit == hand.cards[3].suit) and (hand.cards[3].val != hand.cards[0].val) and ((hand.cards[2].val - hand.cards[4].val) == 2) and (hand.cards[1].val != hand.cards[4].val) and ((hand.cards[2].val - hand.cards[0].val) == 4) and (hand.cards[4].suit != hand.cards[0].suit) and (hand.cards[1].val != hand.cards[0].val):
		hand_confidences[8] += -90
		hand.genes.append(gene_id)

	# Mutation Resistance: 110.082254686%
	gene_id =  248
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 2):
		hand_confidences[8] += -50
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  249
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(1) == 0) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 1) and (hand.cards[2].val != hand.cards[0].val):
		hand_confidences[8] += 55
		hand.genes.append(gene_id)

	# Mutation Resistance: 83.5287456882%
	gene_id =  250
	if ((hand.cards[2].val - hand.cards[0].val) == -1) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0):
		hand_confidences[8] += -10
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  251
	if ((hand.cards[2].val - hand.cards[0].val) == 4) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 1) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 2) and ((hand.cards[1].val - hand.cards[0].val) == -7) and (hand.cards[4].suit != hand.cards[2].suit):
		hand_confidences[8] += -30
		hand.genes.append(gene_id)

	# Mutation Resistance: 83.5287456882%
	gene_id =  252
	if ((hand.cards[2].val - hand.cards[0].val) == -1) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 0):
		hand_confidences[8] += -65
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  253
	if ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(1) == 0) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(5) == 1) and (hand.cards[2].val != hand.cards[0].val):
		hand_confidences[8] += 25
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  254
	if (hand.cards[3].val < 7) and (hand.cards[3].val < 11) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 3]) == 3) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 5) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 3]) == 3) and (hand.cards[1].suit != hand.cards[0].suit) and (hand.cards[4].val != hand.cards[3].val) and ((hand.cards[1].val - hand.cards[3].val) == -3) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(2) == 1) and (hand.cards[2].val == hand.cards[0].val):
		hand_confidences[8] += -40
		hand.genes.append(gene_id)

	# Mutation Resistance: 1.02169422211%
	gene_id =  255
	if (hand.cards[4].val < 2) and (hand.cards[4].suit != hand.cards[1].suit) and ((hand.cards[1].val - hand.cards[2].val) == 7):
		hand_confidences[8] += -50
		hand.genes.append(gene_id)

	# Mutation Resistance: 159.696127132%
	gene_id =  256
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 3]) == 1):
		hand_confidences[8] += -55
		hand.genes.append(gene_id)

	# Mutation Resistance: 69.7120481393%
	gene_id =  257
	if ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 9):
		hand_confidences[8] += -25
		hand.genes.append(gene_id)

	# Mutation Resistance: 461.973073834%
	gene_id =  258
	if ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(3) == 0) and (hand.cards[4].val < 10):
		hand_confidences[8] += -25
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  259
	if (hand.cards[0].val < 7) and (hand.cards[2].val != hand.cards[0].val) and (hand.cards[1].val != hand.cards[4].val) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0) and ((hand.cards[1].val - hand.cards[2].val) == -8) and (hand.cards[0].val != hand.cards[3].val) and (hand.cards[1].val == hand.cards[4].val):
		hand_confidences[8] += 90
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  260
	if (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 4):
		hand_confidences[8] += 85
		hand.genes.append(gene_id)

	# Mutation Resistance: 560.625166037%
	gene_id =  261
	if (hand.cards[3].suit != hand.cards[2].suit):
		hand_confidences[9] += -65
		hand.genes.append(gene_id)

	# Mutation Resistance: 197.802530981%
	gene_id =  262
	if (hand.cards[0].val > 8) and (hand.cards[4].suit != hand.cards[3].suit):
		hand_confidences[9] += -20
		hand.genes.append(gene_id)

	# Mutation Resistance: 80.6613992761%
	gene_id =  263
	if ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 6):
		hand_confidences[9] += -60
		hand.genes.append(gene_id)

	# Mutation Resistance: 80.6613992761%
	gene_id =  264
	if ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 6):
		hand_confidences[9] += -55
		hand.genes.append(gene_id)

	# Mutation Resistance: 268.779377998%
	gene_id =  265
	if (hand.cards[1].val < 11) and (hand.cards[2].val != hand.cards[4].val) and (hand.cards[3].val < 6):
		hand_confidences[9] += -85
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  266
	if (hand.cards[4].suit == hand.cards[1].suit) and (hand.cards[0].suit == hand.cards[2].suit) and (hand.cards[0].val != hand.cards[3].val) and (hand.cards[1].val > 3):
		hand_confidences[9] += 95
		hand.genes.append(gene_id)

	# Mutation Resistance: 22.8026533997%
	gene_id =  267
	if (hand.cards[0].val < 8) and (hand.cards[1].val == hand.cards[0].val) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(4) == 0) and (hand.cards[4].val != hand.cards[0].val) and (hand.cards[0].suit != hand.cards[3].suit) and (hand.cards[4].val > 10) and (hand.cards[3].val == hand.cards[2].val):
		hand_confidences[9] += -30
		hand.genes.append(gene_id)

	# Mutation Resistance: 197.802530981%
	gene_id =  268
	if (hand.cards[4].suit != hand.cards[3].suit) and (hand.cards[0].val > 8):
		hand_confidences[9] += -40
		hand.genes.append(gene_id)

	# Mutation Resistance: 197.802530981%
	gene_id =  269
	if (hand.cards[4].suit != hand.cards[3].suit) and (hand.cards[0].val > 8):
		hand_confidences[9] += -50
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  270
	if (hand.cards[3].val != hand.cards[2].val) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 6) and ([[card.suit for card in hand.cards].count(i+1) for i in range(13)].count(1) == 3) and (hand.cards[1].val == hand.cards[2].val) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(1) == 4) and (hand.cards[3].suit == hand.cards[1].suit) and (hand.cards[4].suit != hand.cards[2].suit) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 6) and ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 10):
		hand_confidences[9] += -25
		hand.genes.append(gene_id)

	# Mutation Resistance: 191.272142479%
	gene_id =  271
	if (hand.cards[0].val != hand.cards[3].val) and (hand.cards[3].val < 9) and (hand.cards[4].suit == hand.cards[1].suit):
		hand_confidences[9] += -85
		hand.genes.append(gene_id)

	# Mutation Resistance: 80.6613992761%
	gene_id =  272
	if ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 6):
		hand_confidences[9] += -60
		hand.genes.append(gene_id)

	# Mutation Resistance: 100.0%
	gene_id =  273
	if (hand.cards[2].val != hand.cards[1].val) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 1]) == 3):
		hand_confidences[9] += 55
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  274
	if ((max([card.val for card in hand.cards]) - min([card.val for card in hand.cards])) == 5) and (len([i for i in range(len(hand.cards) - 1) if (sorted(hand.cards, key=lambda card: card.val)[i+1].val - sorted(hand.cards, key=lambda card: card.val)[i].val) == 2]) == 2) and (hand.cards[2].suit == hand.cards[0].suit) and (hand.cards[3].val != hand.cards[1].val):
		hand_confidences[9] += 35
		hand.genes.append(gene_id)

	# Mutation Resistance: 268.779377998%
	gene_id =  275
	if (hand.cards[2].val != hand.cards[4].val) and (hand.cards[1].val < 11) and (hand.cards[3].val < 6):
		hand_confidences[9] += -80
		hand.genes.append(gene_id)

	# Mutation Resistance: 0.0%
	gene_id =  276
	if (hand.cards[4].val < 5) and ([[card.val for card in hand.cards].count(i+1) for i in range(13)].count(3) == 1) and ((hand.cards[0].val - hand.cards[4].val) == 12):
		hand_confidences[9] += 45
		hand.genes.append(gene_id)

	# Mutation Resistance: 268.779377998%
	gene_id =  277
	if (hand.cards[2].val != hand.cards[4].val) and (hand.cards[3].val < 6) and (hand.cards[1].val < 11):
		hand_confidences[9] += -80
		hand.genes.append(gene_id)

	# Mutation Resistance: 197.802530981%
	gene_id =  278
	if (hand.cards[4].suit != hand.cards[3].suit) and (hand.cards[0].val > 8):
		hand_confidences[9] += -50
		hand.genes.append(gene_id)

	# Mutation Resistance: 197.802530981%
	gene_id =  279
	if (hand.cards[0].val > 8) and (hand.cards[4].suit != hand.cards[3].suit):
		hand_confidences[9] += -15
		hand.genes.append(gene_id)

	# Mutation Resistance: 211.138192494%
	gene_id =  280
	if (hand.cards[3].suit != hand.cards[2].suit) and (hand.cards[3].val < 11) and (hand.cards[3].val < 6):
		hand_confidences[9] += -55
		hand.genes.append(gene_id)

	# Mutation Resistance: 197.802530981%
	gene_id =  281
	if (hand.cards[0].val > 8) and (hand.cards[4].suit != hand.cards[3].suit):
		hand_confidences[9] += -50
		hand.genes.append(gene_id)

	# Mutation Resistance: 197.802530981%
	gene_id =  282
	if (hand.cards[0].val > 8) and (hand.cards[4].suit != hand.cards[3].suit):
		hand_confidences[9] += -95
	
	if max(hand_confidences) >= 100:
		hand.assigned_class = hand_confidences.index(max(hand_confidences))
	else:
		hand.assigned_class = 0
