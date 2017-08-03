from classifier import classify
from chromosome import Chromosome
from gene import Gene
from condition import *
from hand import Hand
from pandas import read_csv
from re import findall

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
	
def find_condition(condition_string):
	'''
	From condition str representation, find the condition
	'''
	parameters = map(int, findall(r'\d+', condition_string))
	condition = None
	if "-" in condition_string and "==" in condition_string and "val" in condition_string:
		condition = ValueDiffEq(0)
	elif "==" in condition_string and "val" in condition_string:
		condition = ValueEq(0)
	elif "!=" in condition_string and "val" in condition_string:
		condition = ValueIneq(0)
	elif ">" in condition_string and "val" in condition_string:
		condition = ValueGt(0)
	elif "<" in condition_string and "val" in condition_string:
		condition = ValueLt(0)
	elif "==" in condition_string and "suit" in condition_string:
		condition = SuitEq(0)
	elif "!=" in condition_string and "suit" in condition_string:
		condition = SuitIneq(0)
	if condition is not None:
		condition.parameters = tuple(parameters)
	return condition
	
	

def find_hand_class(hand_class_string):
	'''
	From string of format "hand_classes[i] += 1" find i
	'''
	stuff = hand_class_string.split("[")
	return int(stuff[1][0])
	
def get_best_chromosome():
	best_chromosome = Chromosome()
	with open("classifier.py", "r") as best_file:
		content = best_file.read().split('\n')
		for i in range(len(content)):
			if "if " in content[i]:
				gene = Gene()
				content[i].replace("if ", "")
				content[i].replace(":", "")
				content[i].replace("(", "")
				content[i].replace(")", "")
				conditions = content[i].split(" and ")
				gene.hand_class = find_hand_class(content[i+1])
				for condition in conditions:
					gene.conditions.append(find_condition(condition))
				best_chromosome.genes.append(gene)
	return best_chromosome
					
				
				
				
				
				
				