import random

def hit(player, players_cards):
    deck, card = get_card()
    print(players_cards)
    players_cards[player][deck].append(card)

    return players_cards

def get_card():
    card = random.randint(1,13)
    deck = int(random.randint(0,3))
    if deck == 0:
        deck = "clubs"
    elif deck == 1:
        deck = "hearts"
    elif deck == 2:
        deck = "spades"
    elif deck == 3:
        deck = "diamonds"
    return deck, card

def deal(names):
    players_cards = {}
    dealer = { "dealer": { 
                    "clubs": [],
                    "hearts": [],
                    "spades": [],
                    "diamonds": [],
                    "status": "play",
                }
    }
    print(players_cards)
    for name in names:
        players_cards = { name: {
                                "clubs": [],
                                "hearts": [],
                                "spades": [],
                                "diamonds": [],
                                "status": "play",
                             }
                        }
    for i in range(2):
        for player in players_cards:    
            deck, card = get_card()
            
            players_cards[player][deck].append(card)

        deck, card = get_card()
        dealer["dealer"][deck].append(card)
    print(players_cards)
    return players_cards, dealer
