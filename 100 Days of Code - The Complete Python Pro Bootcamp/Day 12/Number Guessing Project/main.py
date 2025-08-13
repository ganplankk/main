import random
from art import logo

print(logo)

level = input("Choice what do you want a difficulty level?(High or Low)").strip().lower()
lives = 5 if level == "high" else 10
target = random.choice(range(1,100))

def guess(r_target, r_lives):
    while r_lives > 0:
        try:
            choice = int(input("Enter a number between 1 and 100: "))
        except ValueError:
            print("Invalid input, Please enter integer between 1 and 100")
            continue
        if choice == r_target:
            print("Right!")
            return
        elif choice < r_target:
            print(f"too low! You remain your life {r_lives}")
            r_lives -= 1
        elif choice > r_target:
            print(f"too high! You remain your life {r_lives}")
            r_lives -= 1

guess(r_target = target, r_lives = lives)


