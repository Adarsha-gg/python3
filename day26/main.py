# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas
valid = False
data = pandas.read_csv("day26/nato_ez.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

while not valid:
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
        valid = True
    except KeyError:
        print("Only letters please")

print(output_list)


#alternately create a function and call the function inside itself during exceptions