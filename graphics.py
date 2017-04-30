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

		#Create player data on top
		self.playerData = Label(master = self.root, text = "Player data", height = 2, width=30, fg="black")
		self.playerData.grid(row=1, column=0, sticky = W)

		#Create the Board
		w1 = Frame(master = self.root, bg = "papaya whip")
		w1.grid(row = 0, column = 50, rowspan = 200, columnspan= 400, sticky = E)

		#Start Tile Selection Label 
		#The coordinates are found in the board logic.
		self.start_tile_text = Label(master = self.root, text = "Start Tile: ", height = 1, width = 16, fg = "black")
		self.start_tile_text.grid(row = 3, column = 0, sticky = W)

		self.buttons = []
		self.start_tile = []

		for i in range(15):
			self.buttons.append([])
			for j in range(15):
				def handlebuttonpress(i,j):
					self.start_tile = [i,j]
					coordinates = '({0},{1})'.format(i,j)
					self.start_tile_text["text"] = "Start Tile: " + coordinates
				
				self.buttons[i].append(Button(w1, fg="black", height = 2, width = 4, command = (lambda i = i, j = j: handlebuttonpress(i,j)), bg = "papaya whip"))
				self.buttons[i][j].grid(row = i, column = j)

		self.rack = Label(master = self.root, text = "rack: " + Game.players[0].get_tile_rep(), height = 2, width = 18, fg = "black")
		self.rack.grid(row = 2, column = 0, sticky = W+E)
		self.rack.config (font = ("Lucida", 18))

		#Word Entry Label and Entry
		self.entrylabel = Label(master = self.root, text = "Your Word: ", height = 1, width = 9, fg = "black" )
		self.entrylabel.grid(row = 5, column = 0, sticky = W)
		self.entryTextbox = Entry(master = self.root, width = 30)
		self.entryTextbox.grid(row = 5, column = 0, sticky = E)

		#Horizontal/Vertical Check Label and Button
		self.direction = "Horizontal"
		def directionToggle():
			if self.direction == "Horizontal":
				self.direction = "Vertical"
			else:
				self.direction = "Horizontal"
			self.alignmentToggle["text"] = self.direction
		self.alignmentLabel = Label(master = self.root, text = "Word Alignment: ", height = 1, width = 13, fg = "black" )
		self.alignmentLabel.grid(row = 6, column = 0, sticky = W)
		self.alignmentToggle = Button(master=self.root, text="Horizontal", width=20, height=2, command=directionToggle)
		self.alignmentToggle.grid(row=6,column=0,sticky=E)

		#Turn Label of Game
		self.turnlabel = Label(master= self.root, text = "Turn: " + str(Game.turn), height = 2, width = 6, fg = "black")
		self.turnlabel.grid(row = 199, column = 0, sticky = W)

		#Enter Button 
		self.enter = Button(master = self.root, text = "Enter", height = 2, width = 18, bg = "chartreuse2", fg = "white", command=(lambda: self.enter_move(Game)))
		self.enter.grid(row = 12, column = 0, sticky = E + W)

		#Error message data
		self.errorMessage = Label(master = self.root, text = "Invaid move!", height = 2, width=30, fg="black")
		self.errorMessage.grid(row=1, column=0, sticky = W)
		self.errorMessage.grid_remove()

		self.errorButton = Button(master=self.root, text="OK", width=10, height=2, command=lambda : self.confirm_error(Game))
		self.errorButton.grid(row=6,column=0,sticky=W)
		self.errorButton.grid_remove()

		#render initial board
		self.update(Game)

		#Runs actual game
		self.root.mainloop()

	# Someone clicked the enter button. Should quickly pass along available data to main Scrabble.py functions for processing
	def enter_move(self, Game):
		print("Entering move")
		Game.run_turn(self.entryTextbox.get(), self.direction, self.start_tile)
		self.update(Game)

	def confirm_error(self, Game):
		print("confirm error")
		Game.state = "human_turn"
		self.update(Game)

	# Re-renders board
	def update(self, Game):
		for i in range(15):
			for j in range(15):
				square_tile = Game.board.get_square([i,j])
				if square_tile != " ":
					self.buttons[i][j]["text"] = square_tile
					self.buttons[i][j]["bg"] = "#ffe493"
					self.buttons[i][j]["fg"] = "black"
					self.buttons[i][j]["font"] = font.Font(family="Helvetica", size="10", weight="bold")
				else:
					self.buttons[i][j]["text"] = components.modifiers[i][j]
					self.buttons[i][j]["bg"] = components.modifier_colors[components.modifiers[i][j]]
					self.buttons[i][j]["fg"] = "white"
					self.buttons[i][j]["font"] = font.Font(family="Helvetica", size="10")
		
		self.playerData["text"] = Game.players[0].get_name() + ": " + str(Game.players[0].get_score()) \
									+ "      " + Game.players[1].get_name() + ": " + str(Game.players[1].get_score()) \
									+ "\nCurrent Turn: " + Game.get_current_turn_player().get_name()

		if Game.state == "ai_turn":
			#Remove human move prompts
			self.start_tile_text.grid_remove()
			self.rack.grid_remove()
			self.enter.grid_remove()
			self.entrylabel.grid_remove()
			self.entryTextbox.grid_remove()
			self.alignmentLabel.grid_remove()
			self.alignmentToggle.grid_remove()
			self.errorButton.grid_remove()
			self.errorMessage.grid_remove()
		elif Game.state == "human_turn":
			self.errorButton.grid_remove()
			self.errorMessage.grid_remove()
			#Add back human prompts
			self.start_tile_text.grid()
			self.rack.grid()
			self.enter.grid()
			self.entrylabel.grid()
			self.entryTextbox.grid()
			self.alignmentLabel.grid()
			self.alignmentToggle.grid()
			#Create AI waiting screen?
		else:
			self.start_tile_text.grid_remove()
			self.rack.grid_remove()
			self.enter.grid_remove()
			self.entrylabel.grid_remove()
			self.entryTextbox.grid_remove()
			self.alignmentLabel.grid_remove()
			self.alignmentToggle.grid_remove()
			#Add AI crap
			self.errorMessage["text"] = Game.message
			self.errorButton.grid()
			self.errorMessage.grid()