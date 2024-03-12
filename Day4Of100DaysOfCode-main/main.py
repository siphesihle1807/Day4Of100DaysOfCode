import random

print("Play RPS against a computer.")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
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

print("Choose:\n0 for ROCK\n1 for PAPER\n2 for SCISSORS.")

first_move = input("What is your choice?: ")
if int(first_move) == 0:
    print("You chose: ")
    print(rock)
elif int(first_move) == 1:
    print("You chose: ")
    print(paper)
elif int(first_move) == 2:
    print("You chose: ")
    print(scissors)

print("Now, it's the computers turn!")
random_move = random.randint(0,2)
if int(random_move) == 0:
    print("The computer chose: ")
    print(rock)
elif int(random_move) == 1:
    print("The computer chose: ")
    print(paper)
elif int(random_move) == 2:
    print("The computer chose: ")
    print(scissors)

if int(first_move) == int(random_move):
    print("Wow!!It is a draw!")
elif int(first_move) == 1 and int(random_move) == 0: 
    print("Congratulations. You win!")
elif int(first_move) == 0 and int(random_move) == 1:
    print("Ooops! Computer wins!")
elif int(first_move) == 2 and int(random_move) == 1:
    print("Congratulations. You win!")
elif int(first_move) == 1 and int(random_move) == 2:
    print("Ooops! Computer wins!")
elif int(first_move) == 0 and int(random_move) == 2:
    print("Congratulations. You win!")
elif int(first_move) == 2 and int(random_move) == 0:
    print("Ooops! Computer wins!")

