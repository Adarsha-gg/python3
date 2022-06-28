
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
#HINT: You can call clear() to clear the output in the console.
bids ={}
bidding_finish = False
print(logo)
bidding_record = {}
print("Welcome to secret auction")
def highest(bidding_record):
  high = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > high:
      high = bid_amount
      winner = bidder
  print(f"the winner is {winner} with bid of ${high}")

while not bidding_finish:
  a = input("What's your name: ")
  b = int(input("Enter ur bid: "))
  bids[a] = b
  choice = input("are there more bidders? y/n").lower()
  if(choice == "y"):
    print("waow")
  elif(choice =="n"):
    bidding_finish= True
    highest(bids)
  
