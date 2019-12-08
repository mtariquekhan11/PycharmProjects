# Author: Mohd Tarique Khan
# Date: 14/10/2019
# Purpose: Game for playing cards

# importing the modules random and itertools
import random
import itertools

condition = "True"

# Variable initialization for their types and numbers

color_lst = ["Clubs", "Diamonds", "Hearts", "Spades"]
card_num = range(1, 14)

# Deck preparation on the basis of their combination with the help of itertools.product

card_deck1 = list(itertools.product(card_num, color_lst))
card_deck2 = list(itertools.product(card_num, color_lst))


# print(card_deck1, "\n")
# print(card_deck2, "\n")

# Function to shuffle the deck with the help of random function
def shuffle():
    random.shuffle(card_deck1)
    random.shuffle(card_deck2)
    # print(card_deck1, "\n")
    # print(card_deck2, "\n")
    return ()


def print_card(card_deck, no_of_cards):
    for i in range(no_of_cards):
        print(card_deck[i][0], "of", card_deck[i][1])


def calculate(card_deck, no_of_cards):
    card_total = 0
    for i in range(no_of_cards):
        # print(card_deck[i][0])
        value = (card_deck[i][0])
        card_total = card_total + value
    print(f"Total Score = {card_total}")
    return card_total


def compare_winner(p1, p2):
    if p1 > p2:
        print(f"\nCongratulations!!! {name} is WINNER")
    elif p1 < p2:
        print(f"\nSorry!!! {name}, You LOSS, BETTER LUCK NEXT TIME")
    elif p1 == p2:
        print(f"\nOOPs there is a tie!!! {name} BETTER LUCK NEXT TIME")


if __name__ == '__main__':

    while condition is "True":
        name = input("Enter your name to play the cards: ")
        no_of_cards = int(input("\nEnter the number of cards per person:"))
        shuffle()

        # To withdraw three different cards for the player and calculate total score
        print(f"\n{name} you got:\n")
        print_card(card_deck1, no_of_cards)
        tot_score1 = calculate(card_deck1, no_of_cards)

        # To withdraw five different cards for the Computer and calculate total score
        print("\n Computer got:\n")
        print_card(card_deck2, no_of_cards)
        tot_score2 = calculate(card_deck2, no_of_cards)

        # To compare the total scores of players to select the winner
        compare_winner(tot_score1, tot_score2)

        condition1 = input("Do you want to check more, Press Y or y: ")
        if condition1 == "y" or condition1 == "Y":
            condition = "True"
        else:
            break
