import random 

LETTERS = """\
AAAAAAAAAB\
BCCDDDDEEE\
EEEEEEEEEF\
FGGGHHIIII\
IIIIIJKLLL\
LMMNNNNNNO\
OOOOOOOPPQ\
RRRRRRSSSS\
TTTTTTUUUU\
VVWWXYYZ??\
"""

BLANK = "?" 

def get_bag():
	#Returns a list of letters in the bag"
	return list(LETTERS)

def create_rack (curr_letters, bag):
	#Given an existing rack (string) and a bag (list of letters), it creates a
	#rack with a full 7 letters.

	#shuffle the bag
	random.shuffle(bag);

	#see how many letters we need.
	letters_needed = 7 - len(curr_letters)

	#fill up rack 
	curr_letters += "".join(bag[:letters_needed])

	return curr_letters
	