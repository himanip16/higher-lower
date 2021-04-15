from game_data import data
import random
from art import logo, vs
from replit import clear


def get_random_account():
    return random.choice(data)


def format_data(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}"


def check_answer(account_a, account_b, guess):
    if account_a["follower_count"] > account_b["follower_count"]:
        return guess == "a"

    else:
        return guess == "b"


def game():
    print(logo)
    score = 0
    game_should_continue = True

    account_b = random.choice(data)

    while game_should_continue:
        account_a = account_b
        account_b = random.choice(data)

        while account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        clear()
        print(logo)
        if check_answer(account_a, account_b, guess):
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()
