import pandas as pd
import numpy as np
from tabulate import tabulate 

if __name__ == '__main__':
	df = pd.read_csv("player_data_categorical.csv")
	df = df.drop(df.columns[0], 1)
	df = df.drop('Prev2', 1)
	df = df.drop('Prev3', 1)

	X = np.array(df)

	threshold = [0, 17, 13, 11, 9, 8, 8]


	itemset = {}

	for i in range(len(X)):
		for j in range(len(X[0])):
			itemset[X[i][j]] = 0

	for i in range(len(X)):
		for j in range(len(X[0])):
			itemset[X[i][j]] = itemset[X[i][j]] + 1

	itemset_copy = dict(itemset)
	for i in itemset_copy:
		if(itemset_copy[i] < threshold[1]):
			del itemset[i]

	data = []
	for i in itemset:
		data.append(i)

	#print "data : ", len(data)





	l = 2
	dataset2 = []
	for i in range(len(data)):
		for j in range(i + 1, len(data)):
			tmp = []
			tmp.append(data[i])
			tmp.append(data[j])
			if(tmp not in dataset2):
				dataset2.append(tmp)

	freq2 = [0] * len(dataset2)

	for i in X:
		for j in range(len(dataset2)):
			if(dataset2[j][0] in i and dataset2[j][1] in i):
				freq2[j] = freq2[j] + 1

	dataset2 = [dataset2[i] for i in range(len(dataset2)) if freq2[i] >= threshold[2]]
	freq2 = [freq2[i] for i in range(len(freq2)) if freq2[i] >= threshold[2]]

	#print "dataset2 : ", len(dataset2)






	l = 3
	dataset3 = []
	t = 0
	for i in range(len(dataset2)):
		for j in range(i + 1, len(dataset2)):
			tmp = []
			for k in dataset2[i]:
				tmp.append(k)
			for k in dataset2[j]:
				tmp.append(k)
			tmpl = list(set(tmp))
			if(len(tmpl) <= 3 and tmpl not in dataset3):
				dataset3.append(tmpl)

	freq3 = [0] * len(dataset3)

	for i in X:
		for j in range(len(dataset3)):
			inc = True
			for k in dataset3[j]:
				if(k not in i):
					inc = False
					break
			if(inc == True):
				freq3[j] = freq3[j] + 1

	dataset3 = [dataset3[i] for i in range(len(dataset3)) if freq3[i] >= threshold[3]]
	freq3 = [freq3[i] for i in range(len(freq3)) if freq3[i] >= threshold[3]]

	#print "dataset3 : ", len(dataset3)







	l = 4
	dataset4 = []
	t = 0
	for i in range(len(dataset3)):
		for j in range(i + 1, len(dataset3)):
			tmp = []
			for k in dataset3[i]:
				tmp.append(k)
			for k in dataset3[j]:
				tmp.append(k)
			tmpl = list(set(tmp))
			if(len(tmpl) <= 5 and tmpl not in dataset4):
				dataset4.append(tmpl)

	freq4 = [0] * len(dataset4)


	for i in X:
		for j in range(len(dataset4)):
			inc = True
			for k in dataset4[j]:
				if(k not in i):
					inc = False
					break
			if(inc == True):
				freq4[j] = freq4[j] + 1


	dataset4 = [dataset4[i] for i in range(len(dataset4)) if freq4[i] >= threshold[4]]
	freq4 = [freq4[i] for i in range(len(freq4)) if freq4[i] >= threshold[4]]


	#print "dataset4 : ", len(dataset4)








	l = 5
	dataset5 = []
	t = 0
	for i in range(len(dataset4)):
		for j in range(i + 1, len(dataset4)):
			tmp = []
			for k in dataset4[i]:
				tmp.append(k)
			for k in dataset4[j]:
				tmp.append(k)
			tmpl = list(set(tmp))
			if(len(tmpl) <= 7 and tmpl not in dataset5):
				dataset5.append(tmpl)

	freq5 = [0] * len(dataset5)


	for i in X:
		for j in range(len(dataset5)):
			inc = True
			for k in dataset5[j]:
				if(k not in i):
					inc = False
					break
			if(inc == True):
				freq5[j] = freq5[j] + 1


	dataset5 = [dataset5[i] for i in range(len(dataset5)) if freq5[i] >= threshold[5]]
	freq5 = [freq5[i] for i in range(len(freq5)) if freq5[i] >= threshold[5]]


	#print "dataset5 : ", len(dataset5)







	l = 6
	dataset6 = []
	t = 0
	for i in range(len(dataset5)):
		for j in range(i + 1, len(dataset5)):
			tmp = []
			for k in dataset5[i]:
				tmp.append(k)
			for k in dataset5[j]:
				tmp.append(k)
			tmpl = list(set(tmp))
			if(len(tmpl) <= 7 and tmpl not in dataset6):
				dataset6.append(tmpl)

	freq6 = [0] * len(dataset6)


	for i in X:
		for j in range(len(dataset6)):
			inc = True
			for k in dataset6[j]:
				if(k not in i):
					inc = False
					break
			if(inc == True):
				freq6[j] = freq6[j] + 1


	dataset6 = [dataset6[i] for i in range(len(dataset6)) if freq6[i] >= threshold[6]]
	freq6 = [freq6[i] for i in range(len(freq6)) if freq6[i] >= threshold[6]]


	#print "dataset6 : ", len(dataset6)










	confidence = [0.0, 0.0, 70.0, 70.0, 70.0, 70.0, 70.0]
	rules = []





	d = 2
	for d, f in zip(dataset2, freq2):
		#print d, f
		
		ruleset2 = []		#lhs = 1
		for i in range(len(d)):		
			lhs = [d[i]]
			rhs = list(set(d) - set(lhs))
			tmp = []
			tmp.append(lhs)
			tmp.append(rhs)
			if('FW1' not in rhs):
				ruleset2.append(tmp)
		count2 = []
		for i in ruleset2:
			count = 0
			for j in X:
				inc = True
				for k in i[0]:
					if k not in j:
						inc = False
						break
				if(inc == True):
					count = count + 1
			count2.append(f * 100.0 / count)

		for i, j in zip(ruleset2, count2):
			if(j >= confidence[2]):
				rules.append([i, f, j])









	d = 3
	for d, f in zip(dataset3, freq3):
		#print d, f
		
		ruleset3 = []		#lhs = 1
		for i in range(len(d)):		
			lhs = [d[i]]
			rhs = list(set(d) - set(lhs))
			tmp = []
			tmp.append(lhs)
			tmp.append(rhs)
			if('FW1' not in rhs):
				ruleset3.append(tmp)
		count3 = []
		for i in ruleset3:
			count = 0
			for j in X:
				inc = True
				for k in i[0]:
					if k not in j:
						inc = False
						break
				if(inc == True):
					count = count + 1
			count3.append(f * 100.0 / count)

		for i, j in zip(ruleset3, count3):
			if(j >= confidence[3]):
				rules.append([i, f, j])



		ruleset3 = []		#lhs = 2
		for i in range(len(d)):	
			for j in range(i + 1, len(d)):	
				lhs = [d[i], d[j]]
				rhs = list(set(d) - set(lhs))
				tmp = []
				tmp.append(lhs)
				tmp.append(rhs)
				if('FW1' not in rhs):
					ruleset3.append(tmp)
		count3 = []
		for i in ruleset3:
			count = 0
			for j in X:
				inc = True
				for k in i[0]:
					if k not in j:
						inc = False
						break
				if(inc == True):
					count = count + 1
			count3.append(f * 100.0 / count)

		for i, j in zip(ruleset3, count3):
			if(j >= confidence[3]):
				rules.append([i, f, j])








	d = 4
	for d, f in zip(dataset4, freq4):
		
		ruleset4 = []		#lhs = 1
		for i in range(len(d)):		
			lhs = [d[i]]
			rhs = list(set(d) - set(lhs))
			tmp = []
			tmp.append(lhs)
			tmp.append(rhs)
			if(len(rhs) > 0 and 'FW1' not in rhs):
				ruleset4.append(tmp)
		count4 = []
		for i in ruleset4:
			count = 0
			for j in X:
				inc = True
				for k in i[0]:
					if k not in j:
						inc = False
						break
				if(inc == True):
					count = count + 1
			count4.append(f * 100.0 / count)

		for i, j in zip(ruleset4, count4):
			if(j >= confidence[4]):
				rules.append([i, f, j])



		ruleset4 = []		#lhs = 2
		for i in range(len(d)):	
			for j in range(i + 1, len(d)):	
				lhs = [d[i], d[j]]
				rhs = list(set(d) - set(lhs))
				tmp = []
				tmp.append(lhs)
				tmp.append(rhs)
				if(len(rhs) > 0 and 'FW1' not in rhs):
					ruleset4.append(tmp)
		count4 = []
		for i in ruleset4:
			count = 0
			for j in X:
				inc = True
				for k in i[0]:
					if k not in j:
						inc = False
						break
				if(inc == True):
					count = count + 1
			count4.append(f * 100.0 / count)

		for i, j in zip(ruleset4, count4):
			if(j >= confidence[4]):
				rules.append([i, f, j])




		ruleset4 = []		#lhs = 3
		for i in range(len(d)):	
			for j in range(i + 1, len(d)):	
				for k in range(j + 1, len(d)):
					lhs = [d[i], d[j], d[k]]
					rhs = list(set(d) - set(lhs))
					tmp = []
					tmp.append(lhs)
					tmp.append(rhs)
					if(len(rhs) > 0 and 'FW1' not in rhs):
						ruleset4.append(tmp)
		count4 = []
		for i in ruleset4:
			count = 0
			for j in X:
				inc = True
				for k in i[0]:
					if k not in j:
						inc = False
						break
				if(inc == True):
					count = count + 1
			count4.append(f * 100.0 / count)

		for i, j in zip(ruleset4, count4):
			if(j >= confidence[4]):
				rules.append([i, f, j])








	d = 5
	for d, f in zip(dataset5, freq5):
		#print d, f
		
		ruleset5 = []		#lhs = 1
		for i in range(len(d)):		
			lhs = [d[i]]
			rhs = list(set(d) - set(lhs))
			tmp = []
			tmp.append(lhs)
			tmp.append(rhs)
			if(len(rhs) > 0 and 'FW1' not in rhs):
				ruleset5.append(tmp)
		count5 = []
		for i in ruleset5:
			count = 0
			for j in X:
				inc = True
				for k in i[0]:
					if k not in j:
						inc = False
						break
				if(inc == True):
					count = count + 1
			count5.append(f * 100.0 / count)

		for i, j in zip(ruleset5, count5):
			if(j >= confidence[5]):
				rules.append([i, f, j])



		ruleset5 = []		#lhs = 2
		for i in range(len(d)):	
			for j in range(i + 1, len(d)):	
				lhs = [d[i], d[j]]
				rhs = list(set(d) - set(lhs))
				tmp = []
				tmp.append(lhs)
				tmp.append(rhs)
				if(len(rhs) > 0 and 'FW1' not in rhs):
					ruleset5.append(tmp)
		count5 = []
		for i in ruleset5:
			count = 0
			for j in X:
				inc = True
				for k in i[0]:
					if k not in j:
						inc = False
						break
				if(inc == True):
					count = count + 1
			count5.append(f * 100.0 / count)

		for i, j in zip(ruleset5, count5):
			if(j >= confidence[5]):
				rules.append([i, f, j])




		ruleset5 = []		#lhs = 3
		for i in range(len(d)):	
			for j in range(i + 1, len(d)):	
				for k in range(j + 1, len(d)):
					lhs = [d[i], d[j], d[k]]
					rhs = list(set(d) - set(lhs))
					tmp = []
					tmp.append(lhs)
					tmp.append(rhs)
					if(len(rhs) > 0 and 'FW1' not in rhs):
						ruleset5.append(tmp)
		count5 = []
		for i in ruleset5:
			count = 0
			for j in X:
				inc = True
				for k in i[0]:
					if k not in j:
						inc = False
						break
				if(inc == True):
					count = count + 1
			count5.append(f * 100.0 / count)

		for i, j in zip(ruleset5, count5):
			if(j >= confidence[5]):
				rules.append([i, f, j])




		ruleset5 = []		#lhs = 4
		for i in range(len(d)):	
			for j in range(i + 1, len(d)):	
				for k in range(j + 1, len(d)):
					for l in range(k + 1, len(d)):
						lhs = [d[i], d[j], d[k], d[l]]
						rhs = list(set(d) - set(lhs))
						tmp = []
						tmp.append(lhs)
						tmp.append(rhs)
						if(len(rhs) > 0 and 'FW1' not in rhs):
							ruleset5.append(tmp)
		count5 = []
		for i in ruleset5:
			count = 0
			for j in X:
				inc = True
				for k in i[0]:
					if k not in j:
						inc = False
						break
				if(inc == True):
					count = count + 1
			count5.append(f * 100.0 / count)

		for i, j in zip(ruleset5, count5):
			if(j >= confidence[5]):
				rules.append([i, f, j])










	d = 6
	for d, f in zip(dataset6, freq6):
		#print d, f
		
		ruleset6 = []		#lhs = 1
		for i in range(len(d)):		
			lhs = [d[i]]
			rhs = list(set(d) - set(lhs))
			tmp = []
			tmp.append(lhs)
			tmp.append(rhs)
			if(len(rhs) > 0 and 'FW1' not in rhs):
				ruleset6.append(tmp)
		count6 = []
		for i in ruleset6:
			count = 0
			for j in X:
				inc = True
				for k in i[0]:
					if k not in j:
						inc = False
						break
				if(inc == True):
					count = count + 1
			count6.append(f * 100.0 / count)

		for i, j in zip(ruleset6, count6):
			if(j >= confidence[6]):
				rules.append([i, f, j])



		ruleset6 = []		#lhs = 2
		for i in range(len(d)):	
			for j in range(i + 1, len(d)):	
				lhs = [d[i], d[j]]
				rhs = list(set(d) - set(lhs))
				tmp = []
				tmp.append(lhs)
				tmp.append(rhs)
				if(len(rhs) > 0 and 'FW1' not in rhs):
					ruleset6.append(tmp)
		count6 = []
		for i in ruleset6:
			count = 0
			for j in X:
				inc = True
				for k in i[0]:
					if k not in j:
						inc = False
						break
				if(inc == True):
					count = count + 1
			count6.append(f * 100.0 / count)

		for i, j in zip(ruleset6, count6):
			if(j >= confidence[6]):
				rules.append([i, f, j])




		ruleset6 = []		#lhs = 3
		for i in range(len(d)):	
			for j in range(i + 1, len(d)):	
				for k in range(j + 1, len(d)):
					lhs = [d[i], d[j], d[k]]
					rhs = list(set(d) - set(lhs))
					tmp = []
					tmp.append(lhs)
					tmp.append(rhs)
					if(len(rhs) > 0 and 'FW1' not in rhs):
						ruleset6.append(tmp)
		count6 = []
		for i in ruleset6:
			count = 0
			for j in X:
				inc = True
				for k in i[0]:
					if k not in j:
						inc = False
						break
				if(inc == True):
					count = count + 1
			count6.append(f * 100.0 / count)

		for i, j in zip(ruleset6, count6):
			if(j >= confidence[6]):
				rules.append([i, f, j])




		ruleset6 = []		#lhs = 4
		for i in range(len(d)):	
			for j in range(i + 1, len(d)):	
				for k in range(j + 1, len(d)):
					for l in range(k + 1, len(d)):
						lhs = [d[i], d[j], d[k], d[l]]
						rhs = list(set(d) - set(lhs))
						tmp = []
						tmp.append(lhs)
						tmp.append(rhs)
						if(len(rhs) > 0 and 'FW1' not in rhs):
							ruleset6.append(tmp)
		count6 = []
		for i in ruleset6:
			count = 0
			for j in X:
				inc = True
				for k in i[0]:
					if k not in j:
						inc = False
						break
				if(inc == True):
					count = count + 1
			count6.append(f * 100.0 / count)

		for i, j in zip(ruleset6, count6):
			if(j >= confidence[6]):
				rules.append([i, f, j])




		ruleset6 = []		#lhs = 5
		for i in range(len(d)):	
			for j in range(i + 1, len(d)):	
				for k in range(j + 1, len(d)):
					for l in range(k + 1, len(d)):
						for m in range(l + 1, len(d)):
							lhs = [d[i], d[j], d[k], d[l], d[m]]
							rhs = list(set(d) - set(lhs))
							tmp = []
							tmp.append(lhs)
							tmp.append(rhs)
						if(len(rhs) > 0 and 'FW1' not in rhs):
							ruleset6.append(tmp)
		count6 = []
		for i in ruleset6:
			count = 0
			for j in X:
				inc = True
				for k in i[0]:
					if k not in j:
						inc = False
						break
				if(inc == True):
					count = count + 1
			count6.append(f * 100.0 / count)

		for i, j in zip(ruleset6, count6):
			if(j >= confidence[6]):
				rules.append([i, f, j])



		

	lhs = []
	rhs = []
	supp = []
	conf = []

	for i in rules:
		lhs.append(i[0][0])
		rhs.append(i[0][1])
		supp.append(i[1])
		conf.append(i[2])





	lhs2 = []
	rhs2 =[]
	supp2 =[]
	conf2 =[]
	for l, r, s, c in zip(lhs, rhs, supp, conf):
		if(r not in rhs2):
			lhs2.append(l)
			rhs2.append(r)
			supp2.append(s)
			conf2.append(c)
		else:
			occ = False
			for i in lhs2:
				if(set(l) == set(i)):
					occ = True
					break
			if(occ == False):
				lhs2.append(l)
				rhs2.append(r)
				supp2.append(s)
				conf2.append(c)

	rules = []
	for i, j, k, l in zip(lhs2, rhs2, supp2, conf2):
		rules.append([i, j, k ,l])


	print tabulate(rules, headers=["Antecedent", "Consequent", "Support Count", "Confidence"], tablefmt="fancy_grid")