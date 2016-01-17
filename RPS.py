#ROCK PAPER SCISSORS:
#Rock = 1
#Paper = 2
#Scissors = 3
import random
import time

use_choice = ""
comp_choice = ""
agninp = ""
use_win = 0
comp_win = 0
draws = 0
again = 1
winner = 0

def check_choice(inp):
	if inp == "Rock" or inp == "Paper" or inp == "Scissors" or inp == "rock" or inp == "paper" or inp == "scissors" or inp == "r" or inp == "p" or inp == "s" or inp == "R" or inp == "S" or inp == "P":
		return True
	else:
		return False

def conv_choice(ch):
	if ch == "Rock" or ch == "rock" or ch == "r":
		print "Player selects Rock"
		return 1
	elif ch == "Paper" or ch == "paper" or ch == "p":
		print "Player selects Paper"
		return 2
	else:
		print "Player selects Scissors"
		return 3

def detwin(use, comp):
	if use == comp:
		print "It's a draw!"
		return 0
	elif use ==	1 and comp == 2 or use == 2 and comp == 1:
		print "Paper covers rock!"
		if use > comp:
			return 1
		else:
			return 2
	elif use == 1 and comp == 3 or use == 3 and comp == 1:
		print "Rock smashes scissors!"
		if use < comp:
			return 1
		else:
			return 2
	elif use == 2 and comp == 3 or use == 3 and comp == 2:
		print "Scissors cuts paper!"
		if use > comp:
			return 1
		else:
			return 2

print "==============================================================="
print "WELCOME TO ROCK, PAPER, SCISSORS!"
print "==============================================================="		
while again == 1:
	print ""	
	use_choice = raw_input("Please select Rock, Paper, or Scissors:\n")
	while check_choice(use_choice) is False:
		use_choice = raw_input("Error: Please select Rock, Paper, or Scissors:\n")

	useint = conv_choice(use_choice)
	
	compint = random.randrange(1,4)
	time.sleep(1.5)
	if compint == 1:
		print "Computer selects Rock"
	elif compint == 2:
		print "Computer selects Paper"
	else:
		print "Computer selects Scissors"
	time.sleep(1.5)
	
	winner = detwin(useint, compint)
	if winner == 1:
		time.sleep(1.5)
		use_win += 1
		print "You Win!!!"
	elif winner == 2:
		time.sleep(1.5)
		comp_win += 1
		print "Sorry, you lose."
	else:
		draws += 1
	time.sleep(2)
	
	print ""
	print "THE SCORE IS:"
	time.sleep(0.5)
	print "PLAYER: %s" %(use_win)
	time.sleep(0.5)
	print "COMPUTER: %s" %(comp_win)
	time.sleep(0.5)
	print "DRAWS: %s" %(draws)
	time.sleep(1)
	print ""
	
	
	checker = 0
	while checker == 0:
		time.sleep(1)
		agninp = raw_input("Would you like to play again? 'Y' or 'N'\n")
		if agninp == "Yes" or agninp == "yes" or agninp == "Y" or agninp == "y":
			again = 1
			checker = 1
		elif agninp == "No" or agninp == "no" or agninp == "N" or agninp == "n":
			print "Thanks for playing!"
			again = 0
			checker = 1
		else:
			print "Something went wrong, try again"
	

	