def encrypt(text,shift):
    cipher =""
    for i in text:
        position = alphabet.index(i)
        new = position +shift
        new_letter = alphabet[new]
        cipher +=new_letter
    print(f"the encoded ans is {cipher}")

def decrypt(text,shift):
    de_text=""
    for i in text:
        poss = alphabet.index(i)
        new_pos = poss - shift
        letter = alphabet[new_pos]
        de_text += letter
    print(f"the decoded ans is {de_text}")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = (input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")).lower()
if direction == "encode":
    t = input("Type your message:\n").lower()
    s = int(input("Type the shift number:\n"))
    encrypt(t,s)  
if direction == "decode":
    t = input("Type your cipher:\n").lower()
    s = int(input("Type the shift number:\n"))
    decrypt(t,s)  

