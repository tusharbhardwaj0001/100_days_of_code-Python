
import random
from art import logo
print(logo)
def numberGuess(chance,number):
  print(f"You have {chance} attempts remaining to guess the number.")
  guess = int(input("Make a guess:"))
  if guess == number :
    print(f"You got it! The answer was {guess}.")
  elif guess > number:
    print("Too high.")
  else :
    print("Too low.")
  print("Guess again")
  return guess

  
print("Welcome to the Number Guessing Game!.")
print("I'm thinking of a number between 1 and 100")
number = random.randint(1,100)
difficulty = input("Choose a difficulty, Type 'easy' or 'hard':")
guessNumber = 0
if difficulty == 'easy':
  chance = 10
  while number != guessNumber and chance != 0:
    guessNumber = numberGuess(chance,number)
    chance -= 1
elif difficulty == 'hard':
  chance = 5
  while number != guessNumber and chance != 0:
    guessNumber = numberGuess(chance, number)
    chance -= 1

if (chance == 0):
  print("You've run out of guesses, You lose.")
    
