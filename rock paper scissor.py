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
elements=[rock,paper,scissors]
mychoice=random.randint(0,2)
computerchoice=random.randint(0,2)
print(f"My choice is {elements[mychoice]}")
print(f"Computer choice is {elements[computerchoice]}")
if mychoice==computerchoice:
  print("Draw")
elif mychoice==0 and computerchoice==1:
  print("Computer wins")
elif mychoice==0 and computerchoice==2:
  print("I win")
elif mychoice==1 and computerchoice==0:
  print("I win")
elif mychoice==1 and computerchoice==2:
  print("Computer wins")
elif mychoice==2 and computerchoice==0:
  print("Computer wins")
elif mychoice==2 and computerchoice==1:
  print("I win")