def ceaser(text,shift,direction):
    cipher =""
    for i in text:
        position = alphabet.index(i)
        if(direction == "encode"):
            new = position +shift
        elif(direction == "decode"):
            new = position -shift
        new_letter = alphabet[new]
        cipher +=new_letter
    print(f"the ans is {cipher}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


directionn = (input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")).lower()
t = input("Type your message:\n").lower()
s = int(input("Type the shift number:\n"))

ceaser(t,s,directionn)
