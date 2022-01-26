from replit import clear
#HINT: You can call clear() to clear the output in the console.
# number =[8,500,99,10]
# max_number = 0
# for x in number:
#   if x > max_number:
#    max_number =x
# print(f"max number is {max_number}")
from art import logo
print(logo)
user_dictionary ={}
restart = True
while restart:
  name = input("Enter your name ...\n")
  bid = int(input("Enter your bid amount ...\n"))
  user_dictionary[name] = bid
   
  other_user = input("Any other user who want to bid,if yes type yes if no type no...\n")
  if other_user=="yes":
    restart=True
    clear()
      
  else:
    restart=False


def maxbid():
    max_bid_amount = 0
    winner =""
    for user in user_dictionary:
      x = user_dictionary[user]
      if x >max_bid_amount:
        max_bid_amount = x
        winner = user
    print(f"And the winner is {winner} with {max_bid_amount}$")

maxbid()





  

