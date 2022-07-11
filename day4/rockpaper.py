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

#Write your code below this line 👇
intt =random.randint(0,2)
choice =int(input("0 for rock,1 for paper,2 for scissors: "))
print(f"you chose {choice}")
if(choice == 0):
    print(rock)
elif(choice == 1):
    print(paper)
elif(choice == 2):
    print(scissors)
else:
    print("Enter a valid command")
print(f"comp  chose {intt}")
if(intt == 0):
    print(rock)
elif(intt == 1):
    print(paper)
elif(intt == 2):
    print(scissors)


if(intt == 0 and choice == 0 ):
    print("draw")
elif(intt == 0 and choice == 1):
    print("You win")
elif(intt == 0 and choice == 2):
    print("you lose")
elif(intt == 1 and choice == 0 ):
    print("you lose")
elif(intt == 1 and choice == 1):
    print("draw")
elif(intt == 1 and choice == 2):
    print("you win")    
elif(intt == 2 and choice == 0 ):
    print("you win")
elif(intt == 2 and choice == 1):
    print("You lose")
elif(intt == 2 and choice == 2):
    print("draw")    