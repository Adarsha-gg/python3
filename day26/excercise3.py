import random
names = ["alex","beth","caroline","dave","freddie"]

# {new_key:new_value for item in dict or list}

# {new_key:new value for (key,value) in dictionary.items()}
scores = {student:random.randint(50,100) for student in names}
passed = {student for student in scores if scores[student] >=60}
print(scores)
print(passed)