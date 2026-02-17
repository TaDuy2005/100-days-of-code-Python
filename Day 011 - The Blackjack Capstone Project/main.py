import random
from art import logo

def deal_card():
    card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(card)

def calculate_score(cards):
    if 11 in cards and sum(cards) >21:
        cards.remove(11)
        cards.append(1)

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score or (user_score > 21 and computer_score > 21):
        print("Draw 🙃")
    elif computer_score == 0:
        print("Lose, opponent has Blackjack 😱")
    elif user_score == 0:
        print("Win with a Blackjack 😎")
    elif user_score > 21:
        print("You went over. You lose 😭")
    elif computer_score > 21:
        print("Opponent went over. You win 😁")
    elif user_score < computer_score:
        print("You lose 😤")
    else:
        print("You win 😃")


def play_game():
    print(logo)

    #Deal to user and calculate the score of user card
    user_card = [deal_card(), deal_card()]
    user_score = calculate_score(user_card)

    # Deal to computer and calculate the score of computer card
    computer_card = [deal_card(), deal_card()]
    computer_score = calculate_score(computer_card)

    # Check whether if user or computer got a blackjack
    if user_score == 0 or computer_score == 0:
        # Show all the card and announce the winner then ask the user whether user want to play again
        print(f"Your final  hand: {user_card}, final score: {user_score}")
        print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
        compare(user_score, computer_score)

    else:
        # Show user card and first card of computer card
        print(f"Your cards: {user_card}, current score: {user_score}")
        print(f"Computer's first card: {computer_card[0]}")

        #Check whether the user want to draw a card or not
        user_draw = True

        while user_draw:
            get_card = input("Type 'y'  get another card, type 'n' to pass: ")
            if get_card == 'n':
                user_draw = False
            elif get_card == 'y':
                user_card.append(deal_card())
                user_score = calculate_score(user_card)
                print(f"Your cards: {user_card}, current score: {user_score}")
                print(f"Computer's first card: {computer_card[0]}")
            if user_score > 21:
                user_draw = False

        # After user stop draw, then check whether if computer would draw or not
        while computer_score < 17 and computer_score != 0:
            computer_card.append(deal_card())
            computer_score = calculate_score(computer_card)

        # After user and computer completely draw card, show all the card and announce
        # the winner then ask the user whether user want to play again
        print(f"Your final  hand: {user_card}, final score: {user_score}")
        print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
        compare(user_score, computer_score)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n"*20)
    play_game()
