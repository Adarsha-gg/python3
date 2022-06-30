
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
value = {"k":10,"q":10,"j":10,"a":11}

lose = False
My_Card = []
Com_Card = []
score = 0
comp_score =0
g = input("Do you want to play a game of Blakcjack? Type 'y' or 'n' : ")
if g == 'y':
    for i in range(0,2):
        card = int(random.choice(cards))
        score += card
        My_Card.append(card)
    
    print(f"Your hand is {My_Card} \n Current Score:{score}")
    card2 = int(random.choice(cards))
    Com_Card.append(card2)
    comp_score += card2
    print(f"Comp's first card' is  {Com_Card}")
    while lose == False
        draw =input("Do you want to draw another card? Type 'y' or 'n' : ")
        if draw == 'y':
            card = random.choice(cards)
            My_Card.append(card)
            score += card
        if draw == 'n':
            card2 = random.choice(cards)
            Com_Card.append(card2)    
elif g =='n':
    start = False