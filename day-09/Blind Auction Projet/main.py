# TODO-1: Ask the user for input
import art
print(art.logo)
user_want = True
name_and_bid = {}
while user_want:
    name = input("What is your name?: ")
    bid_price = int(input("What is your bid?: $"))
    name_and_bid[name] = bid_price
    user_wants = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if user_wants == "no":
        user_want = False
        for value in name_and_bid.values():
            if value == max(name_and_bid.values()):
                winner = max(name_and_bid, key=name_and_bid.get)
                print(f"The winner is {winner} with a bid of ${name_and_bid[winner]}.")
    else:
        user_want = True
        print("\n" * 100)

# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


