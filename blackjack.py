import random
import time
suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

deck_of_cards = []

for i in range(len(suits)):
    for j in range(len(cards)):
        deck_of_cards.append(f"{cards[j]} of {suits[i]}")


def dealer_moves(dealer_hand, player_hand, hit_card):
    print("Dealer Shows his Down Card")
    print(f"Dealer Second Card: {dealer_second_card}")
    time.sleep(1)
    print(f"Dealer Hand: {dealer_hand}")

    if dealer_hand == 21 and player_hand == 21:
        print("You Push.")
    elif 17 <= dealer_hand < 21 and 17 <= player_hand < 21 and player_hand == dealer_hand:
        print("You Push.")
    elif dealer_hand == 21 and player_hand < 21:
        print("Sorry, Dealer Wins.")
    elif 21 > dealer_hand >= 17 and dealer_hand > player_hand:
        print("Sorry, Dealer Wins.")
    elif 21 > player_hand >= 17 and 21 > dealer_hand >= 17 and player_hand > dealer_hand:
        print("You Win.")
        time.sleep(1)
    elif player_hand is int and dealer_hand > 17:
        while True:
            print("Dealer Hits")
            time.sleep(1)
            print(hit_card)
            if dealer_hand >= 16:
                print(hit_card)



def hit_me(players_hand_value, hit_card, hit_card_value):
    while True:
        if players_hand_value < 21:
            boom_or_doom = input('Dealer looks at you and signals towards your hand: \nWould you like to Hit or Stand? (h/s):  ').lower()
            if boom_or_doom == 'h':
                print(f"{hit_card}")
                players_hand_value += hit_card_value
                print(f"You Have: {players_hand_value}")
                if players_hand_value > 21:
                    print("You Bust: Dealer Wins.")
                    break
            elif boom_or_doom == 's':
                print("You stand. Good Luck.")
                break

def random_card_from_deck():
    return random.choice(deck_of_cards)

def card_value(card):
    if card.startswith('Ace'):
        return 1
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
    time.sleep(1)
    print('Dealing...')
    time.sleep(2)
    print(f'\nPlayer First Card: {first_card}\n')
    time.sleep(1)
    print('Dealing...')
    time.sleep(2)
    print(f'\nDealer Up Card: {dealer_first_card}\n')
    time.sleep(1)
    print('Dealing...')
    time.sleep(2)
    print(f'\nPlayer Second Card: {second_card}\n')
    time.sleep(1)
    print('\nDealing Dealer Down Card\n')
    time.sleep(1)


    player_card_value = first_card_value + second_card_value
    players_hand = f"{first_card_value} and {second_card}"
    hit_card = random_card_from_deck()
    value_of_hit_card = card_value(hit_card)

    dealers_hand = f"{dealer_first_card} and {dealer_second_card}"
    dealer_card_value = dealer_first_card_value + dealer_second_card_value

    if dealer_second_card.startswith('10') or dealer_second_card.startswith('Jack') or dealer_second_card.startswith('Queen') or dealer_second_card.startswith('King') or dealer_second_card.startswith('Ace'):
        print('Dealer waves hand over table and asks: "Insurance?"')
        print("You pretend to think about it: counter's only take insurance if the count is extremely high.")
        time.sleep(1.5)
        print(random.choice(insurance_denial_expression))
    time.sleep(1)
    print(f'\nPlayer Hand: {first_card} and {second_card}\n')
    if first_card_value < 11 and second_card.startswith('Ace') or second_card_value < 11 and first_card.startswith('Ace'):
        second_card_value += 10
        if first_card_value + second_card_value < 21:
            print(f'\nPlayer Has: Soft {first_card_value + second_card_value}\n')
            hit_me(player_card_value, )
        if first_card_value + second_card_value == 21:
            print(f'\nBlackJack -- You Win!\n')

    else:
        print(f'\nPlayer Has: {first_card_value + second_card_value}\n')
        hit_me(player_card_value, random_card_from_deck(), value_of_hit_card)

        dealer_moves(dealer_card_value, player_card_value, random_card_from_deck())