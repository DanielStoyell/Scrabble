import numpy as np
from sklearn import neural_network
from sklearn import svm 
from sklearn import neighbors

def binary_feature_extract(move):
	FEATURES_LENGTH = 459
	v = [0]*FEATURES_LENGTH
	i = 0

	v[int(min(int(move["Turn"])/10, 10)+i)] = 1
	i += 10

	for letter in move["Letters_Used"]:
		v[(hash(letter)%26)+i] = 1
	i+=26

	v[int(hash(move["Word"])%100)+i] = 1
	i+=100

	for letter in move["Rack"]:
		v[(hash(letter)%26)+i] = 1
	i+=26

	v[(0 if move["Direction"]=="Horizontal" else 1)+i] = 1
	i += 2

	start_square = eval(move["Start"])
	v[(start_square[0]*15+start_square[1])+i] = 1
	i += 15*15

	v[min(int(int(move["Player_Score"])%10), 50)+i] = 1
	i += 50

	v[min(int(int(move["Move_Score"])%10), 20)+i] = 1
	i += 20

	return v

def feature_extract(move):
	v = []
	v.append(int(move["Turn"]))
	for letter in move["Letters_Used"]:
		v.append(ord(letter))
	for i in range(12-len(move["Letters_Used"])):
		v.append(0)
	v.append(sum([ord(x) for x in move["Word"]]))

	for letter in move["Rack"]:
		v.append(ord(letter))
	for i in range(12-len(move["Rack"])):
		v.append(0)

	v.append(0 if move["Direction"]=="Horizontal" else 1)
	start_square = eval(move["Start"])
	v.append(start_square[0]*15+start_square[1])
	v.append(int(move["Player_Score"]))
	v.append(int(move["Move_Score"]))

	return v

def naivebayesPY(x,y):
	y = np.concatenate([y, [-1,1]])
	n = len(y)
	pos = ((y == 1).sum())/float(n)
	neg = 1.0 - pos
	return pos, neg

def naivebayesPXY(x,y):
	n, d = x.shape
	x = np.concatenate([x, np.ones((2,d))])
	y = np.concatenate([y, [-1,1]])
	n, d = x.shape
	
	y = y.reshape(n,1)
	
	#positive probability
	yBool = y == 1
	xTimesy = x*yBool
	numerator = np.sum(xTimesy, axis=0)
	xSum = np.sum(x, axis=1)
	denominatorBig = xSum*np.transpose(yBool)[0]
	denominator = np.sum(denominatorBig, axis=0)
	posprob = numerator/denominator
	
	#negative probability
	yBool = y == -1
	xTimesy = x*yBool
	numerator = np.sum(xTimesy, axis=0)
	xSum = np.sum(x, axis=1)
	denominatorBig = xSum*np.transpose(yBool)[0]
	denominator = np.sum(denominatorBig, axis=0)
	negprob = numerator/denominator
	
	return posprob, negprob

def naivebayesCL(x,y):
	x = np.array(x)
	y = np.array(y)
	n, d = x.shape
	
	posprob, negprob = naivebayesPXY(x,y)
	pos, neg = naivebayesPY(x,y)
	
	b = np.log(pos) - np.log(neg)
	w = np.log(posprob) - np.log(negprob)

	def classifier(xTest):
		xTest = np.array(xTest)
		return np.dot(w, np.transpose(xTest)) + b
	
	return classifier

def getBest(preds):
	return np.argmax(preds)

def construct_test(moves, board, player, turn, binary=False):
	xTest = []
	for move in moves:
		m = {
			"Turn": turn,
			"Letters_Used": str(move["word"]), #Temporary
			"Word": move["word"],
			"Rack": player.rack,
			"Direction": move["direction"],
			"Start": str(move["square"]),
			"Move_Score": str(move["score"]),
			"Player_Score": str(player.score)
		}
		if binary:
			xTest.append(binary_feature_extract(m))
		else:
			xTest.append(feature_extract(m))
	return xTest

def nnCL(xTr, yTr):
	xTr = np.array(xTr)
	yTr = np.array(yTr)
	classifier = neural_network.MLPClassifier(hidden_layer_sizes=(50,50,50))
	classifier.fit(xTr, yTr)
	return classifier

def knnCL(xTr, yTr):
	xTr = np.array(xTr)
	yTr = np.array(yTr)
	classifier = neighbors.KNeighborsClassifier(n_neighbors=10)
	classifier.fit(xTr,yTr)
	return classifier

def find_best(xTest, classifier):
	xTest = np.array(xTest)
	win_index = np.where(classifier.classes_ == 1)[0][0]
	probs = classifier.predict_proba(xTest)
	max_win = 0
	max_index = 0
	for i in range(len(probs)):
		if probs[i][win_index] >= max_win:
			max_win = probs[i][win_index]
			max_index = i
	return i