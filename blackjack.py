import random
import time
suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

deck_of_cards = []

for i in range(len(suits)):
    for j in range(len(cards)):
        deck_of_cards.append(f"{cards[j]} of {suits[i]}")

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

dealer_1st_question = input('All bets in? (y/n)')
if dealer_1st_question == 'y'.lower():
    first_card = random.choice(deck_of_cards)
    first_card_value = card_value(first_card)
    second_card = random.choice(deck_of_cards)
    second_card_value = card_value(second_card)
    dealer_first_card = random.choice(deck_of_cards)
    dealer_second_card = random.choice(deck_of_cards)
    insurance_denial_expression = ["You Shake Your Head", 'You say, "Nope"', "You wave your hand over the table: declining" ]
    time.sleep(1)
    print('Dealing...')
    print(f'\nPlayer First Card: {first_card}\n')
    time.sleep(1)
    print('Dealing...')
    print(f'\nDealer Up Card: {dealer_first_card}\n')
    time.sleep(1)
    print('Dealing...')
    print(f'\nPlayer Second Card: {second_card}\n')
    time.sleep(1)
    print('\nDealing Dealer Down Card\n')
    if dealer_second_card.startswith('10') or dealer_second_card.startswith('Jack') or dealer_second_card.startswith('Queen') or dealer_second_card.startswith('King') or dealer_second_card.startswith('Ace'):
        print('Dealer waves hand over table and asks: "Insurance?"')
        print("You pretend to think about it: counter's only take insurance if the count is extremely high.")
        time.sleep(1.5)
        print(random.choice(insurance_denial_expression))

    print(f'\nPlayer Hand: {first_card} and {second_card}\n')
    if first_card_value < 11 and second_card.startswith('Ace') or second_card_value < 11 and first_card.startswith('Ace'):
        second_card_value += 10
        print(f'\nPlayer Has: Soft {first_card_value + second_card_value}\n')

    else:
        print(f'\nPlayer Has: {first_card_value + second_card_value}\n')
    boom_or_doom = input("Dealer looks at you and signals towards your hand: \n Would you like to Hit or Stand? (h/s):  ").lower()
    player_hand_value = first_card_value + second_card_value
    if boom_or_doom == 'h':
        print(random.choice(deck_of_cards))


    # if dealer_2nd_question == 'n'.lower():
    #     dealer_2nd_question = input('Insurance? (y/n)')