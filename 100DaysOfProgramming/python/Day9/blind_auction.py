import os
from modules import secret_art


def image():
    print(secret_art.logo)

def add_bidder(bidders):
    image()

    name = input("What is your name?: ")
    bid = float(input("What is your bid? $"))
    additional_bidders = input("Are there additional bidders? (y/n) ").lower()
    bidders[name] = bid

    if additional_bidders == "y":
        os.system("clear")
        add_bidder(bidders)
    else:
        calculate_winner(bidders)

def calculate_winner(bids):
    highest_bid = 0

    for key in bids:
        if highest_bid == 0 or highest_bid < bids[key]:
            winner = {}
            winner[key] = bids[key]
            highest_bid = bids[key]
        elif highest_bid == bids[key]:
            winner[key] = bids[key]

    if len(winner) == 1:
        print("winner", winner)
    else:
        print("tie", winner)

if __name__ == '__main__':
    bidders = {}
    add_bidder(bidders)
