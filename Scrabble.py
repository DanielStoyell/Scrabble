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

	def get_next_turn_player(self):
		if self.get_current_turn_player() == self.players[0]:
			return self.players[1]
		else:
			return self.players[0]

	def run_turn(self, word=None, direction=None, square=None):
		player = self.get_current_turn_player()
		opponent = self.get_next_turn_player()
		is_valid, message = self.board.is_valid_move(word, square[:], direction, player.get_tiles())
		if len(player.rack) == 0:
			player.score += opponent.get_rack_score()
			opponent.score -= opponent.get_rack_score()
			print("Game End Sequence Initiated - No tiles left in rack")
			self.state = "end_game"
		elif is_valid >= 0:
			score, letters_used = self.board.play_move(word, square[:], direction, player.get_tiles())
			player.score += score
			self.turn += 1

			#Logic for Rack Update
			for letter in letters_used:
				player.rack.remove(letter)
			
			player.rack = player.rack + self.bag.draw_tiles(7 - len(player.rack))
			print(self.bag.get_len_bag())
		else:
			print("Invalid move - trying again!")
			self.state = "ERROR"
			self.message = message

	def end_game(self):
		player = self.get_current_turn_player()
		opponent = self.get_next_turn_player()
		opponent.score += player.get_rack_score()
		player.score -= player.get_rack_score()
		print("Game End Sequence Initiated")
		self.state = "end_game"
		if player.score > opponent.score:
			self.message = player.get_name() + " won the game! " + str(player.score) + " to " + str(opponent.score)
		elif player.score < opponent.score:
			self.message = opponent.get_name() + " won the game! " + str(opponent.score) + " to " + str(player.score)
		else:
			self.message = "It was a tie! " + str(player.score) + " to " + str(opponent.score)
	
player1 = ["PLAYER_1", False]
player2 = ["PLAYER_2", False]

print("Starting game....")

main = Game(player1, player2)

print("Game ending....")

