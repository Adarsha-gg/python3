
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def div(n1, n2):
    return n1 / n2
def mul(n1, n2):
    return n1 * n2
dict = {"/":div ,"*":mul,"-":sub,"+":add}

def calculate():
    first = float(input("What's the fisrt number: "))
    finish = False
    while finish == False:
        second = float(input("Whats the second number: "))
        for symbol in dict:
            print(symbol)
        operator = input("Pick operator from the above: ")
        function = dict[operator]
        ans = function(first,second)
        print(f"{first} {operator} {second} = {ans}")
        choice = input(f"Type 'y' to continue calculating with {ans}, or type 'n' to exit: ")
        if(choice == "n"):
            finish = True
        if(choice == "y"):
            first = ans
            calculate()
calculate()
            