from random import randint
from art import logo
EASY_LEVEL = 10
HARD_LEVEL = 5
turns = 0

def check_answer(user_guess,actual_answer,turns):
    if user_guess>actual_answer:
        print("too high")
        return turns-1
    elif user_guess<actual_answer:
        print("too low")
        return turns-1
    else:
        print(f"You guessed it,the answer is {actual_answer}")

def difficulty():
    level = input("Choose a difficulty. type 'easy' or 'hard': ")
    if level=="easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def game():
    print(logo)
    print("welcome")
    print("computer is thinking")
    ans = randint(1,100)
    #print(f"The correct answer is {ans} ")
    turns = difficulty()
    #print(f"u have {turns} attempts left")
    guess = 0
    while guess != ans:
        print(f"u have {turns} attempts left")
        guess = int(input("Do the guess! :"))
        turns = check_answer(guess,ans,turns)
        if turns == 0:
            print("ran out of guesses..  lose")
            break
        elif guess!=ans:
            print("guess again !")
game()
