current_bids = {}
more_bids = True

while more_bids:
    name = input("What is your name?\n")
    bid = int(input(f"How much would you like to bid on this item?\n£"))

    current_bids[name] = bid


    highest_bidder = max(current_bids, key=current_bids.get)
    highest_bid = max(current_bids.values())
    another_bidder = input("Is there another person to bid? Yes or No\n").lower()

    if another_bidder == "yes":
        print("\n" * 20)
    else:
        print(f"Congratulations: {highest_bidder}, you win the auction with a bid of £{highest_bid}")
        more_bids = False
