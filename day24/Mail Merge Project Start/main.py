#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open(r'D:\Code\python\day24\Mail Merge Project Start\Input\Letters\starting_letter.txt') as file:
    content = file.read()

with open(r'D:\Code\python\day24\Mail Merge Project Start\Input\Names\invited_names.txt') as file:
    name = file.readlines()

for person in name:
        x = content.replace("[name]", person)
        y = x.strip()
        
        
        with open(f'D:\Code\python\day24\Mail Merge Project Start\Output\ReadyToSend\{person.strip()}.txt',"w") as file:
            file.write(y)
          


    

   

