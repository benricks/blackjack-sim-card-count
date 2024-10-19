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

dealer_1st_question = input('All bets in? (y/n):  ')
if dealer_1st_question == 'y'.lower():
    first_card = random.choice(deck_of_cards)
    first_card_value = card_value(first_card)
    second_card = random.choice(deck_of_cards)
    second_card_value = card_value(second_card)
    dealer_first_card = random.choice(deck_of_cards)
    dealer_second_card = random.choice(deck_of_cards)
    hit_1 = random.choice(deck_of_cards)
    hit_1_value = card_value(hit_1)
    hit_2 = random.choice(deck_of_cards)
    hit_2_value = card_value(hit_2)
    hit_3 = random.choice(deck_of_cards)
    hit_3_value = card_value(hit_3)
    hit_4 = random.choice(deck_of_cards)
    hit_4_value = card_value(hit_4)
    hit_5 = random.choice(deck_of_cards)
    hit_5_value = card_value(hit_5)
    hit_6 = random.choice(deck_of_cards)
    hit_6_value = card_value(hit_6)
    hit_7 = random.choice(deck_of_cards)
    hit_7_value = card_value(hit_7)
    hit_8 = random.choice(deck_of_cards)
    hit_8_value = card_value(hit_8)
    hit_9 = random.choice(deck_of_cards)
    hit_9_value = card_value(hit_9)
    hit_10 = random.choice(deck_of_cards)
    hit_10_value = card_value(hit_10)
    hit_11 = random.choice(deck_of_cards)
    hit_11_value = card_value(hit_11)
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
        if first_card_value + second_card_value == 21:
            print(f'\nBlackJack -- You Win!\n')

    else:
        print(f'\nPlayer Has: {first_card_value + second_card_value}\n')
        boom_or_doom = input("Dealer looks at you and signals towards your hand: \n Would you like to Hit or Stand? (h/s):  ").lower()
        player_hand_value = first_card_value + second_card_value
        if boom_or_doom == 'h':
            print(hit_1)
            player_hand_value += hit_1_value
            print(f"You have {player_hand_value}")
            if player_hand_value > 21:
                h2 = input("Would you like to Hit or Stand? (h/s):  ").lower()
                if h2 == 'h':
                    print(hit_2)
                    player_hand_value += hit_2_value
                    print(f"You have {player_hand_value}")
                    if player_hand_value > 21:
                        h3 = input("Would you like to Hit or Stand? (h/s):  ").lower()
                        if h3 == 'h':
                            print(hit_3)
                            player_hand_value += hit_3_value
                            print(f"You have {player_hand_value}")
                            if player_hand_value > 21:
                                h4 = input("Would you like to Hit or Stand? (h/s):  ").lower()
                                if h4 == 'h':
                                    print(hit_4)
                                    player_hand_value += hit_4_value
                                    print(f"You have {player_hand_value}")
                                    if player_hand_value > 21:
                                        h5 = input("Would you like to Hit or Stand? (h/s):  ").lower()
                                        if h5 == 'h':
                                            print(hit_5)
                                            player_hand_value += hit_5_value
                                            print(f"You have {player_hand_value}")
                                            if player_hand_value > 21:
                                                h6 = input("Would you like to Hit or Stand? (h/s):  ").lower()
                                                if h6 == 'h':
                                                    print(hit_6)
                                                    player_hand_value += hit_6_value
                                                    print(f"You have {player_hand_value}")
                                                    if player_hand_value > 21:
                                                        h7 = input("Would you like to Hit or Stand? (h/s):  ").lower()
                                                        if h7 == 'h':
                                                            print(hit_7)
                                                            player_hand_value += hit_7_value
                                                            print(f"You have {player_hand_value}")
                                                            if player_hand_value > 21:
                                                                h8 = input("Would you like to Hit or Stand? (h/s):  ").lower()
                                                                if h8 == 'h':
                                                                    print(hit_8)
                                                                    player_hand_value += hit_8_value
                                                                    print(f"You have {player_hand_value}")
                                                                    if player_hand_value > 21:
                                                                        h9 = input("Would you like to Hit or Stand? (h/s):  ").lower()
                                                                        if h9 == 'h':
                                                                            print(hit_9)
                                                                            player_hand_value += hit_9_value
                                                                            print(f"You have {player_hand_value}")
                                                                            if player_hand_value > 21:
                                                                                h10 = input("Would you like to Hit or Stand? (h/s):  ").lower()
                                                                                if h10 == 'h':
                                                                                    print(hit_10)
                                                                                    player_hand_value += hit_10_value
                                                                                    print(f"You have {player_hand_value}")
                                                                                    if player_hand_value > 21:
                                                                                        h11 = input("Would you like to Hit or Stand? (h/s):  ").lower()
                                                                                        if h11 == 'h':
                                                                                            print(hit_11)
                                                                                            player_hand_value += hit_11_value
                                                                                            print(f"You have {player_hand_value}")




