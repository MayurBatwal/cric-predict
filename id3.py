import numpy as np 
import pandas as pd
import math

df = pd.read_csv('player_data_categorical.csv')
df = df.drop(df.columns[0], 1)


attributes = ['Opposition', 'Inns', 'Prev1', 'Prev2', 'Prev3', 'fow_wicket', 'fow_overs']
attr_values = [['Sri Lanka', 'Australia', 'Pakistan', 'Bangladesh', 'West Indies', 'New Zealand', 'South Africa', 'England', 'Ireland', 'Zimbabwe', 'U.A.E.', 'Netherlands', 'Afghanisthan'],
			   ['I1', 'I2'],
			   ['P1', 'P2'],
			   ['P1', 'P2'],
			   ['P1', 'P2'], 
			   ['FW0', 'FW1', 'FW2', 'FW3', 'FW4', 'FW5'],
			   ['FO0', 'FO1', 'FO2', 'FO3']]
Class_label = 'Score'
Class = ['S1', 'S2']



class Node:
	value = ''
	children = []



def attr_selection(df, attributes, attr_values):
	y = list(df[Class_label])
	#print y

	p = list(y).count(Class[0]) * 1.0
	n = list(y).count(Class[1]) * 1.0
	t = len(y)

	E = -((p / t) * math.log((p / t), 2)) - ((n / t) * math.log((n / t), 2)) 
	#print "E : ", E

	gain = [0] * len(attributes)

	for i in range(len(attributes)):	
		attr_val = attr_values[i]

		l = list(df[attributes[i]])
		d = [[] for j in range(len(attr_val))]
		for j in range(len(y)):
			d[attr_val.index(l[j])].append(y[j])

		Ei = 0
		for j in range(len(attr_val)):
			p = list(d[j]).count(Class[0]) * 1.0
			n = list(d[j]).count(Class[1]) * 1.0
			t = p + n
			if(p == 0 or n == 0):
				w = 0
			else:
				w = (p * math.log((p / t), 2)) + (n * math.log((n / t), 2))
			Ei = Ei - (w)

		Ei = Ei / len(y)
		gain[i] = E - Ei
		#print attributes[i], ":", gain[i]

			
	return gain.index(max(gain))

def decisionTree(df, attributes, attr_values, level):
	N = Node()

	y = list(df[Class_label])
	#print y.count('yes'), y.count('no'), len(y)
	if(y.count(Class[0]) == len(y)):
		N.value = Class[0]
		print " " * level * 5, "class : ", N.value
		return N
	if(y.count(Class[1]) == len(y)):
		N.value = Class[1]
		print " " * level * 5, "class : ", N.value
		return N

	if(len(attributes) == 0):
		if(y.count(Class[0]) >= y.count(Class[1])):
			N.value = Class[0]
		else:
			N.value = Class[1]
		print " " * level * 5, "class : ", N.value
		return N

	best_attr = attr_selection(df, attributes, attr_values)
	print " " * level * 5, "Node : ", attributes[best_attr]
	N.value = attributes[best_attr]

	attr_val = attr_values[best_attr]   #youth, middle_aged, senior
	l = list(df[attributes[best_attr]]) #df['age']

	del attributes[best_attr]
	del attr_values[best_attr]

	attr_list = list(attributes)
	avalues = list(attr_values)

	d = [[] for j in range(len(attr_val))]
	for j in range(len(l)):
		d[attr_val.index(l[j])].append(j)

	for i in range(len(attr_val)):
		print " " * level * 5, "branch : ", attr_val[i]
		k = 0
		dfi = pd.DataFrame(columns = df.columns)
		for j in d[i]:
			dfi.loc[k] = df.loc[j]
			k = k + 1

		if(len(dfi) == 0):
			if(y.count(Class[0]) >= y.count(Class[1])):
				N.value = Class[0]
			else:
				N.value = Class[1]
		else:
			N.children.append(decisionTree(dfi, list(attr_list), list(avalues), level + 1))

	#print N.value
	return N




	
a = decisionTree(df, attributes, attr_values, 0)
