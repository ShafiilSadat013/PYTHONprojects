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

image = [rock,paper,scissors]
user = int(input("0 for rock , 1 for paper , 2 for scissors : "))
computer_choice = random.randint(0,2)
print("Computer choice is :")
print(image[computer_choice])

if user>=3 or user<0:
    print("invalid propmpt, You lose !!")
else:
    print("User choice is : ")
    print(image[user])

if user == computer_choice :
    print("It is a draw")
elif user == 0 and computer_choice==1:
    print("You Lost !")
elif user == 0 and computer_choice == 2:
    print("You Win!")
elif user == 1 and computer_choice == 0:
    print("You Win!")
elif user == 1 and computer_choice == 2:
    print("You Lost!")
elif user == 2 and computer_choice == 0:
    print("You Lost!")
elif user == 2 and computer_choice == 1:
    print("You Win!")
