#by me
from game_data import data
import art
import random
from replit import clear
score = 0
print (art.logo)
def wrongChoice():
  clear()
  print(art.logo)
  print(f"Sorry, that's wrong. Final score: {score}")

def correctChoice():
  clear()
  print(art.logo)
  global score
  score += 1
  print(f"You're right, Current score: {score}")
  game()
  
def result(playerA,playerB,choice):
  if choice == 'A':
    if playerA['follower_count'] > playerB['follower_count']:
      correctChoice()
    else:
      wrongChoice()
  elif choice == 'B':
    if playerA['follower_count'] < playerB['follower_count']:
      correctChoice()
    else:
      wrongChoice()
  
def game():
  playerA = random.choice(data)
  print(f"Compare A: {playerA['name']}, {playerA['description']}, from {playerA['country']}.")
  print(art.vs)
  playerB = random.choice(data)
  while(playerB['name'] == playerA['name']):
    playerB = random.choice(data)
  print(f"Against B: {playerB['name']}, {playerB['description']}, from {playerB['country']}.")
  choice = input("Who has more followers? Type 'A' or 'B':")
  result(playerA, playerB, choice)

game()
