from art import logo
print(logo)

bidders = {}
bidding_is_on = True

#Angela's function
# def find_highest_bidder(bidding_record):
    # highest_bid = 0
    # winner = ""
    # for bidder in bidding_record:
    # bid_amount = bidding_record[bidder]
    #     if bid_amount > highest_bid:
    #         highest_bid = bid_amount
    #         winner = name
    # print(f"The winner is {winner} with a bid of {highest_bid}")

while bidding_is_on:

    name = input("What is your name?: ")
    bid = int(input("How much are you bidding?: $"))
    bidders[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if other_bidders == "yes":
        clear()
    elif other_bidders == "no":
        bidding_is_on = False
        #Angela called a function she created - find_highest_bidder(bidders) 

        highest_bid = 0
        highest_bidder = ""
        for name in bidders:
            if bidders[name] > highest_bid:
                highest_bid = bidders[name]
                highest_bidder = name
        print(f"The winner is {highest_bidder} with a bid of {highest_bid}")