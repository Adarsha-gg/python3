print("Welcome to the tip calculator")
bill=float(input("What is the total bill?\n"))
people=int(input("How many people to split the bill?\n"))
tip=int(input("What percent would you like to tip?\n"))

bill= (bill+(bill*tip/100))/people


amount=round (bill, 2)

print(f"Each person has to pay ${amount}.")