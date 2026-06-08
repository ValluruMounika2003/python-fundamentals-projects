import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
your_choice=input("Rock, paper, or scissors: ").lower()
computer=random.choice([rock,paper,scissors])
print(computer)
your_choice=random.choice([rock,paper,scissors])
print(your_choice)

if computer==rock and your_choice==paper:
    print(" you win")
elif  computer ==paper and your_choice==scissors:
    print("you win")
elif computer==scissors and your_choice==rock:
    print("you win")
elif your_choice==rock and computer==paper:
    print(" you lose")
elif your_choice==paper and computer==scissors:
    print("you lose")
elif your_choice==scissors and computer==rock:
    print("you lose")
else:

        print("It's a tie")