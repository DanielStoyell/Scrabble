import random

from Tkinter import *
from bag import get_bag, create_rack

TURN = 1

root = Tk()

#Create the Title of the Game
title = Label(master = root, text = "Scrabble!", height = 4, width = 18, bg = "red", fg = "white")
title.grid(row = 0, column = 0, sticky = N+W)
title.config(font = ("Lucida", 21))


#Create the Board
w1 = Frame(master = root, bg = "papaya whip")
w1.grid(row = 0, column = 50, rowspan = 200, columnspan= 400, sticky = E)
states = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

b = 	[ [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] ]

for i in range(15):
	for j in range(15):
		
		def handlebuttonpress(i,j):
			coordinates = '({0},{1})'.format(i,j)
			coordinateLabel = Label(master = root, text = coordinates, height = 1, width = 3, fg = "black" )
			coordinateLabel.grid(row = 3, column = 0, sticky = E + W )
		
		b[i][j] = Button(w1, height = 1, width = 1, command = lambda i = i, j = j: handlebuttonpress(i,j), bg = "papaya whip")
		b[i][j].grid(row = i, column = j)

#Create the rack for the player
bag = get_bag()
rack = ""
new_rack = create_rack(rack, bag)

rack = Label(master = root, text = "rack: " + new_rack, height = 2, width = 18, fg = "black")
rack.grid(row = 1, column = 0, sticky = W+E)
rack.config (font = ("Lucida", 18))

#Start Tile Selection Label 
#The coordinates are found in the board logic.
buttontext = Label(master = root, text = "Start Tile: ", height = 1, width = 8, fg = "black")
buttontext.grid(row = 2, column = 0, sticky = W)

#Word Entry Label and Entry
entrylabel = Label(master = root, text = "Your Word: ", height = 1, width = 9, fg = "black" )
entrylabel.grid(row = 4, column = 0, sticky = W)
e1 = Entry(master = root, width = 30)
e1.grid(row = 4, column = 0, sticky = E)

#Horizontal/Vertical Check Label and Button
checklabel = Label(master = root, text = "Word Alignment: ", height = 1, width = 13, fg = "black" )
checklabel.grid(row = 5, column = 0, sticky = W)
horizontal = Checkbutton(master = root, text = "horizontal", width = 25)
horizontal.grid(row = 5, column = 0, sticky = E)
vertical = Checkbutton(master = root, text = "vertical", width = 27)
vertical.grid(row = 6, column = 0, sticky = E)

#Turn Label of Game
turnlabel = Label(master= root, text = "Turn: " + str(TURN), height = 2, width = 6, fg = "black")
turnlabel.grid(row = 199, column = 0, sticky = W)

#Enter Button 
enter = Button (master = root, text = "Enter", height = 2, width = 18, bg = "chartreuse2", fg = "white")
enter.grid(row = 11, column = 0, sticky = E + W)


#Runs actual game
root.mainloop()