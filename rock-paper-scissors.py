import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choose = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
inchoose = int(choose)
if inchoose == 0:
  print(rock)
if inchoose == 1:
  print(paper)
if inchoose == 2:
  print(scissors)
computer_chose = random.randint(0,2)

if inchoose == 0 or inchoose == 1 or inchoose == 2:
  print(f"Computer chose:")
  if computer_chose == 0:
    print(rock)
  elif computer_chose == 1:
    print(paper)
  else:
    print(scissors)

if computer_chose == inchoose:
  print("It's a draw")
elif (inchoose == 0 and computer_chose == 1) or (inchoose == 1 and computer_chose == 2) or (inchoose == 2 and computer_chose == 0):
  print("You lose")
elif (inchoose == 0 and computer_chose == 2) or (inchoose == 1 and computer_chose == 0) or (inchoose == 2 and computer_chose == 1):
  print("You win!")
else:
  print("You typed and invalid number, you lose")
