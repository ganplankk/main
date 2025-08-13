MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# TODO 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
# TODO 2. Print Report
def report():
    print(f"Water : {resources['water']}ml")
    print(f"Milk : {resources['milk']}ml")
    print(f"Coffee : {resources['coffee']}g")
    print(f"Money : ${profit}")

def pay(p_order, is_sufficient):
    for i in is_sufficient:
        if resources[i] < is_sufficient[i]:
            print(f"Sorry there is not enough {i}.")
    coin = int(input("how many pay quarters?:")) * 0.25
    coin += int(input("how many pay dimes?:")) * 0.1
    coin += int(input("how many pay dimes?:")) * 0.05
    coin += int(input("how many pay pennies?:")) * 0.01
    if coin >= MENU[p_order]['cost']:
        change = coin - MENU[p_order]['cost']
        print(f"Thank you, here is your drink{p_order} and refund {change}")
        global profit
        profit += coin - change
        for i in is_sufficient:
            resources[i] -= is_sufficient[i]
    else:
        print(f"Sorry that's not enough money. Money refunded. : {coin}")

def e_pay(p_order):
    if resources['water'] < MENU[p_order]['ingredients']["water"]:
        print(f"Sorry there is not enough water.")
    elif resources['coffee'] < MENU[p_order]['ingredients']["coffee"]:
        print(f"Sorry there is not enough coffee.")
    else:
        coin = float(input("how many pay quarters?:")) * 0.25
        coin += float(input("how many pay dimes?:")) * 0.10
        coin += float(input("how many pay pennies?:")) * 0.10
        if coin >= MENU[p_order]['cost']:
            change = round(coin - MENU[p_order]['cost'], 2)
            print(f"Thank you, here is your drink{p_order} and refund {change}")
            global profit
            profit += coin - change
            resources['water'] -= MENU[p_order]['ingredients']["water"]
            resources['coffee'] -= MENU[p_order]['ingredients']["coffee"]
        else:
            print(f"Sorry that's not enough money. Money refunded. : {coin}")

is_on = True
while is_on:
    order = input("What would you like? (espresso/latte/cappuccino):").strip().lower()
    if order == "off":
        is_on = False
    elif order == "report":
        report()
    elif order == "latte" or order == "cappuccino" or order == "espresso":
        pay(order, MENU[order]['ingredients'])

