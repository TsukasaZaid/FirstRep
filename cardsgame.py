import random

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

deck = [(rank, suit) for rank in ranks for suit in suits]

def card_value(card):
    rank = card[0]
    if rank in ['J', 'Q', 'K']:
        return 11 + ['J', 'Q', 'K'].index(rank)
    elif rank == 'A':
        return 14
    else:
        return int(rank)

random.shuffle(deck)

player1 = deck[:26]
player2 = deck[26:]

def play_round(player1_card, player2_card):
    val1 = card_value(player1_card)
    val2 = card_value(player2_card)
    
    print(f"Player 1 plays: {player1_card[0]} of {player1_card[1]}")
    print(f"Player 2 plays: {player2_card[0]} of {player2_card[1]}")
    
    if val1 > val2:
        print("Player 1 wins the round!\n")
        return 'Player 1'
    elif val2 > val1:
        print("Player 2 wins the round!\n")
        return 'Player 2'
    else:
        print("It's a tie!\n")
        return 'Tie'

while player1 and player2:
    input("Press Enter to draw cards...")

    p1_card = player1.pop(0)
    p2_card = player2.pop(0)
    
    round_winner = play_round(p1_card, p2_card)
    
    if round_winner == 'Player 1':
        player1.extend([p1_card, p2_card])
    elif round_winner == 'Player 2':
        player2.extend([p2_card, p1_card])
    
    print(f"Player 1 has {len(player1)} cards left.")
    print(f"Player 2 has {len(player2)} cards left.\n")

if len(player1) > len(player2):
    print("Player 1 wins the game!")
else:
    print("Player 2 wins the game!")
