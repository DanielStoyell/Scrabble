import numpy as np

FEATURES_LENGTH = 459

def feature_extract(move):
	v = [0]*FEATURES_LENGTH
	i = 0

	v[int(min(int(move["Turn"])/10, 10)+i)]
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

def construct_test(moves, board, player, turn):
	xTest = []
	for move in moves:
		m = {
			"Turn": turn,
			"Letters_Used": str(move["word"]), #Temporary
			"Word": move["word"],
			"Rack": str(player.rack),
			"Direction": move["direction"],
			"Start": str(move["square"]),
			"Move_Score": str(move["score"]),
			"Player_Score": str(player.score)
		}
		xTest.append(feature_extract(m))
	return xTest