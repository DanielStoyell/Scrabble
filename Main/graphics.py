import random
import components
from tkinter import font
from tkinter import *

class Screen:
	def __init__(self, Game):
		#Startup view
		self.root = Tk()

		#Create the Title of the Game
		title = Label(master = self.root, text = "Scrabble!", height = 4, width = 18, bg = "red", fg = "white")
		title.grid(row = 0, column = 0, sticky = N+W)
		title.config(font = ("Lucida", 21))

		#Create the Board
		w1 = Frame(master = self.root, bg = "papaya whip")
		w1.grid(row = 0, column = 50, rowspan = 200, columnspan= 400, sticky = E)

		#Start Tile Selection Label 
		#The coordinates are found in the board logic.
		self.start_tile_text = Label(master = self.root, text = "Start Tile: ", height = 1, width = 16, fg = "black")
		self.start_tile_text.grid(row = 2, column = 0, sticky = W)

		self.buttons = []

		for i in range(15):
			self.buttons.append([])
			for j in range(15):
				def handlebuttonpress(i,j):
					coordinates = '({0},{1})'.format(i,j)
					self.start_tile_text["text"] = "Start Tile: " + coordinates
				
				self.buttons[i].append(Button(w1, fg="black", height = 2, width = 4, command = (lambda i = i, j = j: handlebuttonpress(i,j)), bg = "papaya whip"))
				self.buttons[i][j].grid(row = i, column = j)

		self.rack = Label(master = self.root, text = "rack: " + Game.players[0].get_tile_rep(), height = 2, width = 18, fg = "black")
		self.rack.grid(row = 1, column = 0, sticky = W+E)
		self.rack.config (font = ("Lucida", 18))

		#Word Entry Label and Entry
		self.entrylabel = Label(master = self.root, text = "Your Word: ", height = 1, width = 9, fg = "black" )
		self.entrylabel.grid(row = 4, column = 0, sticky = W)
		self.entryTextbox = Entry(master = self.root, width = 30)
		self.entryTextbox.grid(row = 4, column = 0, sticky = E)

		#Horizontal/Vertical Check Label and Button
		self.checklabel = Label(master = self.root, text = "Word Alignment: ", height = 1, width = 13, fg = "black" )
		self.checklabel.grid(row = 5, column = 0, sticky = W)
		self.horizontal = Checkbutton(master = self.root, text = "horizontal", width = 25)
		self.horizontal.grid(row = 5, column = 0, sticky = E)
		self.vertical = Checkbutton(master = self.root, text = "vertical", width = 27)
		self.vertical.grid(row = 6, column = 0, sticky = E)

		#Turn Label of Game
		self.turnlabel = Label(master= self.root, text = "Turn: " + str(Game.turn), height = 2, width = 6, fg = "black")
		self.turnlabel.grid(row = 199, column = 0, sticky = W)

		#Enter Button 
		self.enter = Button (master = self.root, text = "Enter", height = 2, width = 18, bg = "chartreuse2", fg = "white", command=(lambda: self.enter_move(Game)))
		self.enter.grid(row = 11, column = 0, sticky = E + W)

		#render initial board
		self.update(Game)

		#Runs actual game
		self.root.mainloop()

	# Someone clicked the enter button. Should quickly pass along available data to main Scrabble.py functions for processing
	def enter_move(self, Game):
		print("Entering move")
		self.update(Game)

	# Re-renders board
	def update(self, Game):
		for i in range(15):
			for j in range(15):
				square_tile = Game.board.get_square([i,j])
				if square_tile != " ":
					self.buttons[i][j]["text"] = square_tile
					self.buttons[i][j]["bg"] = "#ffe493"
					self.buttons[i][j]["font"] = font.Font(family="Helvetica", size="10", weight="bold")
				else:
					self.buttons[i][j]["text"] = components.modifiers[i][j]
					self.buttons[i][j]["bg"] = components.modifier_colors[components.modifiers[i][j]]
					self.buttons[i][j]["fg"] = "white"
					self.buttons[i][j]["font"] = font.Font(family="Helvetica", size="10")
