from classifier import classify
from chromosome import Chromosome
from gene import Gene
from condition import *
from hand import Hand
from pandas import read_csv
from re import findall
import os

def get_classified_hands(data_path):
	''' Classifies hands using python script from GA (importCSV.py) '''
	df = read_csv(data_path)
	hands = []
	for index, row in df.iterrows():
		hands.append(Hand(row))
	classify(hands)
	return hands
	
def get_data_bias(data_path):
	'''
	Debugging function to get the bias in the csv data. The input is the path to the
	data as a string (relative or absolute)
	'''
	df = read_csv(data_path)
	hands = []
	for index, row in df.iterrows():
		hands.append(Hand(row))
		
	class_occurences = [0 for i in range(10)]
	for hand in hands:
		class_occurences[hand.labelled_class] += 1
	
	class_occurences = [100.0 * float(coc) / float(len(hands)) for coc in class_occurences]
	for i in range(len(class_occurences)):
		print "Class %s: %.4f percent" % (i, class_occurences[i])
	
	return class_occurences
	
def join_dirs(base_dir, *dirs):
	final_dir = base_dir
	for dir in dirs:
		# Check for Windows
		if os.name == "nt":
			final_dir += "\\%s" % dir
		else:
			final_dir += "/%s" % dir
	return final_dir
	
def find_condition(condition_string):
	'''
	From condition str representation, find the condition
	'''
	condition = None
	
	# Loop through all possible conditions, and see if the string matches with any of them
	possible_conditions = Condition.get_conditions()
	for possible_condition in possible_conditions:
		if possible_condition.is_string_condition(condition_string):
			condition = possible_condition(0)
			break
			
	# Find the parameters for the condition if the string is a condition
	if condition is not None:
		parameters = map(int, findall(r'[-]?\d+', condition_string))
		condition.parameters = tuple(parameters)
	else:
		print "Unable to find correct condition"
		print condition_string
		
	return condition

def find_hand_class(hand_class_string):
	'''
	From string of format "hand_classes[i] += 1" find i
	'''
	stuff = hand_class_string.split("[")
	return int(stuff[1][0])
	
def find_confidence(confidence_string):
	stuff = confidence_string.split(" += ")
	return int(stuff[1])
	
def get_best_chromosome(function_name):
	best_chromosome = Chromosome()
	with open("classifier.py", "r") as best_file:
		content = best_file.read().split('\n')
		start = False
		for i in range(len(content)):
			# Start and stop conditions
			if ("def " + function_name + "(hand):") in content[i]:
				start = True
				continue
			elif "def " in content[i]:
				start = False
				continue
				
			# Parsing
			if start and "if " in content[i] and "hand_confidences" not in content[i]:
				gene = Gene()
				content[i].replace("if ", "")
				content[i].replace(":", "")
				conditions = content[i].split(" and ")
				gene.hand_class = find_hand_class(content[i+1])
				gene.confidence = find_confidence(content[i+1])
				for condition in conditions:
					gene.conditions.append(find_condition(condition))
				best_chromosome.genes.append(gene)
			elif start and "else:" in content[i]:
				stuff = content[i + 1].split(" = ")
				best_chromosome.default_class = int(stuff[1])
	return best_chromosome
					
				
				
				
				
				
				