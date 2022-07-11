import random

print("Welcome too Number Guessing Game!")
print("I am thinking of a number from 1 to 100")


def easy():
    lives= 10
    over = False
    number = random.randint(1,100)
    print(number)
    while over == False:
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it the answer was {number}")
            over = True
        else:
            lives -=1
            if(number > guess):
                print("Too low")
            elif(number < guess):
                print("Too high")   
            print(f"You have {lives} attemps remaining")
            if(lives == 0):
                print("Ran out of guesses, You lose.")
                over = True
                print(f"The number was {number}")    

def hard():
    lives = 5
    over = False
    number = random.randint(1,100)
    while over == False:
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it the answer was {number}")
            over = True
        else:
            lives -=1
            if(number > guess):
                print("Too low")
            elif(number < guess):
                print("Too high")   
            print(f"You have {lives} attemps remaining")
            if(lives == 0):
                print("Ran out of guesses, You lose.")
                over = True
                print(f"The number was {number}")

def play():
    c = input("Choose a difficulty, easy or hard : ").lower()
    if c == "easy":
        easy()
    if c == "hard":
        hard()    

play()