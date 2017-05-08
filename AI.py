import components

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
			#check for containing moves
			#Construct pattern and pass into anagram_checker
			pass
			#check for bordering moves
			#Construct pattern and pass into anagram_checker
			pass
	return moves

def anagram_checker(pattern, base, rack, board):
	# 'pattern' is of the form "_____i__e______", is a full row or column of the board
	# 'base' is an index into pattern. Generated words must contain base
	# Checks all possible moves that comply with pattern, and runs is_valid_move
	return []

def choose_move(moves, board, player):
	#Given a list of moves, finds the "best" and returns it. Best is defined through ai crap
	return {}

def get_AI_move(board, player):
	playable_squares = get_playable_squares(board)
	moves = []
	for square in playable_squares:
		moves += find_moves(square, board, player)

	move = choose_move(moves, board, player)
	return {"type": "skip"} #SOOO SMART