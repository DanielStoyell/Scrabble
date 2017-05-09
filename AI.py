import components
from itertools import permutations

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

def get_playable_squares(board):
	playable_squares = []
	for i in range(board.num_rows):
		for j in range(board.num_cols):
			if board.get_square([i,j]) != " ":
				playable_squares.append([i,j])
	return playable_squares


def find_moves(square, board, player):
	moves = []
	#Iterate through each side of the tile
	for side in [[1,0],[-1,0,],[0,1],[0,-1]]:
		side_square = [square[0] + side[0], square[1] + side[1]]
		if (board.is_valid_square(side_square) and board.get_square(side_square) == " "):
			if (side[0] == 0):
				containDirection = "Vertical"
				borderDirection = "Horizontal"
			else:
				containDirection = "Horizontal"
				borderDirection = "Vertical"
			#check for containing moves
			#Construct pattern and pass into anagram_checker
			pattern, base = get_line(side_square, side, board)
			moves += anagram_checker(pattern, base, player.get_tiles(), containDirection, side_square, board)
			#check for bordering moves
			#Construct pattern and pass into anagram_checker
			pattern, base = get_line(side_square, side[::-1], board)
			moves += anagram_checker(pattern, base, player.get_tiles(), borderDirection, side_square, board)

	return moves

def get_line(square, side, board):
	base = 0
	pattern = board.get_square(square)
	s = [square[0]-abs(side[0]), square[1]-abs(side[1])]
	while (board.is_valid_square(s)):
		pattern = board.get_square(s) + pattern
		base += 1
		s = [s[0]-abs(side[0]), s[1]-abs(side[1])]
	s = [square[0]+abs(side[0]), square[1]+abs(side[1])]
	while (board.is_valid_square(s)):
		pattern = pattern + board.get_square(s)
		s = [s[0]+abs(side[0]), s[1]+abs(side[1])]
	return pattern, base


def anagram_checker(pattern, base, rack, direction, square, board):
	# 'pattern' is of the form "     i  e      ", is a full row or column of the board
	# 'base' is an index into pattern. Generated words must contain base
	# Checks all possible moves that comply with pattern, and runs is_valid_move
	moves = []
	for i in range(len(rack)):
		for perm in permutations(rack, i+1):
			for pos in range(len(perm)):
				new_pattern, start_pos = fill_pattern(perm, pattern, base, pos)
				if start_pos > -1: #If not anagram extended beyond the page and is invalid
					word = ""
					i = start_pos
					while i < len(pattern) and new_pattern[i] != " ":
						word += new_pattern[i]
						i += 1
					if word in components.dictionary: #Don't both to check if a valid move if the base isn't even a valid word
						if direction == "Vertical":
							start_square = [square[0], square[1] + (start_pos - base)]
						else:
							start_square = [square[0] + (start_pos - base), square[1]]
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

def choose_move(moves, board, player):
	#Given a list of moves, finds the "best" and returns it. Best is defined through ai crap
	if (len(moves)) > 1:
		bestScore = 0
		for move in moves:
			if move["score"] > bestScore:
				bestScore = move["score"]
				bestMove = move
		return bestMove
	else:
		return {"type":"skip"}

def get_AI_move(board, player):
	if board.isEmpty:
		moves = anagram_checker(" "*15, 7, player.rack, "Horizontal", [7,7], board)
	else:
		playable_squares = get_playable_squares(board)
		moves = []
		for square in playable_squares:
			moves += find_moves(square, board, player)

	move = choose_move(moves, board, player)
	return move 

def move_rep(move):
	return "Word: " + move["word"] + " | Score: " + str(move["score"]) + " | Square: " + str(move["square"]) + " | Direction: " + move["direction"]