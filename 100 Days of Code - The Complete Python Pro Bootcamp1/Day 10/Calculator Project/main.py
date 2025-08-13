from sys import set_coroutine_origin_tracking_depth
import art
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

def calculator():
    print(art.logo)
    again=True
    first = input("Enter your first number: ")
    while again:

        dic = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": div,
        }

        for i in dic:
            print(i)`
        operator = input("Enter your operator: ")
        second = input("Enter your second number: ")
        values = dic.get(operator)(float(first), float(second))
        print(f"{first} {operator} {second} = {values}")
        do=input(f"Current values is {values}, Continue calculating? (y/n)").lower()
        if do == "n":
            again = False
            calculator()
        first=values

calculator()