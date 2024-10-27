dict={}
new_person=True
while new_person:
    person=input("what is your name:")
    bid=input("Enter your bidding amount:")
    dict[person]=bid
    new_person=input("Is there any other person?Yes or No:").lower()
    print("\n" *100)
    if new_person=="no":
        new_person=False

highest_bid=0
for bidder in dict:
    bid_amount=int(dict[bidder])
    if bid_amount>highest_bid:
        highest_bid=bid_amount
        highest_bidder=bidder
print(f"The winner of the bidding is {highest_bidder} with highest bid of {highest_bid}")
