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

#Write your code below this line 👇
import random
game_choice = ['rock', 'paper', 'scissor']

computer_choice = game_choice[random.randint(0,len(game_choice)-1)]
print(computer_choice)

your_choice = input("rock or paper or scissor ")

print(your_choice)

if (your_choice == "rock" and computer_choice == "scissor"):
  print("You win")
elif (your_choice == "scissor" and computer_choice == "paper"):
  print("You win")
elif (your_choice == "paper" and computer_choice == "rock"):
  print("You win")
