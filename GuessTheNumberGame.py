# This is a guess the number game.

import random

print('Hello. What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1, 20) # Assignment statement

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7): # For loop.
	print('Take a guess.')
	guess = int(input()) # Call the input function, store in a variable called 
	                     # guess, and convert the input to an int.
	if guess < secretNumber:
		print('Your guess is too low.')
	elif guess > secretNumber:
		print('Your guess is too high.')
	else:
		break # This condition is for the correct guess!

if guess == secretNumber:
	print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
	print('Nope, the number I was thinking of was ' + str(secretNumber)) # Convert to str.
