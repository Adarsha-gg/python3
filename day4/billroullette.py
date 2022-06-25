import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
int = random.randint(0,len(names)-1)
print(f"{names[int]} is going to pay the bill")


