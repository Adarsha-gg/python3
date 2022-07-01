
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
value = {"k":10,"q":10,"j":10,"a":11}
My_Card = []
Com_Card = []

def winner(score,comp_score):
    if(score == comp_score):
        print("Draw")    
    elif comp_score > 21:
        print( "Opponent went over. You win 😁")
    elif score > comp_score:
        print("You win")
    elif(score > 21):
        print("You went overboard. You lose")
    elif(score < comp_score):
        print("You lose. Dealer has more score")      
    
def play():
    lose = False
   
    score = 0
    comp_score =0
    g = input("Do you want to play a game of Blakcjack? Type 'y' or 'n' : ")
    if g == 'y':
        for i in range(0,2):
            card = int(random.choice(cards))
            score += card
            My_Card.append(card)
            card2 = int(random.choice(cards))
            Com_Card.append(card2)
            comp_score += card2
        print(f"Your hand is {My_Card} \n Current Score:{score}")
        print(f"Comp's first card' is  {Com_Card[0]}")
    elif g =='n':
        lose = True
        return
    while lose == False:    
        if score > 21:
            lose = True
        else:
            draw =input("Do you want to draw another card? Type 'y' or 'n' : ")            
        if draw == 'y':
            user_draw(score)
        if comp_score < 17:
            comp_draw(comp_score)
        print(f"Your cards: {My_Card}, current score: {score}")
        print(f"Computer's first card: {Com_Card[0]}")     
   
def user_draw(score):
        card = int(random.choice(cards))
        score += card
        My_Card.append(card)
        
        return score
    
def comp_draw(comp_score):
        card2 = int(random.choice(cards))
        comp_score += card2
        Com_Card.append(card2)
        
        return comp_score
play()    


    
   


