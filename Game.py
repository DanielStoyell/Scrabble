import components as comps

class Game:
	''' Initializer for game of scrabble
		### TODO ###
		1. Init players 1 and 2
		2. Init board
	'''
	def __init__(self, player0info, player1info):
		self.bag = comps.Bag()
		self.board = comps.Board()

		# Define both players and store in player array (somewhat generalizable to >2 players but for now just 2)
		player0 = comps.Player(player0info[0], [], player0info[2])
		player1 = comps.Player(player1info[0], [], player1info[2])
		self.players = [player1, player2]

		# Figure out who is going first
		self.current_turn = 0 if random.random() > .5 else 1
