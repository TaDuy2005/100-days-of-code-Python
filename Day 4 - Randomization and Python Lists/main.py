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
game_images = [rock, paper, scissors]
user_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))


random_number  = random.randint(0,2)
computer_choose = game_images[random_number]
if user_choose > 2 or user_choose < 0:
  print("You typed an invalid number, you lose!")
else:
  print(game_images[user_choose])
  print(f"Computer choose\n{computer_choose}")
  if (user_choose == 0 and random_number == 2) or (user_choose == 1 and random_number == 0) or (user_choose == 2 and random_number == 1):
    print("You win!")
  elif user_choose == random_number:
    print("It's a draw")
  else:
    print("You lose")
