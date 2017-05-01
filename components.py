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
	"A": 1,
	"B": 3,
	"C": 3,
	"D": 2,
	"E": 1,
	"F": 4,
	"G": 2,
	"H": 4,
	"I": 1,
	"J": 8,
	"K": 5,
	"L": 1,
	"M": 3,
	"N": 1,
	"O": 1,
	"P": 3,
	"Q": 10,
	"R": 1,
	"S": 1,
	"T": 1,
	"U": 1,
	"V": 4,
	"W": 4,
	"X": 8,
	"Y": 4,
	"Z": 10,
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

	def play_move(self, word, start_square, direction, rack):
		score, message = self.is_valid_move(word, start_square[:], direction, rack)
		if score == -1:
			return -1, []
		current_square = start_square
		letters_used = []
		for i in range(len(word)):
			if self.get_square(current_square) == " ":
				self.set_square(current_square, word[i].upper())
				letters_used.append(word[i])
			if direction == "Vertical":
				current_square[0] += 1
			else:
				current_square[1] += 1
		return score, letters_used

	def is_valid_move(self, word, square, direction, rack):
		#Returns the number of points, and a message about the move.
		# -1 if move is invalid, and the message is why
		# direction reassign for effiency
		if direction == "Vertical":
			direction = True
		else:
			direction = False
		current_square = square
		score = 0
		word_multiplier = 1
		rack = rack[:] #might convert to alt form eventually

		if word not in dictionary:
			return -1, word + " not in dictionary"

		for i in range(len(word)):
			if not self.is_valid_square(square):
				return -1, "Out of board bounds"
			if self.get_square(current_square) == " ":
				try:
					print(str(rack))
					print(word[i])
					rack.remove(word[i])
				except:
					return -1, "Letter used that is not in rack"
				modifier = modifiers[square[0]][square[1]]
				square_multiplier = 1
				if modifier != "  ":
					square_multiplier = 2 if modifier[0] == "D" else 3
					if modifier[1] == "W":
						word_multiplier *= square_multiplier
						score += letter_values[word[i]]
					else:
						score += letter_values[word[i]]*square_multiplier
				else:
					score += letter_values[word[i]]
				#TODO: CHECK FOR BRANCHING WORDS
				if direction:
					border_right = [current_square[0], current_square[1]+1]
					border_left = [current_square[0], current_square[1]-1]
					if self.get_square(border_left) != " " or self.get_square(border_right) != " ":
						branch_score, branch_word = self.get_branch_word_score(current_square, not direction, word[i])
						if branch_score == -1:
							return -1, branch_word + " is not a valid word"
						else:
							score += branch_score
				else:
					border_bottom = [current_square[0]+1, current_square[1]]
					border_top = [current_square[0]-1, current_square[1]]
					if self.get_square(border_top) != " " or self.get_square(border_bottom) != " ":
						branch_score, branch_word = self.get_branch_word_score(current_square, not direction, word[i])
						if branch_score == -1:
							return -1, branch_word + " is not a valid word"
						else:
							score += branch_score
			else:
				if self.get_square(current_square) == word[i]:
					score += letter_values[word[i]]
				else:
					return -1, "Letter exists on move space that is not aligned with word"

			if direction:
				current_square[0] += 1
			else:
				current_square[1] += 1

		return score*word_multiplier, "Valid move"

	def get_branch_word_score(self, square, direction, letter):
		#Only guarantee about passed in square is that the word contains it
		#This is ugly af I know
		word = letter
		score = letter_values[letter]
		mult = 1
		modifier = modifiers[square[0]][square[1]]
		if modifier != "  ":
			if modifier[1] == "L":
				score *= 2 if modifier[0] == "D" else 3
			else:
				mult = 2 if modifier[0] == "D" else 3
		p = square[:]
		if direction:
			p[0] += 1
			while self.get_square(p) != " ":
				letter =  self.get_square(p)
				word = word + letter
				score += letter_values[letter]
				p[0] += 1
			p[0] = square[0]-1
			while self.get_square(p) != " ":
				letter =  self.get_square(p)
				word = letter + word
				score += letter_values[letter]
				p[0] -= 1
		else:
			p[1] += 1
			while self.get_square(p) != " ":
				letter =  self.get_square(p)
				word = word + letter
				score += letter_values[letter]
				p[1] += 1
			p[1] = square[1]-1
			while self.get_square(p) != " ":
				letter =  self.get_square(p)
				word = letter + word
				score += letter_values[letter]
				p[1] -= 1
		print(word)
		print(score*mult)
		if word not in dictionary:
			return -1, word
		return score*mult, word

	def is_valid_square(self, square):
		return square[0] >= 0 and square[1] >=0 and square[0] <= 14 and square[1] <= 14

class Bag:
	def __init__(self):
		self.bag = ['J','K','Q','X','Z'] * 1 \
			+  ['B','C','F','H','M','P','V','W','Y'] * 2 \
			+  ['G'] * 3 \
			+  ['D','L','S','U'] * 4 \
			+  ['N','R','T'] * 6 \
			+  ['O'] * 8 \
			+  ['A','I'] * 9 \
			+  ['E'] * 12
		random.shuffle(self.bag)

	def get_len_bag(self):
		return len(self.bag)

	def draw_tiles(self, n):
		n = min(len(self.bag), n)
		if n == 0:
			return []
		else:
			drawn = self.bag[-n:]
			self.bag = self.bag[:-n]
			return drawn
