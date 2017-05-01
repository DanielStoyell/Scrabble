import graphics
import random
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
		self.message = ""
		self.state = "human_turn"

		# Define both players and store in player array (somewhat generalizable to >2 players but for now just 2)
		player1 = components.Player(player0info[0], self.bag.draw_tiles(7), player0info[1])
		player2 = components.Player(player1info[0], self.bag.draw_tiles(7), player1info[1])
		self.players = [player1, player2]
		self.screen = graphics.Screen(self)
		if self.get_current_turn_player().is_ai():
			self.state = "ai_turn"
		else:
			self.state = "human_turn"

	def get_current_turn_player(self):
		return self.players[self.turn % 2]

	def run_turn(self, word=None, direction=None, square=None):
		player = self.get_current_turn_player()
		is_valid, message = self.board.is_valid_move(word, direction, square)
		if is_valid:
			score, letters_used = self.board.play_move(word, square, direction)
			player.score += score
			self.turn += 1

			#Logic for Rack Update
			print(letters_used)
			print(player.rack)
			i = 0
			while i < len(letters_used):
				player.rack.remove(letters_used[i])
				i = i + 1
			print(player.rack)

			lengthbag = self.bag.get_len_bag()
			print(lengthbag)
			
			if lengthbag == 0:
				player.rack = player.rack
			else:
				player.rack = player.rack + self.bag.draw_tiles(7 - len(player.rack))
				print(player.rack)
			
			lengthbag = self.bag.get_len_bag()
			print(lengthbag)
			
		else:
			print("Invalid move - trying again!")
			self.state = "ERROR"
			self.message = message

player1 = ["PLAYER_1", False]
player2 = ["PLAYER_2", False]

print("Starting game....")

main = Game(player1, player2)

print("Game ending....")
