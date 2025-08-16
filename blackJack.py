#BLACK JACK V1

import random
from art import logo

def deal_card():
     """return a random card from the deck"""
     cards =  [11,2,3,4,5,6,7,8,9,10,10,10,10]
     card = random.choice(cards)
     return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    #if 11 in cards and 10 in cards and len(cards)==2:
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
# u_sc means user score , c_sc means computers score
def compare(u_sc, c_sc):
    if u_sc == c_sc:
        return "Draw!"
    elif c_sc == 0:
        return "Lose , opponent has a BlackJack"
    elif u_sc == 0:
        return "Win with a BlackJack "
    elif u_sc > 21:
        return "You went over 21. Busted "
    elif c_sc > 21:
        return "Opponent went over. You win <3"
    elif u_sc > c_sc:
        return "You win "
    else:
        return "You Lose :( "


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False
    for _ in range(2):
        #new_card = deal_card()
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards : {user_cards},current score : {user_score}")
        print(f"computer's first card : {computer_cards[0]} ")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over =  True

        else:
            user_should_deal = input("type 'y' to get another card pr type 'n' to pass : ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over =  True

    while computer_score!=0 and computer_score < 17 :
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final cards {user_cards}, final score is : {user_score}")
    print(f"Computer's final cards : {computer_cards}, computer's final score is : {computer_score}")
    print(compare(user_score,computer_score))

while input("Wanna play blackjack ? type 'y' or 'n' : ") == "y" :
    print("\n" * 20)
    play_game()
