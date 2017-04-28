import graphics
import components

class Game:
	''' Initializer for game of scrabble
		### TODO ###
		1. Init players 1 and 2
		2. Init board
	'''
	def __init__(self, player0info, player1info):
		self.bag = components.Bag()
		self.board = components.Board()
		self.turn = 1

		# Define both players and store in player array (somewhat generalizable to >2 players but for now just 2)
		player0 = components.Player(player0info[0], self.bag.draw_tiles(7), player0info[1])
		player1 = components.Player(player1info[0], self.bag.draw_tiles(7), player1info[1])
		self.players = [player1, player2]
		self.screen = graphics.Screen(self)


player1 = ["PLAYER_1", False]
player2 = ["PLAYER_2", True]

print("Starting game....")

main = Game(player1, player2)

print("Game ending....")
