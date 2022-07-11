print("Welcome to the tip calculator")
bill = float(input("What was the total bill? Rs. "))
tip = int(input("what percentage tip do u want to give? 10,13,15 :"))
splitt = int(input("How many people to split: "))


if (tip == 10):
    total =(0.1*bill+bill)/splitt
    
elif (tip == 12):
    total =(0.12*bill+bill)/splitt    
    
elif (tip == 15):
    total =(0.15*bill+bill)/splitt
        
   
       
print(f"Each person should pay Rs.{total} ")       
