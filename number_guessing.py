import random


number = random.randrange(1,50)
guess = int(input("Guess a Number Between 1 and 50: "))

while guess!= number:
	if guess < number:
		print("You Need To Guess Higher. Try Again")
		guess = int(input("Guess a Number Between 1 and 50: "))
	else:
		print("You Need To Guess Lower. Try Again")
		guess = int(input("Guess a Number Between 1 and 50: "))

print("You Guessed the number correctly!")
input()




