__author__ = 'andreas'
from random import randint
secret = randint(1,10)
print("Welcome!")
guess = 0
while guess != secret:
    g = input("Guess the Number")
    guess = int(g)
    if guess == secret:
        print("You win!")
    else:
        if guess > secret:
            print("Your guess is too high")
        else:
            print("Too low")
print("Game over!")
