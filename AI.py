import components
from itertools import permutations
import time
import learning
import csv
import random

"""
Example move:
move = {
	"word": "banana"
	"score": 26
	"square": [4,5]
	"direction": "Vertical"
	"type": "word" #Could be "skip"
}

"""

### learning Construction ###
print("Reading in and constructing training data")
binaryxTr = []
xTr = []
yTr = []
dataFile = open("totalgamedata.txt", "r")
reader = csv.DictReader(dataFile, delimiter=";")
for row in reader:
	v = learning.binary_feature_extract(row)
	binaryxTr.append(v)
	v = learning.feature_extract(row)
	xTr.append(v)
	yTr.append(int(row["Win"]))

#Trains and returns classifier function
#classifier function returns distances from linear separator
#To get classification, take np.sign(preds[i]), where preds is a return value
print("Training naive bayes classifier")
bayesClassifier = learning.naivebayesCL(binaryxTr,yTr)
print("Training neural network classifier")
nnClassifier = learning.nnCL(xTr, yTr)
print("Training knn classifier")
knnClassifier = learning.knnCL(xTr, yTr)
print("classifier training complete")

#### END classifier CONSTRUCTION #####

def get_playable_squares(board):
	playable_squares = []
	for i in range(board.num_rows):
		for j in range(board.num_cols):
			if board.get_square([i,j]) != " ":
				playable_squares.append([i,j])
	return playable_squares


def find_moves(square, board, player):
	moves = []
	basePatternCache = set()
	#Iterate through each side of the tile
	for side in [[1,0],[-1,0,],[0,1],[0,-1]]:
		side_square = [square[0] + side[0], square[1] + side[1]]
		if (board.is_valid_square(side_square) and board.get_square(side_square) == " "):
			if (side[0] == 0):
				containDirection = "Horizontal"
				borderDirection = "Vertical"
			else:
				containDirection = "Vertical"
				borderDirection = "Horizontal"
			#check for containing moves
			#Construct pattern and pass into anagram_checker
			pattern = get_line(side_square, side, board)
			if containDirection == "Horizontal":
				base = side_square[1]
			else:
				base = side_square[0]
			if pattern+str(base) not in basePatternCache:
				additional_moves = anagram_checker(pattern, base, player.get_tiles(), containDirection, side_square, board)
				moves += additional_moves
				basePatternCache.add(pattern+str(base))
			else:
				pass
				#print("Found cached base and pattern, skipping")
			#check for bordering moves
			#Construct pattern and pass into anagram_checker
			pattern = get_line(side_square, side[::-1], board)
			if borderDirection == "Horizontal":
				base = side_square[1]
			else:
				base = side_square[0]
			if pattern+str(base) not in basePatternCache:
				additional_moves = anagram_checker(pattern, base, player.get_tiles(), borderDirection, side_square, board)
				moves += additional_moves
				basePatternCache.add(pattern+str(base))
			else:
				pass
				#print("Found cached base and pattern, skipping")

	return moves

def get_line(square, side, board):
	pattern = board.get_square(square)
	s = [square[0]-abs(side[0]), square[1]-abs(side[1])]
	while (board.is_valid_square(s)):
		pattern = board.get_square(s) + pattern
		s = [s[0]-abs(side[0]), s[1]-abs(side[1])]
	s = [square[0]+abs(side[0]), square[1]+abs(side[1])]
	while (board.is_valid_square(s)):
		pattern = pattern + board.get_square(s)
		s = [s[0]+abs(side[0]), s[1]+abs(side[1])]
	return pattern


def anagram_checker(pattern, base, rack, direction, square, board):
	# 'pattern' is of the form "     i  e      ", is a full row or column of the board
	# 'base' is an index into pattern. Generated words must contain base
	# Checks all possible moves that comply with pattern, and runs is_valid_move
	moves = []
	for i in range(len(rack)):
		for perm in permutations(rack, i+1):
			for pos in range(len(perm)):
				new_pattern, start_pos = fill_pattern(perm, pattern, base, pos)
				while start_pos-1 > -1 and new_pattern[start_pos-1] != " ":
					start_pos -= 1
				#OPTIMIZE BY DOING IN FILL_PATTERN
				if start_pos > -1 and True: #If not anagram extended beyond the page and is invalid
					word = ""
					i = start_pos
					while i < len(pattern) and new_pattern[i] != " ":
						word += new_pattern[i]
						i += 1
					if word in components.dictionary: #Don't both to check if a valid move if the base isn't even a valid word
						if direction == "Vertical":
							start_square = [square[0] + (start_pos - base), square[1]]
						else:
							start_square = [square[0], square[1] + (start_pos - base)]
						score, message = board.is_valid_move(word, start_square, direction, rack)
						if score != -1:
							moves.append({
								"word": word,
								"score": score,
								"square": start_square[:],
								"direction": direction,
								"type": "word"
							})
	return moves

def fill_pattern(perm, pattern, base, pos):
	pattern = list(pattern)
	pattern[base] = perm[pos]
	start_pos = base

	permPos = pos+1
	patPos = base+1
	while permPos < len(perm):
		if patPos >= len(pattern):
			return [], -1
		if pattern[patPos] == " ":
			pattern[patPos] = perm[permPos]
			permPos += 1
		patPos += 1

	permPos = pos-1
	patPos = base-1
	while permPos > -1:
		if patPos < 0:
			return [], -1
		if pattern[patPos] == " ":
			pattern[patPos] = perm[permPos]
			permPos -= 1
			start_pos = patPos
		patPos -= 1

	return ''.join(pattern), start_pos

def choose_move(moves, board, player, turn):
	#Given a list of moves, finds the "best" and returns it. Best is defined through ai crap
	#IMPLEMENT GIVING UP
	if (len(moves)) > 0:
		if player.heuristic == "RAND":
			return moves[random.randint(0, len(moves)-1)]
		elif player.heuristic == "BEST_SCORE":
			bestScore = 0
			for move in moves:
				#print(str_move(move))
				if move["score"] > bestScore:
					bestScore = move["score"]
					bestMove = move
			return bestMove
		elif player.heuristic == "BAYES":
			xTest = learning.construct_test(moves, board, player, turn, True)
			preds = bayesClassifier(xTest)
			return moves[learning.getBest(preds)]
		elif player.heuristic == "NN":
			xTest = learning.construct_test(moves, board, player, turn, False)
			bestMoveIndex = learning.find_best(xTest, nnClassifier)
			return moves[bestMoveIndex]
		elif player.heuristic == "KNN":
			xTest = learning.construct_test(moves, board, player, turn, False)
			bestMoveIndex = learning.find_best(xTest, knnClassifier)
			return moves[bestMoveIndex]
		else:
			return moves[0]
	else:	

		return {"type":"skip"}

def get_AI_move(board, player, turn, screen):
	#print("################################")
	#print(player.rack)
	if board.isEmpty:
		moves = anagram_checker(" "*15, 7, player.rack, "Horizontal", [7,7], board)
	else:
		playable_squares = get_playable_squares(board)
		start = time.clock()
		moves = []
		for i in range(len(playable_squares)):
			screen.update_progress(i, len(playable_squares))
			moves += find_moves(playable_squares[i], board, player)
		# REENABLE FOR DATA COLLECTION WHEN THE SCRAPING IS FIXED
		# elapsed = time.clock() - start
		# with open('moveScrape1.csv', 'a') as f:
		# 	f.write(str(len(playable_squares)) + "," + str(elapsed) + "\n")

	move = choose_move(moves, board, player, turn)
	print(player.name + " PLAYING | " + str_move(move))
	return move 

def str_move(move):
	if move['type'] == "skip":
		return "SKIP"
	return "Word: " + move["word"] + " | Score: " + str(move["score"]) + " | Square: " + str(move["square"]) + " | Direction: " + move["direction"]