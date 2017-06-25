import urllib2
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
from sklearn import tree


urllink = "http://stats.espncricinfo.com/ci/engine/player/253802.html?class=2;filter=advanced;innings_number=1;innings_number=2;orderby=start;template=results;type=allround;view=innings"

#page = urllib2.urlopen(urllink)
file = open("player_HTML.txt", "r")
page = file.read()

soup = BeautifulSoup(page)

#print soup

all_tables=soup.find_all("table", class_="engineTable")
table = all_tables[3]

data = table.find_all("tr")
rows = data[1:]

Inns = []
Score = []
Overs = []
Conc = []
Wkts = []
Ct = []
St = []
Opposition =[]
Ground = []
Start_Date = []
MatchID = []
FoW = []

# Teams = {}
# Teams['Australia'] = 1
# Teams['South Africa'] = 2
# Teams['England'] = 3
# Teams['New Zealand'] = 4
# Teams['Sri Lanka'] = 5
# Teams['West Indies'] = 6
# Teams['Pakistan'] = 7
# Teams['Bangladesh'] = 8
# Teams['Ireland'] = 9
# Teams['Zimbabwe'] = 10
# Teams['U.A.E.'] = 11
# Teams['Netherlands'] = 12
# Teams['Afghanisthan'] = 13



for r in rows:
	cell = r.find_all("td")

	x = str(cell[1].text).replace("*", "")
	if((x <> "-") and (x <> "DNB")):
		Inns.append(int(cell[0].text))
		Score.append(int(x))
		Overs.append(str(cell[2].text))
		Conc.append(str(cell[3].text))
		Wkts.append(str(cell[4].text))
		Ct.append(str(cell[5].text))
		St.append(str(cell[6].text))
		Opposition.append(str(cell[8].text).replace("v ", ""))
		Ground.append(str(cell[9].text))
		Start_Date.append(str(cell[10].text))
		MatchID.append(str(cell[11].find("a").get("href")))


ScoreClass = Score
# for i in Score:
# 	if(i <= 20):
# 		ScoreClass.append(1)
# 	elif(i <= 40):
# 		ScoreClass.append(2)
# 	elif(i <= 60):
# 		ScoreClass.append(3)
# 	elif(i <= 80):
# 		ScoreClass.append(4)
# 	elif(i <= 100):
# 		ScoreClass.append(5)
# 	else:
# 		ScoreClass.append(6)

j = 0
for i in MatchID:
	url = "http://stats.espncricinfo.com" + i + "?innings=1;view=fow"
	#print url
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page)
	all_tables=soup.find_all("table", class_="partnership-table")
	if(Inns[j] == 1):
		x = 0
	else:
		x = 2
	table = all_tables[x]
	rows = table.find_all("tr")
	rows = rows[1:]
	res = "None"
	for r in rows:
		data = r.find_all("td")
		if(("Kohli" in data[4].text) or ("Kohli" in data[5].text)):
			res = str(data[6].text).replace("\n", "")
			break
	print j, res
	FoW.append(res)
	j = j + 1



df = pd.DataFrame()
df['Inns'] = Inns[3:]
df['Score'] = ScoreClass[3:]
#df['Overs'] = Overs[3:]
#df['Conc'] = Conc[3:]
#df['Wkts'] = Wkts[3:]
#df['Ct'] = Ct[3:]
#df['St'] = St[3:]
df['Opposition'] = Opposition[3:]
df['FoW'] = FoW[3:]
#df['Ground'] = Ground[3:]
#df['Start_Date'] = Start_Date[3:]
df['MatchID'] = MatchID[3:]

df['Prev1'] = ScoreClass[2:-1]
df['Prev2'] = ScoreClass[1:-2]
df['Prev3'] = ScoreClass[:-3]

print df
df.to_csv("player_data.csv")

# df2 = pd.read_csv("kohli_data.csv")
# df2 = df2.drop(df2.columns[0], 1)
# print df2

















# X = np.array(df.drop(['Score'], 1))
# y = np.array(df['Score'])

# print X[:9]
# print np.max(X[:9])

# enf = preprocessing.OneHotEncoder()#n_values = [2, 13, 6, 6, 6]


# print X[:9]


# X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.25)

# print df

# clf = svm.SVR()
# clf.fit(X_train, y_train)

# print X_test
# print X_test[0:1]
# for i in X[100:]:
# 	print i, clf.predict([i]) * 20
