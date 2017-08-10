# Fitness: 476.323200266
def classify(hand):
	hand_confidences = [0 for i in range(10)]
	
	# Mutation Resistance: 18.3062515008%
	if (hand.cards[0].suit != hand.cards[4].suit) and (hand.cards[2].suit == hand.cards[1].suit) and (len([card for card in hand.cards if card.val == 12]) != 3) and (hand.cards[3].val != hand.cards[2].val):
		hand_confidences[0] += 70
	
	# Mutation Resistance: 75.9465300568%
	if (hand.cards[2].suit != hand.cards[1].suit):
		hand_confidences[0] += 20
	
	# Mutation Resistance: 72.7607460178%
	if (len([card for card in hand.cards if card.suit == 3]) != 5) and (len([card for card in hand.cards if card.suit == 4]) != 2) and (hand.cards[4].val != hand.cards[0].val):
		hand_confidences[0] += 75
	
	# Mutation Resistance: 61.3195515602%
	if (len([card for card in hand.cards if card.suit == 3]) == 0) and (hand.cards[0].val > 10) and (len([card for card in hand.cards if card.val == 6]) != 4):
		hand_confidences[0] += -25
	
	# Mutation Resistance: 300.258159863%
	if (hand.cards[2].val > 3) and (hand.cards[3].suit == hand.cards[0].suit):
		hand_confidences[0] += -10
	
	# Mutation Resistance: 127.697547769%
	if (hand.cards[4].val == hand.cards[1].val):
		hand_confidences[0] += -100
	
	# Mutation Resistance: 3.15045423951%
	if (hand.cards[4].val == hand.cards[3].val) and ((hand.cards[2].val - hand.cards[0].val) == 4):
		hand_confidences[0] += -40
	
	# Mutation Resistance: 15.1408965006%
	if (len([card for card in hand.cards if card.suit == 2]) != 2) and ((hand.cards[0].val - hand.cards[4].val) == -2) and (hand.cards[3].suit != hand.cards[0].suit) and (hand.cards[1].val < 12):
		hand_confidences[0] += -25
	
	# Mutation Resistance: 98.6072200432%
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
	
	# Mutation Resistance: 72.6317019187%
	if (len([card for card in hand.cards if card.suit == 3]) == 1) and (len([card for card in hand.cards if card.suit == 4]) == 2) and (len([card for card in hand.cards if card.suit == 4]) != 4) and (len([card for card in hand.cards if card.suit == 4]) != 3) and (hand.cards[4].val > 6) and (hand.cards[4].val > 9):
		hand_confidences[0] += -70
	
	# Mutation Resistance: 0.120658149013%
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
	
	# Mutation Resistance: 0.152085167694%
	if (hand.cards[3].suit != hand.cards[4].suit) and (hand.cards[4].suit == hand.cards[1].suit) and (hand.cards[4].val < 6) and ((hand.cards[1].val - hand.cards[3].val) == -8):
		hand_confidences[0] += 60
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val > 8) and (len([card for card in hand.cards if card.suit == 2]) == 2) and (hand.cards[4].val != hand.cards[1].val) and (len([card for card in hand.cards if card.val == 2]) != 1) and ((hand.cards[4].val - hand.cards[0].val) == -10) and ((hand.cards[0].val - hand.cards[2].val) == -8) and (len([card for card in hand.cards if card.suit == 1]) == 2):
		hand_confidences[1] += -20
	
	# Mutation Resistance: 0.568318258225%
	if (len([card for card in hand.cards if card.val == 1]) != 4) and (hand.cards[1].suit == hand.cards[2].suit) and (hand.cards[2].val != hand.cards[4].val) and (len([card for card in hand.cards if card.suit == 1]) == 4) and (hand.cards[1].suit == hand.cards[4].suit):
		hand_confidences[1] += -90
	
	# Mutation Resistance: 370.477475707%
	if (hand.cards[4].suit != hand.cards[1].suit) and (len([card for card in hand.cards if card.val == 11]) != 4) and (hand.cards[3].val != hand.cards[0].val):
		hand_confidences[1] += -15
	
	# Mutation Resistance: 2.76441173696%
	if (hand.cards[4].val > 11) and (hand.cards[1].val != hand.cards[2].val) and (hand.cards[4].suit == hand.cards[2].suit):
		hand_confidences[1] += 25
	
	# Mutation Resistance: 0.0829187396352%
	if (hand.cards[1].val < 11) and (hand.cards[2].val != hand.cards[0].val) and (hand.cards[1].val != hand.cards[0].val) and ((hand.cards[1].val - hand.cards[0].val) == 8) and (len([card for card in hand.cards if card.val == 9]) != 3) and (hand.cards[4].val == hand.cards[3].val) and (len([card for card in hand.cards if card.suit == 2]) != 1) and (hand.cards[3].suit != hand.cards[2].suit):
		hand_confidences[1] += -75
	
	# Mutation Resistance: 89.9613171054%
	if (hand.cards[2].val != hand.cards[1].val):
		hand_confidences[1] += 80
	
	# Mutation Resistance: 871.973466003%
	if (len([card for card in hand.cards if card.val == 13]) != 2):
		hand_confidences[1] += -80
	
	# Mutation Resistance: 69.3839041419%
	if (hand.cards[0].val != hand.cards[4].val) and (hand.cards[3].suit != hand.cards[0].suit):
		hand_confidences[1] += 60
	
	# Mutation Resistance: 69.5348617794%
	if (hand.cards[3].suit != hand.cards[0].suit) and (hand.cards[4].val != hand.cards[1].val):
		hand_confidences[1] += 60
	
	# Mutation Resistance: 69.5159920747%
	if (hand.cards[3].val != hand.cards[1].val) and (hand.cards[3].suit != hand.cards[0].suit):
		hand_confidences[1] += 65
	
	# Mutation Resistance: 4.00037739409%
	if (hand.cards[2].val > 12) and (hand.cards[4].val != hand.cards[2].val) and (hand.cards[3].suit != hand.cards[2].suit) and (hand.cards[0].suit != hand.cards[2].suit):
		hand_confidences[1] += 85
	
	# Mutation Resistance: 4.15995920679%
	if (hand.cards[0].suit == hand.cards[4].suit) and ((hand.cards[2].val - hand.cards[1].val) == -8) and (len([card for card in hand.cards if card.val == 11]) != 2) and (hand.cards[4].val < 11) and (len([card for card in hand.cards if card.val == 12]) == 0):
		hand_confidences[1] += -65
	
	# Mutation Resistance: 0.0%
	if ((hand.cards[1].val - hand.cards[3].val) == 4) and (len([card for card in hand.cards if card.val == 10]) == 3) and (len([card for card in hand.cards if card.val == 5]) != 4) and (len([card for card in hand.cards if card.suit == 2]) != 5) and (len([card for card in hand.cards if card.val == 12]) == 3) and (hand.cards[2].val > 11):
		hand_confidences[1] += -50
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 3]) == 2) and (len([card for card in hand.cards if card.suit == 3]) == 4):
		hand_confidences[1] += -40
	
	# Mutation Resistance: 65.5887230514%
	if (hand.cards[3].val > 1) and (hand.cards[2].val > 2) and (hand.cards[0].val > 1) and (len([card for card in hand.cards if card.val == 10]) != 4) and (hand.cards[1].val > 2):
		hand_confidences[2] += 30
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].suit != hand.cards[3].suit) and (hand.cards[2].val == hand.cards[0].val) and ((hand.cards[4].val - hand.cards[2].val) == 9) and (hand.cards[2].val > 8) and (hand.cards[1].val < 11) and (hand.cards[4].val == hand.cards[2].val):
		hand_confidences[2] += -25
	
	# Mutation Resistance: 77.5290215589%
	if (hand.cards[0].val != hand.cards[4].val):
		hand_confidences[2] += 60
	
	# Mutation Resistance: 870.326603139%
	if (len([card for card in hand.cards if card.val == 2]) != 2) and (len([card for card in hand.cards if card.val == 10]) != 2):
		hand_confidences[2] += -100
	
	# Mutation Resistance: 77.5290215589%
	if (hand.cards[0].val != hand.cards[4].val):
		hand_confidences[2] += 5
	
	# Mutation Resistance: 78.3582089552%
	if (hand.cards[1].val != hand.cards[2].val) and (hand.cards[1].val != hand.cards[2].val):
		hand_confidences[2] += 10
	
	# Mutation Resistance: 868.604480507%
	if (len([card for card in hand.cards if card.val == 4]) != 2) and (len([card for card in hand.cards if card.val == 11]) != 3):
		hand_confidences[2] += -95
	
	# Mutation Resistance: 0.0%
	if ((hand.cards[2].val - hand.cards[4].val) == 12) and (hand.cards[0].val < 2) and (len([card for card in hand.cards if card.val == 2]) == 2) and ((hand.cards[2].val - hand.cards[1].val) == 9) and ((hand.cards[4].val - hand.cards[1].val) == -7) and (hand.cards[4].val == hand.cards[1].val):
		hand_confidences[2] += 40
	
	# Mutation Resistance: 479.198963715%
	if (hand.cards[2].suit != hand.cards[3].suit):
		hand_confidences[2] += -10
	
	# Mutation Resistance: 873.453470453%
	if (len([card for card in hand.cards if card.val == 3]) != 2) and (len([card for card in hand.cards if card.val == 12]) != 2):
		hand_confidences[2] += -30
	
	# Mutation Resistance: 876.618077177%
	if (len([card for card in hand.cards if card.val == 12]) != 2) and (len([card for card in hand.cards if card.val == 7]) != 2):
		hand_confidences[2] += -80
	
	# Mutation Resistance: 92.6202321725%
	if (len([card for card in hand.cards if card.val == 12]) != 1) and (len([card for card in hand.cards if card.suit == 3]) != 4):
		hand_confidences[2] += 65
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].val != hand.cards[0].val) and (hand.cards[0].suit != hand.cards[1].suit) and (hand.cards[0].val != hand.cards[2].val) and (len([card for card in hand.cards if card.val == 7]) != 0) and (hand.cards[2].val != hand.cards[3].val) and ((hand.cards[3].val - hand.cards[1].val) == 11) and (len([card for card in hand.cards if card.suit == 1]) == 4) and (len([card for card in hand.cards if card.suit == 3]) != 4) and (hand.cards[1].val < 8) and (hand.cards[2].val < 6) and (hand.cards[3].suit != hand.cards[1].suit) and (hand.cards[3].val != hand.cards[4].val):
		hand_confidences[2] += -5
	
	# Mutation Resistance: 78.3582089552%
	if (hand.cards[1].val != hand.cards[2].val) and (hand.cards[1].val != hand.cards[2].val):
		hand_confidences[2] += 40
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].val == hand.cards[3].val) and (len([card for card in hand.cards if card.suit == 4]) == 0) and (hand.cards[1].val < 3) and (len([card for card in hand.cards if card.suit == 1]) == 3) and (hand.cards[3].suit == hand.cards[4].suit) and (len([card for card in hand.cards if card.val == 8]) == 2) and (len([card for card in hand.cards if card.suit == 2]) != 0):
		hand_confidences[2] += 90
	
	# Mutation Resistance: 77.5290215589%
	if (hand.cards[0].val != hand.cards[4].val):
		hand_confidences[2] += 90
	
	# Mutation Resistance: 862.672579174%
	if (len([card for card in hand.cards if card.val == 3]) != 2) and (len([card for card in hand.cards if card.val == 6]) != 2):
		hand_confidences[2] += -5
	
	# Mutation Resistance: 77.5290215589%
	if (hand.cards[0].val != hand.cards[4].val):
		hand_confidences[2] += 30
	
	# Mutation Resistance: 77.5290215589%
	if (hand.cards[0].val != hand.cards[4].val):
		hand_confidences[2] += 70
	
	# Mutation Resistance: 0.0%
	if ((hand.cards[0].val - hand.cards[4].val) == -12) and (hand.cards[0].val == hand.cards[3].val) and (len([card for card in hand.cards if card.suit == 4]) != 5) and (hand.cards[2].val != hand.cards[4].val) and (hand.cards[0].val > 2):
		hand_confidences[2] += 25
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val > 10) and (len([card for card in hand.cards if card.suit == 2]) == 2) and (len([card for card in hand.cards if card.val == 3]) == 3) and (len([card for card in hand.cards if card.val == 7]) == 4):
		hand_confidences[2] += -15
	
	# Mutation Resistance: 18.0311890838%
	if (len([card for card in hand.cards if card.suit == 4]) == 1) and (hand.cards[3].val > 9) and (hand.cards[2].val == hand.cards[0].val) and (hand.cards[2].val == hand.cards[4].val) and (hand.cards[0].suit != hand.cards[3].suit):
		hand_confidences[2] += -80
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val < 6) and (hand.cards[1].val != hand.cards[4].val) and (len([card for card in hand.cards if card.val == 10]) == 2) and (hand.cards[3].val > 5) and (len([card for card in hand.cards if card.suit == 4]) == 4) and (len([card for card in hand.cards if card.val == 1]) == 1) and (hand.cards[4].suit != hand.cards[0].suit) and (hand.cards[0].val == hand.cards[1].val) and (hand.cards[1].suit == hand.cards[2].suit):
		hand_confidences[2] += 90
	
	# Mutation Resistance: 0.663349917081%
	if (hand.cards[3].val < 6) and (hand.cards[1].val == hand.cards[3].val) and (len([card for card in hand.cards if card.suit == 4]) != 2) and (hand.cards[0].suit == hand.cards[4].suit) and (len([card for card in hand.cards if card.suit == 1]) != 1):
		hand_confidences[2] += 10
	
	# Mutation Resistance: 74.269005848%
	if (hand.cards[3].val != hand.cards[1].val) and (len([card for card in hand.cards if card.suit == 2]) != 5):
		hand_confidences[3] += 65
	
	# Mutation Resistance: 74.269005848%
	if (len([card for card in hand.cards if card.suit == 4]) != 5) and (hand.cards[3].val != hand.cards[1].val):
		hand_confidences[3] += 35
	
	# Mutation Resistance: 74.269005848%
	if (len([card for card in hand.cards if card.suit == 4]) != 5) and (hand.cards[3].val != hand.cards[1].val):
		hand_confidences[3] += 50
	
	# Mutation Resistance: 71.1500974659%
	if (len([card for card in hand.cards if card.suit == 2]) != 3) and (hand.cards[3].val != hand.cards[1].val):
		hand_confidences[3] += 5
	
	# Mutation Resistance: 731.854079917%
	if (hand.cards[4].val != hand.cards[3].val) and (hand.cards[4].val != hand.cards[0].val):
		hand_confidences[3] += -95
	
	# Mutation Resistance: 744.278736049%
	if (hand.cards[4].val != hand.cards[2].val) and (hand.cards[4].val != hand.cards[1].val):
		hand_confidences[3] += -5
	
	# Mutation Resistance: 74.269005848%
	if (hand.cards[3].val != hand.cards[1].val) and (len([card for card in hand.cards if card.suit == 3]) != 5):
		hand_confidences[3] += 20
	
	# Mutation Resistance: 688.285081809%
	if (hand.cards[0].val != hand.cards[1].val) and (hand.cards[4].val != hand.cards[2].val):
		hand_confidences[3] += -35
	
	# Mutation Resistance: 100.0%
	if (len([card for card in hand.cards if card.suit == 3]) != 4):
		hand_confidences[3] += 30
	
	# Mutation Resistance: 671.80058759%
	if (hand.cards[4].val != hand.cards[2].val) and (hand.cards[0].val != hand.cards[2].val):
		hand_confidences[3] += -90
	
	# Mutation Resistance: 74.269005848%
	if (len([card for card in hand.cards if card.suit == 3]) != 5) and (hand.cards[3].val != hand.cards[1].val):
		hand_confidences[3] += 35
	
	# Mutation Resistance: 749.554121083%
	if (hand.cards[0].val != hand.cards[1].val) and (hand.cards[1].val != hand.cards[0].val):
		hand_confidences[3] += -25
	
	# Mutation Resistance: 74.269005848%
	if (hand.cards[3].val != hand.cards[1].val) and (len([card for card in hand.cards if card.suit == 4]) != 5):
		hand_confidences[3] += 5
	
	# Mutation Resistance: 74.269005848%
	if (len([card for card in hand.cards if card.suit == 3]) != 5) and (hand.cards[3].val != hand.cards[1].val):
		hand_confidences[3] += 65
	
	# Mutation Resistance: 691.740279638%
	if (hand.cards[3].val != hand.cards[1].val) and (hand.cards[0].val != hand.cards[2].val):
		hand_confidences[3] += -70
	
	# Mutation Resistance: 74.269005848%
	if (hand.cards[3].val != hand.cards[1].val) and (len([card for card in hand.cards if card.suit == 1]) != 5):
		hand_confidences[3] += 75
	
	# Mutation Resistance: 688.429244944%
	if (hand.cards[4].val != hand.cards[1].val) and (hand.cards[0].val != hand.cards[3].val):
		hand_confidences[3] += -85
	
	# Mutation Resistance: 683.886668648%
	if (hand.cards[0].val != hand.cards[1].val) and (hand.cards[0].val != hand.cards[3].val):
		hand_confidences[3] += -85
	
	# Mutation Resistance: 74.269005848%
	if (hand.cards[3].val != hand.cards[1].val) and (len([card for card in hand.cards if card.suit == 4]) != 5):
		hand_confidences[3] += 70
	
	# Mutation Resistance: 100.0%
	if (len([card for card in hand.cards if card.suit == 3]) != 4):
		hand_confidences[3] += 55
	
	# Mutation Resistance: 677.551152765%
	if (len([card for card in hand.cards if card.suit == 1]) != 4) and (hand.cards[4].val != hand.cards[3].val) and (hand.cards[3].val != hand.cards[0].val):
		hand_confidences[3] += -20
	
	# Mutation Resistance: 752.368828562%
	if (hand.cards[3].val != hand.cards[1].val) and (hand.cards[1].val != hand.cards[3].val):
		hand_confidences[3] += -95
	
	# Mutation Resistance: 680.866764864%
	if (hand.cards[4].val != hand.cards[3].val) and (hand.cards[3].val != hand.cards[1].val):
		hand_confidences[3] += -75
	
	# Mutation Resistance: 688.285081809%
	if (hand.cards[4].val != hand.cards[2].val) and (hand.cards[1].val != hand.cards[0].val):
		hand_confidences[3] += -100
	
	# Mutation Resistance: 74.269005848%
	if (len([card for card in hand.cards if card.suit == 3]) != 5) and (hand.cards[3].val != hand.cards[1].val):
		hand_confidences[3] += 70
	
	# Mutation Resistance: 731.854079917%
	if (hand.cards[4].val != hand.cards[0].val) and (hand.cards[4].val != hand.cards[3].val):
		hand_confidences[3] += -5
	
	# Mutation Resistance: 3.54690600212%
	if (len([card for card in hand.cards if card.val == 9]) != 4) and (hand.cards[3].val == hand.cards[1].val) and (len([card for card in hand.cards if card.suit == 2]) != 1) and (len([card for card in hand.cards if card.val == 10]) == 2) and (len([card for card in hand.cards if card.suit == 2]) == 2) and (len([card for card in hand.cards if card.suit == 1]) != 0):
		hand_confidences[3] += -70
	
	# Mutation Resistance: 100.0%
	if (len([card for card in hand.cards if card.suit == 3]) != 4):
		hand_confidences[3] += 10
	
	# Mutation Resistance: 681.756551238%
	if (hand.cards[1].val != hand.cards[2].val) and (hand.cards[0].val != hand.cards[3].val):
		hand_confidences[3] += -65
	
	# Mutation Resistance: 681.811435323%
	if (hand.cards[0].val != hand.cards[3].val) and (hand.cards[4].val != hand.cards[2].val):
		hand_confidences[3] += -15
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].val == hand.cards[4].val) and (hand.cards[3].val < 4) and (len([card for card in hand.cards if card.suit == 3]) != 2) and (hand.cards[4].suit != hand.cards[0].suit) and (hand.cards[4].suit != hand.cards[1].suit) and (hand.cards[3].val != hand.cards[1].val) and (hand.cards[1].val > 12) and (len([card for card in hand.cards if card.val == 2]) != 0) and (hand.cards[0].val == hand.cards[3].val) and (hand.cards[3].val == hand.cards[4].val) and (len([card for card in hand.cards if card.val == 5]) == 1) and (hand.cards[4].suit == hand.cards[1].suit) and ((hand.cards[1].val - hand.cards[2].val) == -4) and ((hand.cards[2].val - hand.cards[1].val) == 3) and (len([card for card in hand.cards if card.suit == 3]) == 1):
		hand_confidences[3] += 85
	
	# Mutation Resistance: 2.13137818227%
	if (hand.cards[1].suit == hand.cards[3].suit) and (len([card for card in hand.cards if card.suit == 3]) != 4) and (len([card for card in hand.cards if card.suit == 2]) != 1) and ((hand.cards[0].val - hand.cards[2].val) == -1) and (len([card for card in hand.cards if card.suit == 3]) == 1):
		hand_confidences[3] += -85
	
	# Mutation Resistance: 11.1111111111%
	if (hand.cards[4].val > 4) and (hand.cards[2].suit != hand.cards[1].suit) and (hand.cards[2].val > 2) and (hand.cards[3].suit == hand.cards[0].suit) and (hand.cards[3].suit != hand.cards[2].suit):
		hand_confidences[3] += 85
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].suit == hand.cards[1].suit) and (hand.cards[3].val != hand.cards[2].val) and (len([card for card in hand.cards if card.val == 3]) != 4) and (hand.cards[3].val < 6) and (len([card for card in hand.cards if card.suit == 4]) != 0) and (hand.cards[0].suit == hand.cards[1].suit) and (len([card for card in hand.cards if card.suit == 4]) != 2) and ((hand.cards[2].val - hand.cards[1].val) == -2) and (hand.cards[4].val != hand.cards[3].val) and (len([card for card in hand.cards if card.val == 8]) != 0):
		hand_confidences[3] += 15
	
	# Mutation Resistance: 6.87134502924%
	if (len([card for card in hand.cards if card.val == 9]) == 3) and (hand.cards[3].val != hand.cards[4].val):
		hand_confidences[4] += -15
	
	# Mutation Resistance: 0.0%
	if (hand.cards[2].suit == hand.cards[3].suit) and ((hand.cards[0].val - hand.cards[2].val) == 3) and (hand.cards[4].val == hand.cards[0].val) and (hand.cards[2].val > 9) and (hand.cards[3].val > 5) and (len([card for card in hand.cards if card.suit == 3]) != 1) and (len([card for card in hand.cards if card.suit == 2]) != 3) and (hand.cards[1].val == hand.cards[4].val) and ((hand.cards[0].val - hand.cards[2].val) == 6):
		hand_confidences[4] += -75
	
	# Mutation Resistance: 151.86659108%
	if (hand.cards[0].val < 4) and (len([card for card in hand.cards if card.val == 5]) == 0):
		hand_confidences[4] += -70
	
	# Mutation Resistance: 0.722100089372%
	if (len([card for card in hand.cards if card.val == 10]) != 0) and (len([card for card in hand.cards if card.suit == 1]) != 4) and (hand.cards[4].suit == hand.cards[1].suit) and (hand.cards[2].val > 1) and (hand.cards[4].val != hand.cards[3].val) and (hand.cards[2].suit != hand.cards[4].suit) and (hand.cards[1].val < 5) and (hand.cards[4].val < 5):
		hand_confidences[4] += -95
	
	# Mutation Resistance: 80.6451612903%
	if (hand.cards[3].val != hand.cards[0].val) and (hand.cards[1].val > 1) and (hand.cards[1].suit != hand.cards[4].suit):
		hand_confidences[4] += 10
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].val != hand.cards[4].val) and (hand.cards[0].val < 3) and (hand.cards[0].val > 2) and (hand.cards[2].suit != hand.cards[3].suit):
		hand_confidences[4] += -95
	
	# Mutation Resistance: 37.134502924%
	if (hand.cards[2].val == hand.cards[4].val) and (hand.cards[2].val == hand.cards[0].val) and (len([card for card in hand.cards if card.suit == 2]) != 0):
		hand_confidences[4] += -75
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 13]) == 0) and (len([card for card in hand.cards if card.val == 13]) != 4) and (len([card for card in hand.cards if card.suit == 2]) == 0) and (len([card for card in hand.cards if card.val == 6]) == 1) and (len([card for card in hand.cards if card.val == 3]) != 0) and ((hand.cards[1].val - hand.cards[2].val) == -4) and (hand.cards[2].suit != hand.cards[0].suit):
		hand_confidences[4] += 25
	
	# Mutation Resistance: 36.5591397849%
	if (hand.cards[4].suit != hand.cards[1].suit) and (len([card for card in hand.cards if card.val == 4]) == 1):
		hand_confidences[4] += 70
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 8]) != 2) and (hand.cards[0].val == hand.cards[4].val) and ((hand.cards[1].val - hand.cards[3].val) == -8):
		hand_confidences[4] += 10
	
	# Mutation Resistance: 47.311827957%
	if (len([card for card in hand.cards if card.val == 11]) == 1):
		hand_confidences[4] += 20
	
	# Mutation Resistance: 79.5698924731%
	if (hand.cards[2].suit != hand.cards[3].suit) and (len([card for card in hand.cards if card.suit == 2]) != 5):
		hand_confidences[4] += 35
	
	# Mutation Resistance: 121.643856386%
	if (hand.cards[4].val == hand.cards[0].val):
		hand_confidences[4] += -80
	
	# Mutation Resistance: 47.311827957%
	if (len([card for card in hand.cards if card.val == 11]) == 1):
		hand_confidences[4] += 80
	
	# Mutation Resistance: 39.7849462366%
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
	
	# Mutation Resistance: 75.2688172043%
	if (hand.cards[1].suit != hand.cards[0].suit):
		hand_confidences[4] += 5
	
	# Mutation Resistance: 862.844413183%
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
	
	# Mutation Resistance: 559.667850415%
	if (hand.cards[1].suit != hand.cards[4].suit):
		hand_confidences[5] += -55
	
	# Mutation Resistance: 100.0%
	if (hand.cards[0].val != hand.cards[3].val) and (hand.cards[0].suit == hand.cards[2].suit) and (len([card for card in hand.cards if card.suit == 4]) != 3) and (len([card for card in hand.cards if card.suit == 1]) != 2):
		hand_confidences[5] += 45
	
	# Mutation Resistance: 563.80125216%
	if (hand.cards[0].suit != hand.cards[1].suit):
		hand_confidences[5] += -80
	
	# Mutation Resistance: 6.17114641537%
	if (len([card for card in hand.cards if card.suit == 4]) != 2) and ((hand.cards[3].val - hand.cards[1].val) == -3) and (hand.cards[3].suit == hand.cards[2].suit):
		hand_confidences[5] += -50
	
	# Mutation Resistance: 583.472635149%
	if (hand.cards[2].suit != hand.cards[1].suit):
		hand_confidences[5] += -90
	
	# Mutation Resistance: 100.0%
	if (len([card for card in hand.cards if card.val == 6]) != 2):
		hand_confidences[5] += 40
	
	# Mutation Resistance: 752.951743577%
	if (len([card for card in hand.cards if card.val == 7]) != 1):
		hand_confidences[5] += -100
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 13]) == 4) and (len([card for card in hand.cards if card.val == 10]) == 1) and (hand.cards[1].val == hand.cards[0].val) and (len([card for card in hand.cards if card.val == 3]) != 0):
		hand_confidences[5] += -95
	
	# Mutation Resistance: 12.9243074086%
	if (hand.cards[2].val == hand.cards[1].val) and (hand.cards[3].val != hand.cards[0].val) and (len([card for card in hand.cards if card.val == 2]) != 1) and (hand.cards[1].val > 1) and (len([card for card in hand.cards if card.suit == 3]) == 1) and (len([card for card in hand.cards if card.suit == 2]) != 5) and (len([card for card in hand.cards if card.suit == 1]) == 1):
		hand_confidences[5] += -25
	
	# Mutation Resistance: 90.7407407407%
	if (hand.cards[0].val > 1) and (hand.cards[3].val != hand.cards[4].val) and (hand.cards[2].suit == hand.cards[3].suit):
		hand_confidences[5] += 25
	
	# Mutation Resistance: 90.7407407407%
	if (hand.cards[2].suit == hand.cards[3].suit) and (hand.cards[3].val != hand.cards[4].val) and (hand.cards[0].val > 1):
		hand_confidences[5] += 55
	
	# Mutation Resistance: 100.0%
	if (len([card for card in hand.cards if card.val == 6]) != 2):
		hand_confidences[5] += 15
	
	# Mutation Resistance: 9.25925925926%
	if (len([card for card in hand.cards if card.val == 12]) == 1) and (len([card for card in hand.cards if card.suit == 1]) != 0):
		hand_confidences[5] += 70
	
	# Mutation Resistance: 100.0%
	if (hand.cards[4].suit == hand.cards[0].suit):
		hand_confidences[5] += 45
	
	# Mutation Resistance: 583.472635149%
	if (hand.cards[1].suit != hand.cards[2].suit):
		hand_confidences[5] += -95
	
	# Mutation Resistance: 90.7407407407%
	if (hand.cards[0].val > 1) and (hand.cards[2].suit == hand.cards[3].suit) and (hand.cards[3].val != hand.cards[4].val):
		hand_confidences[5] += 100
	
	# Mutation Resistance: 580.858460209%
	if (hand.cards[0].suit != hand.cards[2].suit):
		hand_confidences[5] += -95
	
	# Mutation Resistance: 580.858460209%
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
	
	# Mutation Resistance: 100.0%
	if (len([card for card in hand.cards if card.val == 12]) != 1):
		hand_confidences[6] += 35
	
	# Mutation Resistance: 805.635785564%
	if (hand.cards[4].val != hand.cards[1].val):
		hand_confidences[6] += -5
	
	# Mutation Resistance: 94.4444444444%
	if (hand.cards[4].suit != hand.cards[1].suit) and (hand.cards[1].suit != hand.cards[4].suit):
		hand_confidences[6] += 100
	
	# Mutation Resistance: 44.4444444444%
	if (hand.cards[3].val == hand.cards[0].val):
		hand_confidences[6] += 75
	
	# Mutation Resistance: 100.0%
	if (len([card for card in hand.cards if card.val == 12]) != 1):
		hand_confidences[6] += 35
	
	# Mutation Resistance: 817.245032503%
	if (hand.cards[4].val != hand.cards[0].val):
		hand_confidences[6] += -70
	
	# Mutation Resistance: 821.72405716%
	if (hand.cards[4].val != hand.cards[3].val):
		hand_confidences[6] += -75
	
	# Mutation Resistance: 16.6666666667%
	if (len([card for card in hand.cards if card.suit == 3]) != 0) and (len([card for card in hand.cards if card.val == 12]) != 1) and (len([card for card in hand.cards if card.val == 11]) != 0) and (hand.cards[4].suit != hand.cards[2].suit):
		hand_confidences[6] += 60
	
	# Mutation Resistance: 821.72405716%
	if (hand.cards[4].val != hand.cards[3].val):
		hand_confidences[6] += -75
	
	# Mutation Resistance: 100.0%
	if (len([card for card in hand.cards if card.val == 12]) != 1):
		hand_confidences[6] += 45
	
	# Mutation Resistance: 821.72405716%
	if (hand.cards[4].val != hand.cards[3].val):
		hand_confidences[6] += -80
	
	# Mutation Resistance: 805.635785564%
	if (hand.cards[4].val != hand.cards[1].val):
		hand_confidences[6] += -90
	
	# Mutation Resistance: 821.72405716%
	if (hand.cards[4].val != hand.cards[3].val):
		hand_confidences[6] += -45
	
	# Mutation Resistance: 77.7777777778%
	if (hand.cards[3].suit != hand.cards[2].suit) and (len([card for card in hand.cards if card.suit == 3]) != 0) and (len([card for card in hand.cards if card.val == 11]) != 1) and (len([card for card in hand.cards if card.val == 7]) != 1):
		hand_confidences[6] += 95
	
	# Mutation Resistance: 756.456161087%
	if (hand.cards[3].val != hand.cards[2].val):
		hand_confidences[6] += -15
	
	# Mutation Resistance: 805.650747756%
	if (hand.cards[4].val != hand.cards[2].val):
		hand_confidences[6] += -80
	
	# Mutation Resistance: 805.635785564%
	if (hand.cards[4].val != hand.cards[1].val):
		hand_confidences[6] += -60
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 4]) != 0) and (hand.cards[0].val == hand.cards[3].val) and (hand.cards[4].suit != hand.cards[2].suit) and (hand.cards[1].val < 4) and (hand.cards[1].val > 6) and (len([card for card in hand.cards if card.suit == 2]) != 4) and ((hand.cards[1].val - hand.cards[4].val) == -9):
		hand_confidences[6] += 50
	
	# Mutation Resistance: 94.4444444444%
	if (hand.cards[4].suit != hand.cards[1].suit) and (hand.cards[1].suit != hand.cards[4].suit):
		hand_confidences[6] += 85
	
	# Mutation Resistance: 821.72405716%
	if (hand.cards[4].val != hand.cards[3].val):
		hand_confidences[6] += -40
	
	# Mutation Resistance: 77.7777777778%
	if (len([card for card in hand.cards if card.val == 11]) != 1) and (len([card for card in hand.cards if card.suit == 3]) != 0) and (hand.cards[3].suit != hand.cards[2].suit) and (len([card for card in hand.cards if card.val == 7]) != 1):
		hand_confidences[6] += 55
	
	# Mutation Resistance: 821.72405716%
	if (hand.cards[4].val != hand.cards[3].val):
		hand_confidences[6] += -5
	
	# Mutation Resistance: 94.4444444444%
	if (hand.cards[1].suit != hand.cards[4].suit) and (hand.cards[4].suit != hand.cards[1].suit):
		hand_confidences[6] += 95
	
	# Mutation Resistance: 100.0%
	if (len([card for card in hand.cards if card.val == 12]) != 4):
		hand_confidences[6] += 60
	
	# Mutation Resistance: 30.5555555556%
	if (hand.cards[2].val == hand.cards[3].val):
		hand_confidences[6] += 60
	
	# Mutation Resistance: 805.650747756%
	if (hand.cards[4].val != hand.cards[2].val):
		hand_confidences[6] += -90
	
	# Mutation Resistance: 86.1111111111%
	if (len([card for card in hand.cards if card.val == 3]) == 0):
		hand_confidences[6] += 15
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val != hand.cards[0].val) and (len([card for card in hand.cards if card.val == 6]) == 2) and (hand.cards[1].val > 9) and ((hand.cards[1].val - hand.cards[0].val) == 3):
		hand_confidences[6] += 5
	
	# Mutation Resistance: 75.0%
	if (len([card for card in hand.cards if card.suit == 3]) != 0) and (hand.cards[0].suit != hand.cards[2].suit) and (len([card for card in hand.cards if card.val == 11]) != 1) and (len([card for card in hand.cards if card.val == 7]) != 1):
		hand_confidences[6] += 90
	
	# Mutation Resistance: 817.245032503%
	if (hand.cards[4].val != hand.cards[0].val):
		hand_confidences[6] += -25
	
	# Mutation Resistance: 199.579068246%
	if (len([card for card in hand.cards if card.suit == 4]) == 2):
		hand_confidences[6] += -15
	
	# Mutation Resistance: 817.245032503%
	if (hand.cards[4].val != hand.cards[0].val):
		hand_confidences[6] += -90
	
	# Mutation Resistance: 821.72405716%
	if (hand.cards[4].val != hand.cards[3].val):
		hand_confidences[6] += -55
	
	# Mutation Resistance: 100.0%
	if (len([card for card in hand.cards if card.val == 12]) != 1):
		hand_confidences[6] += 80
	
	# Mutation Resistance: 805.635785564%
	if (hand.cards[4].val != hand.cards[1].val):
		hand_confidences[6] += -60
	
	# Mutation Resistance: 759.398175663%
	if (hand.cards[0].val != hand.cards[1].val):
		hand_confidences[6] += -85
	
	# Mutation Resistance: 94.4444444444%
	if (hand.cards[1].suit != hand.cards[4].suit) and (hand.cards[4].suit != hand.cards[1].suit):
		hand_confidences[6] += 10
	
	# Mutation Resistance: 821.72405716%
	if (hand.cards[4].val != hand.cards[3].val):
		hand_confidences[6] += -75
	
	# Mutation Resistance: 11.7681743932%
	if (len([card for card in hand.cards if card.val == 12]) == 1) and (len([card for card in hand.cards if card.val == 4]) != 2) and (hand.cards[4].suit == hand.cards[3].suit) and (hand.cards[0].val < 8) and (hand.cards[0].val > 5):
		hand_confidences[6] += -60
	
	# Mutation Resistance: 817.245032503%
	if (hand.cards[4].val != hand.cards[0].val):
		hand_confidences[6] += -85
	
	# Mutation Resistance: 100.0%
	if (len([card for card in hand.cards if card.val == 12]) != 1):
		hand_confidences[6] += 35
	
	# Mutation Resistance: 12.2341871171%
	if (hand.cards[2].val != hand.cards[0].val) and (len([card for card in hand.cards if card.suit == 4]) != 3) and (hand.cards[3].val < 8) and (hand.cards[2].val != hand.cards[0].val) and (len([card for card in hand.cards if card.val == 4]) == 2) and (len([card for card in hand.cards if card.val == 11]) != 3):
		hand_confidences[6] += -65
	
	# Mutation Resistance: 100.0%
	if (len([card for card in hand.cards if card.val == 12]) != 1):
		hand_confidences[6] += 75
	
	# Mutation Resistance: 77.7777777778%
	if (len([card for card in hand.cards if card.suit == 3]) != 0) and (len([card for card in hand.cards if card.val == 11]) != 1) and (len([card for card in hand.cards if card.val == 7]) != 1) and (hand.cards[3].suit != hand.cards[2].suit):
		hand_confidences[6] += 95
	
	# Mutation Resistance: 100.0%
	if (len([card for card in hand.cards if card.val == 12]) != 1):
		hand_confidences[6] += 35
	
	# Mutation Resistance: 803.842620108%
	if (hand.cards[0].val != hand.cards[1].val):
		hand_confidences[7] += -55
	
	# Mutation Resistance: 809.233938864%
	if (hand.cards[2].val != hand.cards[3].val):
		hand_confidences[7] += -50
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 1]) == 5) and (hand.cards[3].suit == hand.cards[1].suit) and ((hand.cards[2].val - hand.cards[0].val) == 1) and (hand.cards[4].suit == hand.cards[3].suit) and (hand.cards[3].val != hand.cards[2].val) and (hand.cards[4].suit == hand.cards[2].suit) and (hand.cards[2].suit != hand.cards[1].suit) and (len([card for card in hand.cards if card.suit == 3]) != 1) and (hand.cards[0].val == hand.cards[1].val) and (hand.cards[0].suit != hand.cards[2].suit) and (hand.cards[1].val > 4) and (hand.cards[2].suit != hand.cards[0].suit) and (hand.cards[4].val == hand.cards[0].val) and (hand.cards[4].val == hand.cards[3].val) and (hand.cards[1].val == hand.cards[0].val):
		hand_confidences[7] += 90
	
	# Mutation Resistance: 16.6666666667%
	if (len([card for card in hand.cards if card.val == 4]) != 4) and (hand.cards[1].val == hand.cards[4].val) and (len([card for card in hand.cards if card.val == 4]) != 1) and (hand.cards[2].suit != hand.cards[1].suit) and (hand.cards[2].val == hand.cards[3].val):
		hand_confidences[7] += 75
	
	# Mutation Resistance: 791.662605983%
	if (hand.cards[2].val != hand.cards[1].val):
		hand_confidences[7] += -75
	
	# Mutation Resistance: 100.0%
	if (hand.cards[0].suit != hand.cards[2].suit):
		hand_confidences[7] += 60
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].suit == hand.cards[4].suit) and (len([card for card in hand.cards if card.val == 12]) != 4) and (hand.cards[1].suit != hand.cards[0].suit) and (len([card for card in hand.cards if card.val == 1]) == 4) and (hand.cards[3].suit != hand.cards[0].suit) and (len([card for card in hand.cards if card.val == 5]) == 2) and (hand.cards[3].suit != hand.cards[1].suit):
		hand_confidences[7] += -85
	
	# Mutation Resistance: 116.441359823%
	if (len([card for card in hand.cards if card.suit == 2]) != 1) and (hand.cards[4].val < 5) and (hand.cards[3].suit == hand.cards[2].suit):
		hand_confidences[7] += -10
	
	# Mutation Resistance: 797.317414423%
	if (hand.cards[2].val != hand.cards[4].val):
		hand_confidences[7] += -90
	
	# Mutation Resistance: 791.662605983%
	if (hand.cards[2].val != hand.cards[1].val):
		hand_confidences[7] += -95
	
	# Mutation Resistance: 0.0%
	if (hand.cards[3].val < 5) and ((hand.cards[1].val - hand.cards[0].val) == 1) and (len([card for card in hand.cards if card.val == 3]) == 2) and (hand.cards[2].val < 8) and (len([card for card in hand.cards if card.suit == 1]) == 3) and (len([card for card in hand.cards if card.val == 13]) == 0) and (hand.cards[4].val == hand.cards[0].val) and (hand.cards[4].suit != hand.cards[0].suit) and (hand.cards[4].val == hand.cards[1].val) and (len([card for card in hand.cards if card.val == 8]) == 0) and (len([card for card in hand.cards if card.suit == 2]) == 3) and (hand.cards[1].suit != hand.cards[2].suit) and (len([card for card in hand.cards if card.suit == 1]) == 5):
		hand_confidences[7] += -15
	
	# Mutation Resistance: 66.6666666667%
	if (hand.cards[4].suit != hand.cards[0].suit) and (hand.cards[3].val > 4):
		hand_confidences[7] += 60
	
	# Mutation Resistance: 50.0%
	if (hand.cards[1].val != hand.cards[4].val) and (len([card for card in hand.cards if card.suit == 2]) != 2) and (len([card for card in hand.cards if card.val == 5]) != 4) and (hand.cards[1].val < 12):
		hand_confidences[7] += 40
	
	# Mutation Resistance: 638.900788673%
	if (hand.cards[0].val < 13) and (hand.cards[4].val > 3):
		hand_confidences[7] += -10
	
	# Mutation Resistance: 83.3333333333%
	if (hand.cards[0].val == hand.cards[1].val) and (len([card for card in hand.cards if card.suit == 3]) != 2) and (len([card for card in hand.cards if card.val == 2]) != 1):
		hand_confidences[7] += 25
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 9]) == 1) and (hand.cards[2].val == hand.cards[0].val) and (hand.cards[3].val != hand.cards[0].val) and ((hand.cards[0].val - hand.cards[1].val) == -9) and (len([card for card in hand.cards if card.val == 13]) == 4) and (hand.cards[1].suit != hand.cards[4].suit) and (len([card for card in hand.cards if card.val == 2]) == 0) and (len([card for card in hand.cards if card.suit == 1]) == 2) and (hand.cards[3].val > 8) and ((hand.cards[2].val - hand.cards[0].val) == -11):
		hand_confidences[7] += 70
	
	# Mutation Resistance: 83.3333333333%
	if (len([card for card in hand.cards if card.suit == 2]) == 1) and (hand.cards[2].suit != hand.cards[0].suit):
		hand_confidences[7] += 85
	
	# Mutation Resistance: 83.3333333333%
	if (len([card for card in hand.cards if card.suit == 3]) != 2) and (len([card for card in hand.cards if card.val == 1]) != 1) and (hand.cards[0].val == hand.cards[1].val):
		hand_confidences[7] += 70
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].val == hand.cards[2].val) and (hand.cards[1].val < 13) and (hand.cards[1].val > 9) and (hand.cards[0].suit == hand.cards[3].suit) and (hand.cards[3].suit != hand.cards[2].suit) and (hand.cards[3].suit != hand.cards[0].suit) and (hand.cards[3].suit != hand.cards[4].suit) and (len([card for card in hand.cards if card.suit == 4]) == 2) and (hand.cards[3].val > 5):
		hand_confidences[7] += 40
	
	# Mutation Resistance: 0.389073810183%
	if (hand.cards[1].val > 9) and (len([card for card in hand.cards if card.val == 2]) == 0) and (hand.cards[4].suit == hand.cards[2].suit) and (hand.cards[3].val == hand.cards[1].val) and (len([card for card in hand.cards if card.val == 4]) != 0) and (hand.cards[0].suit != hand.cards[4].suit) and (len([card for card in hand.cards if card.suit == 4]) != 2):
		hand_confidences[7] += -70
	
	# Mutation Resistance: 862.844413183%
	if (len([card for card in hand.cards if card.val == 11]) != 2):
		hand_confidences[7] += -80
	
	# Mutation Resistance: 83.3333333333%
	if (hand.cards[1].val < 13) and (len([card for card in hand.cards if card.suit == 1]) != 2):
		hand_confidences[7] += 60
	
	# Mutation Resistance: 16.6666666667%
	if (hand.cards[2].val == hand.cards[3].val) and (len([card for card in hand.cards if card.val == 7]) != 4) and (hand.cards[2].val > 9):
		hand_confidences[7] += 40
	
	# Mutation Resistance: 791.662605983%
	if (hand.cards[2].val != hand.cards[1].val):
		hand_confidences[7] += -65
	
	# Mutation Resistance: 83.3333333333%
	if (hand.cards[2].val < 12) and (hand.cards[3].val == hand.cards[1].val):
		hand_confidences[7] += 100
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val == hand.cards[1].val) and (hand.cards[1].val < 5) and (len([card for card in hand.cards if card.suit == 1]) != 4) and (hand.cards[3].suit != hand.cards[1].suit) and (len([card for card in hand.cards if card.suit == 3]) != 2) and (hand.cards[4].suit != hand.cards[3].suit) and (hand.cards[1].suit == hand.cards[0].suit) and ((hand.cards[2].val - hand.cards[3].val) == 4) and (hand.cards[0].suit != hand.cards[3].suit):
		hand_confidences[7] += 20
	
	# Mutation Resistance: 797.317414423%
	if (hand.cards[2].val != hand.cards[4].val):
		hand_confidences[7] += -95
	
	# Mutation Resistance: 801.77362151%
	if (hand.cards[2].val != hand.cards[0].val):
		hand_confidences[7] += -85
	
	# Mutation Resistance: 83.3333333333%
	if (hand.cards[2].val < 12) and (hand.cards[3].val == hand.cards[1].val):
		hand_confidences[7] += 50
	
	# Mutation Resistance: 801.77362151%
	if (hand.cards[2].val != hand.cards[0].val):
		hand_confidences[7] += -25
	
	# Mutation Resistance: 83.3333333333%
	if (hand.cards[3].val == hand.cards[1].val) and (hand.cards[2].val < 12):
		hand_confidences[7] += 60
	
	# Mutation Resistance: 791.662605983%
	if (hand.cards[2].val != hand.cards[1].val):
		hand_confidences[7] += -100
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 7]) == 1) and (hand.cards[0].suit != hand.cards[3].suit) and (len([card for card in hand.cards if card.val == 3]) != 2) and (hand.cards[0].suit != hand.cards[1].suit) and (hand.cards[2].val == hand.cards[0].val) and (hand.cards[1].val == hand.cards[3].val) and (len([card for card in hand.cards if card.val == 12]) != 0):
		hand_confidences[7] += 20
	
	# Mutation Resistance: 100.0%
	if (hand.cards[2].suit == hand.cards[3].suit):
		hand_confidences[8] += 80
	
	# Mutation Resistance: 857.777777778%
	if (len([card for card in hand.cards if card.suit == 3]) != 5):
		hand_confidences[8] += -95
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 12]) == 3) and ((hand.cards[0].val - hand.cards[2].val) == -10):
		hand_confidences[8] += 65
	
	# Mutation Resistance: 583.472635149%
	if (hand.cards[1].suit != hand.cards[2].suit):
		hand_confidences[8] += -40
	
	# Mutation Resistance: 778.356143614%
	if (hand.cards[4].val != hand.cards[0].val):
		hand_confidences[8] += -45
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 13]) != 1) and (hand.cards[4].suit != hand.cards[3].suit):
		hand_confidences[8] += 50
	
	# Mutation Resistance: 100.0%
	if (hand.cards[2].val != hand.cards[0].val) and (hand.cards[3].val != hand.cards[4].val):
		hand_confidences[8] += 35
	
	# Mutation Resistance: 580.858460209%
	if (hand.cards[2].suit != hand.cards[0].suit):
		hand_confidences[8] += -95
	
	# Mutation Resistance: 100.0%
	if (hand.cards[0].suit == hand.cards[2].suit):
		hand_confidences[8] += 65
	
	# Mutation Resistance: 20.0%
	if (hand.cards[0].val > 7) and (hand.cards[2].val > 4):
		hand_confidences[8] += 35
	
	# Mutation Resistance: 100.0%
	if (hand.cards[3].val != hand.cards[2].val) and (len([card for card in hand.cards if card.val == 13]) != 2) and (hand.cards[0].val < 10):
		hand_confidences[8] += 45
	
	# Mutation Resistance: 720.509286775%
	if (hand.cards[0].val != hand.cards[1].val):
		hand_confidences[8] += -15
	
	# Mutation Resistance: 698.183744749%
	if (hand.cards[2].val > 3):
		hand_confidences[8] += -90
	
	# Mutation Resistance: 583.472635149%
	if (hand.cards[1].suit != hand.cards[2].suit):
		hand_confidences[8] += -65
	
	# Mutation Resistance: 8.9003581184%
	if (hand.cards[2].val == hand.cards[0].val) and (hand.cards[1].val < 13) and (len([card for card in hand.cards if card.suit == 1]) == 0):
		hand_confidences[8] += -65
	
	# Mutation Resistance: 80.0%
	if (hand.cards[1].val < 8):
		hand_confidences[8] += 70
	
	# Mutation Resistance: 60.0%
	if (len([card for card in hand.cards if card.val == 5]) != 3) and (hand.cards[0].val < 3) and (hand.cards[1].val != hand.cards[2].val):
		hand_confidences[8] += 10
	
	# Mutation Resistance: 684.569979635%
	if (hand.cards[0].val < 11) and (len([card for card in hand.cards if card.suit == 4]) != 4):
		hand_confidences[8] += -5
	
	# Mutation Resistance: 559.667850415%
	if (hand.cards[4].suit != hand.cards[1].suit):
		hand_confidences[8] += -5
	
	# Mutation Resistance: 100.0%
	if (hand.cards[3].val != hand.cards[2].val) and (hand.cards[0].val < 10) and (len([card for card in hand.cards if card.val == 13]) != 2):
		hand_confidences[8] += 75
	
	# Mutation Resistance: 857.777777778%
	if (len([card for card in hand.cards if card.suit == 1]) != 5):
		hand_confidences[8] += -90
	
	# Mutation Resistance: 100.0%
	if (hand.cards[0].val < 10) and (hand.cards[3].val != hand.cards[2].val) and (len([card for card in hand.cards if card.val == 13]) != 2):
		hand_confidences[8] += 40
	
	# Mutation Resistance: 539.698783827%
	if (len([card for card in hand.cards if card.val == 13]) != 2) and (hand.cards[0].suit != hand.cards[3].suit):
		hand_confidences[8] += -40
	
	# Mutation Resistance: 897.893609741%
	if (len([card for card in hand.cards if card.suit == 1]) != 4):
		hand_confidences[8] += -65
	
	# Mutation Resistance: 726.63783441%
	if (hand.cards[3].val != hand.cards[1].val):
		hand_confidences[8] += -50
	
	# Mutation Resistance: 100.0%
	if (len([card for card in hand.cards if card.suit == 2]) != 1) and (hand.cards[2].val != hand.cards[3].val):
		hand_confidences[8] += 20
	
	# Mutation Resistance: 100.0%
	if (hand.cards[4].val != hand.cards[0].val) and (hand.cards[0].val != hand.cards[4].val):
		hand_confidences[8] += 65
	
	# Mutation Resistance: 100.0%
	if (hand.cards[3].val != hand.cards[2].val) and (hand.cards[0].val < 10) and (len([card for card in hand.cards if card.val == 13]) != 2):
		hand_confidences[8] += 65
	
	# Mutation Resistance: 563.80125216%
	if (hand.cards[0].suit != hand.cards[1].suit):
		hand_confidences[8] += -35
	
	# Mutation Resistance: 763.984081089%
	if (hand.cards[2].val != hand.cards[4].val) and (len([card for card in hand.cards if card.val == 7]) != 4):
		hand_confidences[8] += -95
	
	# Mutation Resistance: 857.777777778%
	if (len([card for card in hand.cards if card.suit == 1]) != 5):
		hand_confidences[8] += -35
	
	# Mutation Resistance: 20.0%
	if (hand.cards[1].val > 3) and (len([card for card in hand.cards if card.val == 10]) != 3) and (hand.cards[0].val < 8) and (hand.cards[4].val > 4) and (len([card for card in hand.cards if card.suit == 1]) != 0) and (len([card for card in hand.cards if card.val == 10]) != 4):
		hand_confidences[8] += 95
	
	# Mutation Resistance: 857.777777778%
	if (len([card for card in hand.cards if card.suit == 1]) != 5):
		hand_confidences[8] += -80
	
	# Mutation Resistance: 100.0%
	if (hand.cards[0].val < 10) and (hand.cards[3].val != hand.cards[2].val) and (len([card for card in hand.cards if card.val == 13]) != 2):
		hand_confidences[8] += 70
	
	# Mutation Resistance: 747.317414423%
	if (len([card for card in hand.cards if card.val == 3]) != 4) and (hand.cards[2].val != hand.cards[4].val):
		hand_confidences[8] += -55
	
	# Mutation Resistance: 100.0%
	if (hand.cards[0].suit == hand.cards[2].suit):
		hand_confidences[8] += 40
	
	# Mutation Resistance: 583.472635149%
	if (hand.cards[1].suit != hand.cards[2].suit):
		hand_confidences[8] += -40
	
	# Mutation Resistance: 100.0%
	if (hand.cards[2].val != hand.cards[4].val) and (len([card for card in hand.cards if card.suit == 3]) != 2):
		hand_confidences[8] += 10
	
	# Mutation Resistance: 0.0%
	if (hand.cards[0].val > 11):
		hand_confidences[8] += 70
	
	# Mutation Resistance: 100.0%
	if (hand.cards[3].val != hand.cards[2].val) and (len([card for card in hand.cards if card.val == 13]) != 2) and (hand.cards[0].val < 10):
		hand_confidences[8] += 45
	
	# Mutation Resistance: 0.0%
	if (hand.cards[1].val < 12) and (len([card for card in hand.cards if card.val == 10]) == 4):
		hand_confidences[8] += 5
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 3]) == 0) and (hand.cards[2].val == hand.cards[4].val) and (hand.cards[4].suit == hand.cards[1].suit) and (hand.cards[3].val == hand.cards[1].val) and (hand.cards[3].val > 5) and (len([card for card in hand.cards if card.suit == 3]) != 1) and (len([card for card in hand.cards if card.val == 3]) == 2) and (hand.cards[1].val == hand.cards[4].val) and (hand.cards[0].val == hand.cards[1].val) and (len([card for card in hand.cards if card.suit == 1]) == 4) and (hand.cards[4].val > 3):
		hand_confidences[8] += -85
	
	# Mutation Resistance: 100.0%
	if (hand.cards[4].suit == hand.cards[0].suit):
		hand_confidences[9] += 75
	
	# Mutation Resistance: 553.642934383%
	if (hand.cards[4].val > 1) and (len([card for card in hand.cards if card.val == 12]) != 1) and (hand.cards[1].val != hand.cards[4].val):
		hand_confidences[9] += -100
	
	# Mutation Resistance: 3.39129311276%
	if (hand.cards[2].val > 8) and (hand.cards[2].val == hand.cards[4].val) and (hand.cards[3].val != hand.cards[4].val) and (len([card for card in hand.cards if card.suit == 4]) == 1) and (hand.cards[2].val > 11) and (len([card for card in hand.cards if card.val == 6]) != 0):
		hand_confidences[9] += -5
	
	# Mutation Resistance: 0.0%
	if ((hand.cards[3].val - hand.cards[0].val) == -9) and (hand.cards[4].val != hand.cards[1].val) and (hand.cards[1].suit != hand.cards[0].suit) and (len([card for card in hand.cards if card.suit == 1]) != 1):
		hand_confidences[9] += 100
	
	# Mutation Resistance: 628.690533125%
	if (hand.cards[3].val < 10):
		hand_confidences[9] += -100
	
	# Mutation Resistance: 80.0%
	if (hand.cards[2].val > 5) and (len([card for card in hand.cards if card.val == 1]) == 1):
		hand_confidences[9] += 15
	
	# Mutation Resistance: 100.0%
	if (hand.cards[3].val != hand.cards[1].val):
		hand_confidences[9] += 80
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 6]) == 3) and (hand.cards[4].suit == hand.cards[0].suit) and (hand.cards[1].suit == hand.cards[0].suit):
		hand_confidences[9] += -40
	
	# Mutation Resistance: 685.229857445%
	if (len([card for card in hand.cards if card.val == 2]) != 3) and (hand.cards[2].val != hand.cards[1].val):
		hand_confidences[9] += -10
	
	# Mutation Resistance: 855.603756604%
	if (hand.cards[3].val < 13):
		hand_confidences[9] += -70
	
	# Mutation Resistance: 559.353910415%
	if (hand.cards[2].suit != hand.cards[4].suit):
		hand_confidences[9] += -30
	
	# Mutation Resistance: 79.202660621%
	if (hand.cards[1].suit == hand.cards[2].suit) and (hand.cards[3].suit != hand.cards[2].suit) and (hand.cards[2].suit != hand.cards[3].suit) and (hand.cards[4].suit != hand.cards[1].suit):
		hand_confidences[9] += -90
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 9]) != 2) and (len([card for card in hand.cards if card.val == 10]) != 0) and (len([card for card in hand.cards if card.val == 4]) == 4):
		hand_confidences[9] += -95
	
	# Mutation Resistance: 100.0%
	if (hand.cards[3].val != hand.cards[1].val):
		hand_confidences[9] += 55
	
	# Mutation Resistance: 2.38203257914%
	if (hand.cards[2].val == hand.cards[1].val) and (len([card for card in hand.cards if card.suit == 2]) != 1) and (hand.cards[0].suit == hand.cards[1].suit) and (hand.cards[4].suit != hand.cards[3].suit) and (hand.cards[0].val < 7) and (len([card for card in hand.cards if card.suit == 3]) != 2):
		hand_confidences[9] += -80
	
	# Mutation Resistance: 100.0%
	if (hand.cards[3].val != hand.cards[1].val):
		hand_confidences[9] += 5
	
	# Mutation Resistance: 755.553281869%
	if (hand.cards[2].val != hand.cards[4].val) and (len([card for card in hand.cards if card.val == 2]) != 3):
		hand_confidences[9] += -10
	
	# Mutation Resistance: 80.0%
	if (hand.cards[2].val > 5) and (len([card for card in hand.cards if card.val == 1]) == 1):
		hand_confidences[9] += 60
	
	# Mutation Resistance: 428.629047164%
	if (hand.cards[1].suit != hand.cards[2].suit) and (hand.cards[1].val != hand.cards[3].val):
		hand_confidences[9] += -60
	
	# Mutation Resistance: 685.229857445%
	if (hand.cards[2].val != hand.cards[1].val) and (len([card for card in hand.cards if card.val == 2]) != 3):
		hand_confidences[9] += -55
	
	# Mutation Resistance: 559.667850415%
	if (hand.cards[1].suit != hand.cards[4].suit):
		hand_confidences[9] += -45
	
	# Mutation Resistance: 142.078698205%
	if (len([card for card in hand.cards if card.suit == 1]) != 0) and (hand.cards[2].val != hand.cards[0].val) and (len([card for card in hand.cards if card.val == 13]) != 0):
		hand_confidences[9] += -5
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.suit == 3]) == 4) and (hand.cards[4].val < 7):
		hand_confidences[9] += 95
	
	# Mutation Resistance: 693.887897%
	if (len([card for card in hand.cards if card.val == 10]) != 1):
		hand_confidences[9] += -35
	
	# Mutation Resistance: 0.0%
	if (len([card for card in hand.cards if card.val == 4]) != 1) and ((hand.cards[0].val - hand.cards[1].val) == 11) and (hand.cards[4].val > 12) and ((hand.cards[0].val - hand.cards[4].val) == -1) and (hand.cards[3].val > 8) and (hand.cards[3].suit != hand.cards[4].suit) and (hand.cards[3].suit != hand.cards[2].suit) and (len([card for card in hand.cards if card.suit == 3]) != 5) and (hand.cards[0].val == hand.cards[2].val) and (hand.cards[4].suit != hand.cards[3].suit) and (hand.cards[0].val < 10):
		hand_confidences[9] += -60
	
	# Mutation Resistance: 283.521991359%
	if (len([card for card in hand.cards if card.suit == 4]) != 1) and (hand.cards[3].suit == hand.cards[1].suit):
		hand_confidences[9] += -30
	
	# Mutation Resistance: 559.353910415%
	if (hand.cards[2].suit != hand.cards[4].suit):
		hand_confidences[9] += -65
	
	# Mutation Resistance: 628.690533125%
	if (hand.cards[3].val < 10):
		hand_confidences[9] += -30
	
	# Mutation Resistance: 628.690533125%
	if (hand.cards[3].val < 10):
		hand_confidences[9] += -90
	
	if max(hand_confidences) >= 100:
		hand.assigned_class = hand_confidences.index(max(hand_confidences))
	else:
		hand.assigned_class = 0