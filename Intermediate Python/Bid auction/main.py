import os

# Function to clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

bid_dic={}
def bid_asker(enter_name,enter_bid):
    bid_dic[name]=bid

condition=True
highest_bid=0
hisghest_bidder=0
while condition:
    name=input("What is your name? ")
    bid=int(input("What is your bid? "))


    bid_asker(name,bid)
    ask=input("Do you have another bider")
    if ask =="no":
        condition=False
    clear()

for i in bid_dic:
    if bid_dic[i]>highest_bid:
        highest_bid=bid_dic[i]
        hisghest_bidder=i

print(f"tyhe winner is {hisghest_bidder} with a bid of {highest_bid}")
