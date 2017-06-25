import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
from sklearn import tree
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

if __name__ == '__main__':
	df = pd.read_csv("player_data.csv")
	df = df.drop(df.columns[0], 1)


	innlist = list(df['Inns'])
	Inns = []
	for i in innlist:
		if(i == 1):
			Inns.append("I1")
		else:
			Inns.append("I2")
	df = df.drop('Inns', 1)
	df['Inns'] = Inns


	scorelist = list(df['Score'])
	Score = []
	for i in scorelist:
		if(i < 50):
			Score.append("S1")
		else:
			Score.append("S2")
	df = df.drop('Score', 1)
	df['Score'] = Score

	prev1list = list(df['Prev1'])
	Prev1 = []
	for i in prev1list:
		if(i < 50):
			Prev1.append("P1")
		else:
			Prev1.append("P2")
	df = df.drop('Prev1', 1)
	df['Prev1'] = Prev1

	prev2list = list(df['Prev2'])
	Prev2 = []
	for i in prev2list:
		if(i < 50):
			Prev2.append("P1")
		else:
			Prev2.append("P2")
	df = df.drop('Prev2', 1)
	df['Prev2'] = Prev2

	prev3list = list(df['Prev3'])
	Prev3 = []
	for i in prev3list:
		if(i < 50):
			Prev3.append("P1")
		else:
			Prev3.append("P2")
	df = df.drop('Prev3', 1)
	df['Prev3'] = Prev3





	fowlist = list(df['FoW'])
	fow_wicket = []
	fow_runs = []
	fow_overs = []
	for i in fowlist:
		if(i == '-  '):
			fow_wicket.append("FW0")
			#fow_runs.append(0)
			fow_overs.append("FO0")
		else:
			tmp1 = i.split("/")
			s = "FW" + tmp1[0]
			fow_wicket.append(s)
			tmp2 = tmp1[1].split(" ")
			#fow_runs.append(int(tmp2[0]))
			#fow_overs.append(float(tmp2[1].replace("(", "").replace(")", "")))
			x = int(float(tmp2[1].replace("(", "").replace(")", "")))
			if(x < 7):
				str = "FO0"
			elif(x < 20):
				str = "FO1"
			elif(x < 35):
				str = "FO2"
			else:
				str = "FO3"
			fow_overs.append(str)



	df = df.drop('MatchID', 1)
	df = df.drop('FoW', 1)
	df['fow_wicket'] = fow_wicket
	#df['fow_runs'] = fow_runs
	df['fow_overs'] = fow_overs


	#print df	
	#df.to_csv("kohli_data_categorical.csv")


	df2 = pd.get_dummies(df.drop(['Score'], 1))
	#print df2.columns
	#print len(df2.columns)
	df2['Score'] = Score
	#print df2.columns
	#print len(df2.columns)

	#print df2

	X = np.array(df2.drop(['Score'], 1))
	y = np.array(df2['Score'])

	X_scaled = preprocessing.scale(X)

	X_train, X_test, y_train, y_test = cross_validation.train_test_split(X_scaled, y, test_size=0.15)



	clf3 = tree.DecisionTreeClassifier()
	clf3.fit(X_train, y_train)
	predicted3 = clf3.predict(X_test)

	clf4 = GaussianNB()
	clf4.fit(X_train, y_train)
	predicted4 = clf4.predict(X_test)


	#with open("decisiontree.dot", 'w') as f:
	#    f = tree.export_graphviz(clf3, out_file=f)

	t = 0
	tacc = 0
	nacc = 0
	#print "Score", "\t", "Decision Tree", "\t", "Naive Bayes"
	for i, l, m in zip(y_test, predicted3, predicted4):
		#print i, "\t", l, "\t\t", m
		t = t + 1
		
	acc3 = float(accuracy_score(y_test, predicted3)) * 100
	acc4 = float(accuracy_score(y_test, predicted4)) * 100	
	#print acc3, "\t", acc4


	xt = []
	for i in range(len(y_test)):
		xt.append(i + 1)

	yt = []
	for i in y_test:
		if(i == 'S1'):
			yt.append(-50);
		else:
			yt.append(+50);

	y3 = []
	for i in predicted3:
		if(i == 'S1'):
			y3.append(-50);
		else:
			y3.append(+50);

	y4 = []
	for i in predicted4:
		if(i == 'S1'):
			y4.append(-50);
		else:
			y4.append(+50);

	ax = plt.subplot(211)
	plt.plot(xt, yt, 'ro', xt, y3, 'b^')
	plt.xlabel('Match')
	plt.ylabel('Score')
	ax.set_yticks((-50, +50))
	ax.set_xticks(xt)
	s = "%f" % acc3
	s = "Decision Tree Accuracy = " + s
	plt.text(10, 80, s)
	plt.axis([0, len(yt) + 1, -130, 130])
	plt.grid()


	ax = plt.subplot(212)
	plt.plot(xt, yt, 'ro', xt, y4, 'g^')
	plt.xlabel('Match')
	plt.ylabel('Score')
	ax.set_yticks((-50, +50))
	ax.set_xticks(xt)
	plt.axis([0, len(yt) + 1, -130, 130])
	s = "%f" % acc4
	s = 'Naive Bayes Accuracy = ' + s
	plt.text(10, 80, s)
	plt.grid()
	#mng = plt.get_current_fig_manager()
	#mng.frame.Maximize(True)
	#mng.window.showMaximized()
	plt.show()


