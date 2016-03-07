# this is a guess the  number game
import random
secretNumber = random.randint(1,20)
print('Guess a number between 1 and 20')

# ask the player to guess 6 times
for guessesTaken in range(1,7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Too low')
    elif guess > secretNumber:
        print('Too high')
    else:
        break # this is the correct guess

if guess == secretNumber:
    print('Well done, you guessed in ' + str(guessesTaken) + ' guesses')
else:
    print('The number was ' + str(secretNumber))
              
              
        
