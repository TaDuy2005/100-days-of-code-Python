from art import logo

print(logo)

bidding_finished = False
bid_list = {}

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for name in bidding_record:
        if bidding_record[name] > highest_bid:
            highest_bid = bidding_record[name]
            winner = name
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:

    bidder = input("What is your name? ")
    bid_amount = float(input("What is your bid? $"))

    bid_list[bidder] = bid_amount

    restart = input("Are there any other bidders? Type 'yes or 'no'.\n")

    if restart.lower() == 'yes':
        print("\n"*20)
    elif restart.lower() == 'no':
        bidding_finished = True
        find_highest_bidder(bid_list)
