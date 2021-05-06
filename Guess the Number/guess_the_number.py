#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Name!")
print("I'm thinking of a number between 1 and 100.")
computer_number = random.randint(1, 100)
print(f"Pssst, the correct answer is {computer_number}")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0
end_game = False
if level == "easy":
  print("You have 10 attempts remaining to guess the number.")
  attempts = 10
elif level == "hard":
  print("You have 5 attempts remaining to guess the number.")
  attempts = 5

def guessing():
  global attempts
  guess = int(input("Make a guess: "))
  
  if not guess == computer_number:
    attempts -= 1
    if guess < computer_number and attempts == 0:
      print("Too low.")
      print("You've run out of guesses, you lose.")
    elif guess > computer_number and attempts == 0:
      print("Too high.")
      print("You've run out of guesses, you lose.")
    elif guess > computer_number:
      print("Too high.")
      print("Guess again.")
      print(f"You have {attempts} attempts remaining to guess the number.")
    elif guess < computer_number:
      print("Too low.")
      print("Guess again.")
      print(f"You have {attempts} attempts remaining to guess the number.")

  elif guess == computer_number:
    print(f"You got it! The answer was {guess}.")
    global end_game
    end_game = True
   

while attempts > 0:
  if end_game == False:
    guessing()
