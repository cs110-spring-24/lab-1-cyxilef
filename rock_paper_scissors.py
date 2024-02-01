
#- Generate a random number between 1 and 3 for the computer's choice, where 1 represents Rock, 2 represents Paper, and 3 represents Scissors
#- Store this number in a variable called `cpu`
#- Ask the user for their input next, store this value in a variable called `user`
#- Check what the user chose
#- Given what the user chose, check what the computer chose
#- Print out the result of the game
#- Use nested conditional statements to check for multiple conditions at the same time.

import random
cpu = random.randint(1,3)
user = input("Enter rock, paper, or scissors: ")
if user == "rock":
	if cpu == 1: # cpu chose rock
		print("Tie game")
	elif cpu == 2: #cpu chose paper
		print("You lost")
	else: # cpu chose scissors
		print("You win")
if user == "paper":
	if cpu == 1: # cpu chose rock
		print("Tie game")
	elif cpu == 2: #cpu chose paper
		print("You lost")
	else: # cpu chose scissors
		print("You win")
if user == "scissors":
	if cpu == 1: # cpu chose rock
		print("Tie game")
	elif cpu == 2: #cpu chose paper
		print("You lost")
	else: # cpu chose scissors
		print("You win")




