''' Stores the classes for Player, Board, and Bag
### TODO ###
	1. Implement Bag
	2. Implement Board
	3. Implement Player
'''

import random

class gameData
	letter_values = {
		"a": 1,
		"b": 1,
		"c": 1,
		"d": 1,
		"e": 1,
		"f": 1,
		"g": 1,
		"h": 1,
		"i": 1,
		"j": 1,
		"k": 1,
		"l": 1,
		"m": 1,
		"n": 1,
		"o": 1,
		"p": 1,
		"q": 1,
		"r": 1,
		"s": 1,
		"t": 1,
		"u": 1,
		"v": 1,
		"w": 1,
		"x": 1,
		"y": 1,
		"z": 1
	}

	def get_letter_value(self, letter):
		return letter_values[letter]

class Player:
	def __init__(self, name, start_tiles, is_ai):
		self.score = 0
		self.name = name
		self.rack = start_tiles
		self.is_ai = is_ai

	def get_score(self):
		return self.score

	def is_ai(self):
		return self.is_ai

	def get_name(self):
		return self.name

	def find_move(self, board):
		if self.is_ai:
			# Fancy machine learning and artificial intelligence goes here
			pass
		else:
			# Stupid old human decision-making goes here
			pass

class Board:
	def __init__(self):
		self.board = [['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
					  ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
					  ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
					  ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
					  ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
					  ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
					  ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
					  ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
					  ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
					  ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
					  ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
					  ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
					  ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
					  ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
					  ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_']]
		self.modifiers = [['TW','__','__','__','__','__','__','TW','__','__','__','__','__','__','TW'],
						  ['__','DW','__','__','__','__','__','__','__','__','__','__','__','DW','__'],
						  ['__','__','DW','__','__','__','__','__','__','__','__','__','DW','__','__'],
						  ['__','__','__','DW','__','__','__','__','__','__','__','DW','__','__','__'],
						  ['__','__','__','__','DW','__','__','__','__','__','DW','__','__','__','__'],
						  ['__','__','__','__','__','__','__','__','__','__','__','__','__','__','__'],
						  ['__','__','__','__','__','__','__','__','__','__','__','__','__','__','__'],
						  ['TW','__','__','__','__','__','__','DW','__','__','__','__','__','__','TW'],
						  ['__','__','__','__','__','__','__','__','__','__','__','__','__','__','__'],
						  ['__','__','__','__','__','__','__','__','__','__','__','__','__','__','__'],
						  ['__','__','__','__','DW','__','__','__','__','__','DW','__','__','__','__'],
						  ['__','__','__','DW','__','__','__','__','__','__','__','DW','__','__','__'],
						  ['__','__','DW','__','__','__','__','__','__','__','__','__','DW','__','__'],
						  ['__','DW','__','__','__','__','__','__','__','__','__','__','__','DW','__'],
						  ['TW','__','__','__','__','__','__','TW','__','__','__','__','__','__','TW'],]

	def set_square(self, square, letter):
		if self.board[square[0]][square[1]] == '_':
			self.board[square[0]][square[1]] = letter
			return True
		else:
			return False

	def get_square(self, square):
		return self.board[square[0]][square[1]]

	def get_square_modifier(self, square):
		return self.modifiers[square[0]][square[1]]

	def play_move(self, word, start_square, direction, dictionary):
		is_valid = self.is_valid_move(word, start_square, direction, dictionary)
		if not is_valid[0]:
			return is_valid
		score = 0
		multiplier = 1
		current_square = start_square
		for letter in word.split():
			if self.get_square(current_square) = "_":
				mod = self.get_square_modifier(current_square)
				if mod[1] == "L":
					score += gameData.get_letter_value(letter) * int(mod[0])
				elif mod[1] == "W":
					multiplier *= int(mod[0])
				else:
					score += gameData.get_letter_value(letter)
			elif self.get_square(current_square) == letter:
				score += gameData.get_letter_value(letter)
			else:
				return (False, "You fucked up")
		return (True, score*multiplier)

	def is_valid_move(self, word, start_square, dictionary):
		if not self.is_valid_square(current_square):
			return (False, "Invalid square (outside boundaries of board)")
		elif self.get_square(current_square) != letter:
			return (False, "Tiles already placed that are not compatible with word")



		return (True, score)

	def is_valid_square(self, square):
		return square[0] >= 0 and square[1] >=0 and square[0] <= 15 and square[1] <= 15

class Bag:
	def __init__(self):
		self.bag = ['J','K','Q','X','Z'] * 1 \
			+  ['?','B','C','F','H','M','P','V','W','Y'] * 2 \
			+  ['G'] * 3 \
			+  ['D','L','S','U'] * 4 \
			+  ['N','R','T'] * 6 \
			+  ['O'] * 8 \
			+  ['A','I'] * 9 \
			+  ['E'] * 12
		random.shuffle(bag)

	def draw_tiles(self, n):
		drawn = self.bag[-n:]
		self.bag = self.bag[:-n]
		return drawn