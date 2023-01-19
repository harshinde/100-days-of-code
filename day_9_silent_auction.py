from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
bidders = {}
list_bid_values = []

check = "yes"

while check == "yes":
  name = input("What is your name?\n")
  bid_value = input("What is your bid value?\n$")
  bidders[name] = bid_value
  list_bid_values.append(bid_value)
  check = input("Are there more bidders?Type yes or no\n")
  clear()
else:
  print("Thank you for all your bids")

#print all the dictionaries and lists
print(bidders)
print(list_bid_values)
print(list(bidders.keys()))

#find the max value, then the index of the value, the key in the list of bidders with that index
max_value = max(list_bid_values)
print(max_value)
index_max = list_bid_values.index(max_value)
print(index_max)
highest_bidder = list(bidders.keys())[index_max]
print(highest_bidder)
