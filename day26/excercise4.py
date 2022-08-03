sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# {new_key:new_value for item in dict or list}
split = sentence.split()
result = {word:len(word) for word in split}


print(result)

