for number in range(0,100):
    if (number%5 == 0 and number%3 == 0):
        print("Fizzbuzz")
    elif(number%5 == 0):
        print("buzz")
    elif(number%3 == 0):
        print("fizz")    
    else:
        print(number)
