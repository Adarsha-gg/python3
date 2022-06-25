import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
intz = random.randint(0,len(names)-1)
print(f"{names[intz]} is going to pay the bill")


