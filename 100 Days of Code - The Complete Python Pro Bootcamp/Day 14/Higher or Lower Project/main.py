import random
import art
import game_data

## 메인 게임 함수 : art.py, game_data.py 불러와서 출력해주기
def main_game():
    print(art.logo)
    total_count = 0
    life = True
    compare_a, against_b = random_user()
    while life:
        compare_a = against_b
        against_b = random.randint(0, len(game_data.data) - 1)
        print(f"Compare A: {game_data.data[compare_a]['name']}, {game_data.data[compare_a]['description']},"
              f" {game_data.data[compare_a]['country']}")
        print(art.vs)
        print(f"Against B: {game_data.data[against_b]['name']}, {game_data.data[against_b]['description']},"
              f" {game_data.data[against_b]['country']}")
        try:
            u_answer = str(input("Who has more followers Type 'A' or 'B'? :").strip().lower())
        except ValueError:
            print("You have to enter only type 'A' or 'B'.")
            u_answer = input("Who has more followers Type 'A' or 'B'? :").strip().lower()

        winner=str(compare_followers(a=compare_a, b=against_b))
        life, total_count = who_winner(winner, u_answer, total_count)

def random_user():
    compare_a = random.randint(0, len(game_data.data) - 1)
    against_b = random.randint(0, len(game_data.data) - 1)
    return compare_a, against_b

def compare_followers(a,b):
    if game_data.data[a]['follower_count'] > game_data.data[b]['follower_count']:
        return 'a'
    else:
        return 'b'

def who_winner(winner, u_answer, total_count):
    if winner == u_answer:
        total_count += 1
        print(f"You're right! Current score {total_count}")
        return True, total_count
    else:
        print(f"Sorry, that's wrong. Final score: {total_count}")
        return False, total_count

main_game()