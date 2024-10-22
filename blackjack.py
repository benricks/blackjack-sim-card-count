import random
import time
suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

deck_of_cards = []

for i in range(len(suits)):
    for j in range(len(cards)):
        deck_of_cards.append(f"{cards[j]} of {suits[i]}")


def adjust_for_aces(hand_value, num_aces):
    while hand_value > 21 and num_aces > 0:
        hand_value -= 10  # Treat an Ace as 1 instead of 11
        num_aces -= 1
    return hand_value


def dealer_moves(dealer_hand, player_hand_value):
    print(f"Dealer Shows his Down Card: {dealer_second_card}")
    time.sleep(1)
    print(f"Dealer Hand: {dealer_hand}")
    if dealer_hand == 21 and player_hand_value == 21:
        print("Dealer reluctantly, knocks on the table in front of your bet. You Push.")
    elif 'Ace' and 'Jack' in dealers_hand or 'Ace' and 'King' in dealers_hand or 'Ace' and 'Queen' in dealers_hand or 'Ace' and '10' in dealers_hand:
        print("Dealer Wins. Blackjack.")
    while True:
        if 17 <= dealer_hand < 21 and 17 <= player_hand_value < 21 and player_hand_value == dealer_hand:
            print("Dealer knocks on the table in front of your bet. You Push.")
            break
        elif dealer_hand == 21 and player_hand_value < 21:
            print("Sorry, Dealer Wins.")
            break
        elif 21 > dealer_hand >= 17 and dealer_hand > player_hand_value:
            print("Sorry, Dealer Wins.")
            break
        elif 21 > player_hand_value >= 17 and 21 > dealer_hand >= 17 and player_hand_value > dealer_hand:
            print("You Win.")
            time.sleep(1)
            break
        else:
            print("Dealer Hits")
            time.sleep(1)
            random_card = random_card_from_deck()
            print(random_card)
            if random_card.startswith('Ace') and dealer_hand > 11:
                ace = 11
                dealer_hand += ace
            dealer_hand += card_value(random_card)
            print(f"Dealer Has: {dealer_hand}.")
            time.sleep(1)
            if dealer_hand < 16 and 16 < player_hand_value < 21 and player_hand_value > dealer_hand:
                print("You Win.")
                break
            elif dealer_hand > 21:
                print("Dealer Busts. You Win!")
                break


def hit_me(players_hand_value):
    while True:
        if players_hand_value < 21:
            boom_or_doom = input('Dealer looks at you and signals towards your hand: \nWould you like to Hit or Stand? (h/s):  ').lower()
            if boom_or_doom == 'h':
                random_card = random.choice(deck_of_cards)
                print(f"{random_card}")
                players_hand_value += card_value(random_card)
                print(f"You Have: {players_hand_value}")
                if players_hand_value > 21:
                    print("You Bust: Dealer Wins.")
                    break
            elif boom_or_doom == 's':
                print("You stand. Good Luck.")
                break
    return players_hand_value


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
    # print('Dealing...')
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
        if first_card_value + second_card_value < 21:
            print(f'\nPlayer Has: Soft {first_card_value + second_card_value}\n')
            print(f"Dealer Has: {dealer_first_card} showing.")
            hit_me(player_card_value)
        if first_card_value + second_card_value == 21:
            print(f'\nBlackJack -- You Win!\n')

    else:
        print(f'\nPlayer Has: {first_card_value + second_card_value}')
        print(f"Dealer Has: {dealer_first_card} showing.\n")
        hit_me(player_card_value)

        dealer_moves(dealer_card_value, player_card_value)
