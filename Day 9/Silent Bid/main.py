from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
print (art.logo)
def highestBid(allBid):
  max = -999
  winner = ""
  for key in allBid:
    if allBid[key] > max:
      max = int(allBid[key])
      winner = key
  print (f"The winner is {winner} with a Bid of ${max}.")


allBid = {}
flag = True
print("Welcome to the secret auction program.")
while flag:
  name = input("What is your name?:") 
  bid = int(input("What is your Bid?: $"))
  allBid[name] = bid
  choice = input("Are there any other bidders? Type 'yes' or 'no'")
  if choice == "yes":
    clear()
  elif choice == "no":
    flag = False
  else :
    break
clear()
highestBid(allBid)
