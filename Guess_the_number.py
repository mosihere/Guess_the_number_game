# This is a guess the number game.

import random
print('Hello, What is your name?')
name = input()
print('Well',name,'I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1,20)

# Ask user to guess 6 times !
for guesesTaken in range(1,7):
    print('Take a guess:')
    guess = int(input())
    if guess > secretNumber:
        print('Your guess is too high!')
    elif guess < secretNumber:
        print('Your guess is too low!')
    else:
        break # This condition if for the correct Answer

if guess == secretNumber:
    print('Good job',name,'! You guessed my number in',guesesTaken,'times!')

else:
    print('Nope. The Number I was thinking of was',secretNumber)