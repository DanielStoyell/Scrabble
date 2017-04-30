''' Stores the classes for Player, Board, Bag, and Game
### TODO ###
	1. Implement Bag
	2. Implement Board
	3. Implement Player
'''

import random

#### GENERAL GAME DATA ####

dictFile = open("dictionary.txt", "r")
dictionary = set()
for line in dictFile:
	dictionary.add(line.strip())
dictFile.close()

letter_values = {
	"a": 1,
	"b": 3,
	"c": 3,
	"d": 2,
	"e": 1,
	"f": 4,
	"g": 2,
	"h": 4,
	"i": 1,
	"j": 8,
	"k": 5,
	"l": 1,
	"m": 3,
	"n": 1,
	"o": 1,
	"p": 3,
	"q": 10,
	"r": 1,
	"s": 1,
	"t": 1,
	"u": 1,
	"v": 4,
	"w": 4,
	"x": 8,
	"y": 4,
	"z": 10,
	"?": 0
}

modifiers = [['TW','  ','  ','DL','  ','  ','  ','TW','  ','  ','  ','DL','  ','  ','TW'],
			 ['  ','DW','  ','  ','  ','TL','  ','  ','  ','TL','  ','  ','  ','DW','  '],
			 ['  ','  ','DW','  ','  ','  ','DL','  ','DL','  ','  ','  ','DW','  ','  '],
			 ['DL','  ','  ','DW','  ','  ','  ','DL','  ','  ','  ','DW','  ','  ','DL'],
			 ['  ','  ','  ','  ','DW','  ','  ','  ','  ','  ','DW','  ','  ','  ','  '],
			 ['  ','TL','  ','  ','  ','TL','  ','  ','  ','TL','  ','  ','  ','TL','  '],
			 ['  ','  ','DL','  ','  ','  ','DL','  ','DL','  ','  ','  ','DL','  ','  '],
			 ['TW','  ','  ','DL','  ','  ','  ','DW','  ','  ','  ','DL','  ','  ','TW'],
			 ['  ','  ','DL','  ','  ','  ','DL','  ','DL','  ','  ','  ','DL','  ','  '],
			 ['  ','TL','  ','  ','  ','TL','  ','  ','  ','TL','  ','  ','  ','TL','  '],
			 ['  ','  ','  ','  ','DW','  ','  ','  ','  ','  ','DW','  ','  ','  ','  '],
			 ['DL','  ','  ','DW','  ','  ','  ','DL','  ','  ','  ','DW','  ','  ','DL'],
			 ['  ','  ','DW','  ','  ','  ','DL','  ','DL','  ','  ','  ','DW','  ','  '],
			 ['  ','DW','  ','  ','  ','TL','  ','  ','  ','TL','  ','  ','  ','DW','  '],
			 ['TW','  ','  ','DL','  ','  ','  ','TW','  ','  ','  ','DL','  ','  ','TW'],]

modifier_colors = {
	"TW": "#F26243",
	"DW": "#FDBAA9",
	"TL": "#3FA0BB",
	"DL": "#BDDAD5",
	"  ": "#CEC5A8",
}

def get_letter_value(self, letter):
	return letter_values[letter]

class Player:
	def __init__(self, name, start_tiles, ai):
		self.score = 0
		self.name = name
		self.rack = start_tiles
		self.ai = ai

	def get_score(self):
		return self.score

	def is_ai(self):
		return self.ai

	def get_name(self):
		return self.name

	def get_tiles(self):
		return self.rack

	def get_tile_rep(self):
		output = ""
		delim = ""
		for tile in self.rack:
			output += delim + tile
			delim = ", "
		return output

	def find_move(self, board):
		if self.ai:
			# Fancy machine learning and artificial intelligence goes here
			print("I am a robot and I am finding a move")
			return (False, False, False)
		else:
			# Stupid old human decision-making goes here
			print("Grab human move data and return human move....")
			return (False, False, False)

class Board:
	def __init__(self):
		self.board = [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
					  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
					  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
					  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
					  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
					  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
					  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
					  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
					  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
					  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
					  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
					  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
					  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
					  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
					  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]

	def set_square(self, square, letter):
		self.board[square[0]][square[1]] = letter

	def get_square(self, square):
		return self.board[square[0]][square[1]]

	def play_move(self, word, start_square, direction):
		current_square = start_square
		letters_used = []
		for i in range(len(word)):
			if self.get_square(current_square) == " ":
				self.set_square(current_square, word[i])
				letters_used.append(word[i])
			if direction == "Vertical":
				current_square[0] += 1
			else:
				current_square[1] += 1
		return 10, letters_used

	def is_valid_move(self, word, direction, square):
		return True, "Invalid move! Try again!"
		# if not self.is_valid_square(current_square):
		# 	return (False, "Invalid square (outside boundaries of board)")
		# elif self.get_square(current_square) != letter:
		# 	return (False, "Tiles already placed that are not compatible with word")

		# return (True, score)

	def is_valid_square(self, square):
		return square[0] >= 0 and square[1] >=0 and square[0] <= 14 and square[1] <= 14

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
		random.shuffle(self.bag)

	def draw_tiles(self, n):
		drawn = self.bag[-n:]
		self.bag = self.bag[:-n]
		return drawn