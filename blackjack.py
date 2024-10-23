import random
import time
import sys
MAX_B4_BUST = 21
BUST = False
suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

deck_of_cards = []

for i in range(len(suits)):
    for j in range(len(cards)):
        deck_of_cards.append(f"{cards[j]} of {suits[i]}")


def adjust_for_aces(hand_value, num_aces):
    while hand_value > MAX_B4_BUST and num_aces > 0:
        hand_value -= 10  # Treat an Ace as 1 instead of 11
        num_aces -= 1
    return hand_value


def dealer_moves(dealer_hand, player_hand_value):
    global MAX_B4_BUST
    MAX_B4_BUST = 21  # Assuming this constant is defined
    print(f"Dealer Shows his Down Card: {dealer_second_card}")
    time.sleep(1)
    print(f"Dealer Hand: {dealer_hand}")

    while dealer_hand < 17:
        random_card = random.choice(deck_of_cards)
        print(f"Dealer draws: {random_card}")
        dealer_hand += card_value(random_card)
        print(f"Dealer Has: {dealer_hand}")
        time.sleep(1)

        # Check if dealer busts
        if dealer_hand > MAX_B4_BUST:
            print("Dealer Bust! Player Wins.")
            sys.exit(0)

    # Final comparison between dealer and player hands
    if dealer_hand > player_hand_value:
        print("Dealer Wins!")
        sys.exit(0)
    elif dealer_hand < player_hand_value:
        print("Player Wins!")
        sys.exit(0)
    else:
        print("It's a tie!")
        sys.exit(0)



def hit_me(players_hand_value):
    global BUST
    while True:
        if players_hand_value < MAX_B4_BUST:
            boom_or_doom = input('Dealer looks at you and signals towards your hand: \nWould you like to Hit or Stand? (h/s):  ').lower()
            if boom_or_doom == 'h':
                random_card = random.choice(deck_of_cards)
                print(f"{random_card}")
                players_hand_value += card_value(random_card)
                print(f"You Have: {players_hand_value}")
                if players_hand_value > MAX_B4_BUST:
                    print("You Bust: Dealer Wins.")
                    BUST = True
                    break
            elif boom_or_doom == 's':
                print("You stand. Good Luck.")
                break
        else:
            print("You Have a Blackjack! You Win.")
            break
    return players_hand_value, BUST


def random_card_from_deck():
    return random.choice(deck_of_cards)


def card_value(card):
    if card.startswith('Ace'):
        return 11
    elif card.startswith('2'):
        return 2
    elif card.startswith('3'):
        return 3
    elif card.startswith('4'):
        return 4
    elif card.startswith('5'):
        return 5
    elif card.startswith('6'):
        return 6
    elif card.startswith('7'):
        return 7
    elif card.startswith('8'):
        return 8
    elif card.startswith('9'):
        return 9
    elif card.startswith('10') or card.startswith('Jack') or card.startswith('Queen') or card.startswith('King'):
        return 10


dealer_1st_question = input('All bets in? (y/n):  ')
if dealer_1st_question == 'y'.lower():
    first_card = random.choice(deck_of_cards)
    first_card_value = card_value(first_card)
    second_card = random.choice(deck_of_cards)
    second_card_value = card_value(second_card)
    dealer_first_card = random.choice(deck_of_cards)
    dealer_first_card_value = card_value(dealer_first_card)
    dealer_second_card = random.choice(deck_of_cards)
    dealer_second_card_value = card_value(dealer_second_card)
    insurance_denial_expression = ["You Shake Your Head", 'You say, "Nope"', "You wave your hand over the table: declining" ]
    # time.sleep(1)
    print('Dealing...')
    # time.sleep(2)
    print(f'\nPlayer First Card: {first_card}\n')
    # time.sleep(1)
    print('Dealing...')
    # time.sleep(2)
    print(f'\nDealer Up Card: {dealer_first_card}\n')
    # time.sleep(1)
    print('Dealing...')
    # time.sleep(2)
    print(f'\nPlayer Second Card: {second_card}\n')
    # time.sleep(1)
    print('\nDealing Dealer Down Card\n')
    # time.sleep(1)

    player_card_value = first_card_value + second_card_value
    players_hand = f"{first_card_value} and {second_card}"
    player_num_aces = (1 if 'Ace' in first_card else 0) + (1 if 'Ace' in second_card else 0)

    dealers_hand = f"{dealer_first_card} and {dealer_second_card}"
    dealer_card_value = dealer_first_card_value + dealer_second_card_value
    dealer_num_aces = (1 if 'Ace' in dealer_first_card else 0) + (1 if 'Ace' in dealer_second_card else 0)

    player_card_value = adjust_for_aces(player_card_value, player_num_aces)
    if dealer_first_card.startswith('10') or dealer_first_card.startswith('Jack') or dealer_first_card.startswith('Queen') or dealer_first_card.startswith('King') or dealer_first_card.startswith('Ace'):
        print('Dealer waves hand over table and asks: "Insurance?"')
        print("You pretend to think about it: counter's only take insurance if the count is extremely high.")
        time.sleep(1.5)
        print(random.choice(insurance_denial_expression))
    time.sleep(1)
    print(f'\nPlayer Hand: {first_card} and {second_card}')
    if first_card_value < 11 and second_card.startswith('Ace') or second_card_value < 11 and first_card.startswith('Ace'):
        second_card_value += 10
        if first_card_value + second_card_value < MAX_B4_BUST:
            print(f'\nPlayer Has: Soft {first_card_value + second_card_value}\n')
            print(f"Dealer Has: {dealer_first_card} showing.")
            hit_me(player_card_value)
        if first_card_value + second_card_value == MAX_B4_BUST:
            print(f'\nBlackJack -- You Win!\n')

    else:
        print(f'\nPlayer Has: {first_card_value + second_card_value}')
        print(f"Dealer Has: {dealer_first_card} showing.\n")
        double_down = input("Would you like to double down? (y/n):  ")
        if double_down == 'y'.lower():
            double = random_card_from_deck()
            double_value = player_card_value + card_value(double)
            print("You double down.")
            time.sleep(1)
            print(double)
            print(f"Player Now Has: {double_value}\n")
            if double_value > MAX_B4_BUST:
                print("You Bust. Dealer Wins.")
                time.sleep(2)
                sys.exit()
            else:
                print("Good Luck")
                dealer_moves(dealer_card_value, player_card_value)
        hit_me(player_card_value)

        dealer_moves(dealer_card_value, player_card_value)
