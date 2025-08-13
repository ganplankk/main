# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added

import art
replay = True
print(art.logo)
dic = {}

while replay:
    name = input("What is your name? ")
    price = int(input("What is your bid? "))
    dic[name] = price ## name : price
    again = input("Would you like to play again? ").lower()
    if again == "no":
        replay = False

# TODO-4: Compare bids in dictionary
def winner(bidding_dic):
    max_price = max(bidding_dic.values())
    for i in dic:
        who_next = i
        if dic[who_next] == max_price:
            bid_winner = who_next
            print(f"{bid_winner} wins!, bidding price is {dic[who_next]}")

    # if max_price==max(bidding_dic.values()):
    #     print(f"You win! The bidding price is: {max_price}")
    # for i in dic:
    #     # print(dic.keys())
    #     total_price.append(dic[i][0])
    #     max_price=max(total_price)
    #
    # for j in dic:
    #     who_next=j
    #     # if int(max_price) in int(dic[who_next][0]):
    #     #     print(f" Winner is {dic[who_next]}, he have bet price {max_price}")
    #     if dic[who_next] == max_price:
    #         print(f"Winner is {who_next}, he has bid {max_price}")

winner(bidding_dic = dic)

