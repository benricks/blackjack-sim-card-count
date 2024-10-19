import random

suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

deck_of_cards = []

for i in range(len(suits)):
    for j in range(len(cards)):
        deck_of_cards.append(f"{cards[j]} of {suits[i]}")

simple = input('Would you like to see a deck of cards? (y/n)')
while True:
    if simple.lower() == "n":
        print('Fuck You.')
    else:
        print(deck_of_cards)
        shuff_or_nah = input('Would you like to see them shuffled? (y/n)')
        if shuff_or_nah.lower() == 'y':
            random.shuffle(deck_of_cards)
            print(deck_of_cards)
            break
        while True:
            if shuff_or_nah.lower() == 'n':
                random_card = input("Ok... Would you like to see a random card? (y/n)")
                if random_card.lower() == 'y':
                    print(random.choice(deck_of_cards))
                if random_card.lower() == 'n':
                    break







