def prime_checker(number):
    primee= True
    for i in range(2,number):
        if(number % i == 0):
            primee =False
    if primee == True:
        print("Prime")
    else:
        print("Not prime")





n = int(input("enter the number"))
prime_checker(number=n)