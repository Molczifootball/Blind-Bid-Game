from replit import clear
from art import *
#HINT: You can call clear() to clear the output in the console.
all_bids = []
print(logo)
if_next = "Y"
def ask_user():
  name = input("What is your name ?")
  bid = int(input("Whats ur bid ?"))
  dist = {
  "Name" : name,
  "Bid" : bid
  }
  all_bids.append(dist)
  
def show_winner():
  current_max_bid = 0
  current_winner = ""
  for x in all_bids:
    if x["Bid"] > current_max_bid:
      current_max_bid = x["Bid"]
      current_winner = x["Name"]
  print(f"WINNER IS {current_winner}, with the bid of: {current_max_bid}")

while if_next!="N":
  ask_user()
  clear()
  if_next = input("Is there anyone else ? Y/N")
  
show_winner()