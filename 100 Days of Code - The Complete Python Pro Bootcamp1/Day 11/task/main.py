import art
import random
print(art.logo)
# 0. 카드 번호
cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# 1. 첫번째, 두번째 카드를 컴퓨터와 서로 나눠 갖고 컴퓨터의 첫번째 카드번호와 내가 받은 두개의 카드번호를 알려준다.
users_cards=random.sample(cards, 2)
computer_cards=random.sample(cards, 2)

## 수정 전
# def blackjack_user(user, computer):
#     want_more = during_check(user, computer)
#     while want_more:
#         if want_more = during_check(user, computer) == False:
#             who_win(user=user, computer=computer_add)
#         print(f"You get the card number is {user} total {sum(user)}\nComputer's card number is {computer[0]} \n")
#         more_card=input("Do you want more the card?(y or n)").lower()
#         if more_card == "n":
#             want_more == False
#             computer_add=computer_turn(computer)
#             who_win(user=user, computer=computer_add)
#         add_card(user)

## 수정 후 : 계속 받게됨
def blackjack_user(user, computer):
    want_more = during_check(user, computer)
    while want_more:
        print(f"You get the card number is {user} total {sum(user)}\nComputer's card number is {computer[0]} \n")
        more_card = input("Do you want more the card? (y or n) ").lower()
        if more_card == "n":
            want_more = False
            computer_add = computer_turn(computer)
            who_win(user=user, computer=computer_add)
        else:
            add_card(user)



# If an ace is drawn, count it as 11.
# But if the total goes over 21, count the ace as 1 instead.
def add_card(more_card):
    more=random.choice(cards)
    if more == 11 and sum(more_card) + more > 21:
        more = 1
        more_card.append(more)
        return more_card
    more_card.append(more)
    return more_card

def who_win(user, computer):
    users_total = sum(user)
    computer_total = sum(computer)
    if users_total == computer_total:
        print("Tie~")
        print(f"Your value total is {user}={users_total}\nComputer value total is {computer} = {sum(computer)}")
    elif users_total == 21:
        print(f"You win! Your value total is {user}={users_total}\nComputer value total is {computer} = {sum(computer)}")
    elif computer_total == 21:
        print(f"Computer wins! Computer value total is {computer_total} ")
    elif users_total > computer_total:
        print(f"You win! Your value total is {user}={users_total}\nComputer value total is {computer} = {sum(computer)}")
    elif computer_total > 21:
        print(f"You win! Your value total is {user}={users_total}\nComputer value total is {computer} = {sum(computer)}")
    else:
        print("You loose!")
        print(f"Your value total is {user}={users_total}\nComputer value total is {computer} = {sum(computer)}")

def during_check(user, computer):
    if sum(user) == 21:
        print(f"You are Black jack, You win !")
        print(f"You win! Your value total is {user}\nComputer value total is {computer} = {sum(computer)}")
        return False
    elif sum(user) > 21:
        print(f"Your total value exceeds 21")
        print(f"Your value total is {user}={sum(user)}\nComputer value total is {computer} = {sum(computer)}")
        return False
    return True


def computer_turn(more_card):
    card_stop=sum(more_card)
    while card_stop < 17:
        more=random.choice(cards)
        if more == 11 and sum(more_card) + more >= 21:
            more = 1
        else:
            more_card.append(more)
            card_stop=sum(more_card)
    return more_card

again='y'
while again=='y':
    blackjack_user(user=users_cards, computer=computer_cards)
    again=input("Try again?? y or n")
    users_cards = random.sample(cards, 2)
    computer_cards = random.sample(cards, 2)
    if again=='n':
        users_cards.clear()
        computer_cards.clear()