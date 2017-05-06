import components

"""
Example move:
move = {
	"word": "banana"
	"score": 26
	"square": [4,5]
	"direction": "Vertical"
}

"""

class AI:
	def get_playable_squares(self, board):
		playable_squares = []
		for i in range(len(board)):
			for j in range(len(board[i])):
				if board.get_square([i,j]) != " ":
					playable_squares.append([i,j])
		return playable_squares


	def find_moves(self, square, board, player):
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

	def anagram_checker(self, pattern, base, rack, board):
		# 'pattern' is of the form "_____i__e______", is a full row or column of the board
		# 'base' is an index into pattern. Generatd words must contain base
		# Checks all possible moves that comply with pattern, and runs is_valid_move
		return []

	def choose_move(self, moves, board, player):
		return {}

	def get_AI_move(self, board, player):
		playable_squares = get_playable_squares(board)
		moves = []
		for square in playable_squares:
			moves += find_moves(square, board, player)

		return choose_move(moves, board, player)