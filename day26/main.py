
import pandas

data = pandas.read_csv("day26/nato_ez.csv")

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
dict ={row.letter:row.code for (index,row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
ans = input("Enter a word: ").upper() 
phoneic = {dict[letter] for letter in ans }
print(phoneic)

