import graphics
import random
import components
import AI
import sys 

current = open("currentgamedata.txt", "w+")

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
		self.last_skipped = False 

		# Define both players and store in player array (somewhat generalizable to >2 players but for now just 2)
		player1 = components.Player(player0info[0], self.bag.draw_tiles(7), player0info[1])
		player2 = components.Player(player1info[0], self.bag.draw_tiles(7), player1info[1])
		self.players = [player1, player2]
		self.screen = graphics.Screen(self)
		if self.get_current_turn_player().is_ai():
			self.state = "ai_turn"
			self.run_turn("ai_turn")
		else:
			self.state = "human_turn"
		self.screen.root.mainloop()

	def get_current_turn_player(self):
		return self.players[(self.turn-1) % 2]

	def get_next_turn_player(self):
		if self.get_current_turn_player() == self.players[0]:
			return self.players[1]
		else:
			return self.players[0]

	def run_turn(self, state, word=None, direction=None, square=None):
		player = self.get_current_turn_player()
		opponent = self.get_next_turn_player()
		if state == "human_turn":
			is_valid, message = self.board.is_valid_move(word, square[:], direction, player.get_tiles())
			if is_valid >= 0:
				score, letters_used = self.board.play_move(word, square[:], direction, player.get_tiles())
				player.score += score
				self.turn += 1
				#Writing Data to File
				current = open("currentgamedata.txt", "a+")
				print(player.get_name())
				line = str(player.get_name()) + ";" + str(self.turn) + ";" + word + \
					       ";" + str(len(word)) + ";" + ''.join(player.rack) + \
					       ";" + ''.join(letters_used) + ";" + direction + ";" + str(square) + \
				           ";" + str(player.score) + "\n"
				current.write(line)
				current.close()
				#Logic for Rack Update
				for letter in letters_used:
					player.rack.remove(letter)
				
				player.rack = player.rack + self.bag.draw_tiles(7 - len(player.rack))
			else:
				print("Invalid move - trying again!")
				self.state = "ERROR"
				self.message = message
				return
		elif state == "ai_turn":
			print("AI choosing move")
			ai_move = AI.get_AI_move(self.board, player, self.turn)
			if ai_move["type"] == "word":
				score, letters_used = self.board.play_move(ai_move["word"], ai_move["square"], ai_move["direction"], player.get_tiles())
				if score > -1:
					player.score += score
					print(letters_used)
					#Writing Data to File
					current = open("currentgamedata.txt", "a+")
					print(player.get_name())
					line = str(player.get_name()) + ";" + str(self.turn) + ";" + ai_move["word"] + \
					       ";" + str(len(ai_move["word"])) + ";" + ''.join(player.rack) + \
					       ";" + ''.join(letters_used) + ";" + ai_move["direction"] + ";" + str(ai_move["square"]) + \
				           ";" + str(player.score) + "\n"
					current.write(line)
					current.close()
					#Pick new tiles
					for letter in letters_used:
						player.rack.remove(letter)
					player.rack = player.rack + self.bag.draw_tiles(7 - len(player.rack))
				else:
					print("The ai fucked up")
			else:
				print("AI chose to skip")
				print(self.last_skipped)

				#Skip Logic
				if self.last_skipped == False:
					self.last_skipped = True
				else:
					self.end_game()
					self.screen.restart_game(self)
				
			self.turn += 1
		
		if opponent.is_ai():
			if len(player.rack) == 0:
				self.end_game()
				print("Game End Sequence Initiated - No tiles left in rack")
				self.screen.restart_game(self)
			else:
				self.state = "ai_turn"
				self.screen.update(self)
				self.run_turn("ai_turn")
		else:
			if len(player.rack) == 0 | self.last_skipped == True:
				self.end_game()
				print("Game End Sequence Initiated - No tiles left in rack")
				self.screen.restart_game(self)
			else:
				self.state = "human_turn"
				self.screen.update(self)
				#pass back to ui for human turn
				pass

	def end_game(self):
		player = self.get_current_turn_player()
		opponent = self.get_next_turn_player()
		opponent.score += player.get_rack_score()
		player.score -= player.get_rack_score()
		print("Game End Sequence Initiated")
		self.state = "end_game"
		if player.score > opponent.score:
			self.message = player.get_name() + " won the game! " + str(player.score) + " to " + str(opponent.score)
			#Writing Data to File
			with open("totalgamedata.txt", "a+") as out_file:
				with open("currentgamedata.text", "r") as in_file:
					for line in in_file:
						if str(player.get_name()) in line:
							out_file.write(line.rstrip('\n') + ";1 " + "\n")
						else:
							out_file.write(line.rstrip('\n') + ";-1 " + "\n")
		elif player.score < opponent.score:
			#Message Update
			self.message = opponent.get_name() + " won the game! " + str(opponent.score) + " to " + str(player.score)
			#Writing Data to File
			with open("totalgamedata.txt", "a+") as out_file:
				with open("currentgamedata.txt", "r") as in_file:
					for line in in_file:
						if str(opponent.get_name()) in line:
							out_file.write(line.rstrip('\n') + ";1 " + "\n")
						else:
							out_file.write(line.rstrip('\n') + ";-1 " + "\n")
		else:
			#Message Update
			self.message = "It was a tie! " + str(player.score) + " to " + str(opponent.score)
			#Writing Data to File
			with open("totalgamedata.txt", "a+") as out_file:
				with open("currentgamedata.text", "r") as in_file:
					for line in in_file:
						if str(player.get_name()) in line:
							out_file.write(line.rstrip('\n') + ";-1 " + "\n")
						else:
							out_file.write(line.rstrip('\n') + ";-1 " + "\n")
		self.screen.update(self)
			


types = [True, True]
if len(sys.argv[1:]) == 2:
	for i in [0,1]:
		if sys.argv[i+1].lower() == "ai":
			types[i] = True
		elif sys.argv[i+1].lower() == "human":
			types[i] = False
		else:
			print("Unrecognized player type")
			sys.exit()


player1 = ["PLAYER_1", types[0]]
player2 = ["PLAYER_2", types[1]]

print("Starting game....")

main = Game(player1, player2)

print("Game ending....")



