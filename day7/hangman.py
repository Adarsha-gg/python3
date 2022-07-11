import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
win = False
word = ["aardvark", "baboon", "camel","rahul"]
main = random.choice(word)
lives =6
g = len(main)
display = []

for i in range(g):
    display +="_"
print(display)
while(lives != 0 or win == False):
    guess = input("Enter ur guess: ").lower()
    for position in range(g):   
        letter = main[position]
        if(guess == letter):
            display[position] = letter
           
    if guess not in main:
        lives -=1
        if lives == 0:
            win = True
            print("You lose")
            print(f"The word was {main}")
            
    print(f"{' '.join(display)}")
    if"_" not in display:
        win = True
        print("You win")
        print(f"The word was {main}")
    print(stages[lives])
