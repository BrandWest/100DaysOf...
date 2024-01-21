from modules import blackjack_card_art

def merge_art(cards):
    print(cards)

def print_hand(players_cards, player):
    cards = ""
    if player == "dealer":
        for deck in players_cards["dealer"]:
            if len(players_cards["dealer"][deck]) > 0:
                if deck == "clubs":
                    for card in players_cards["dealer"][deck]:
                        cards += blackjack_card_art.clubs[card]
                elif deck == "diamonds":                    
                    for card in players_cards["dealer"][deck]:
                        cards += blackjack_card_art.diamonds[card]
                elif deck == "spades":                    
                    for card in players_cards["dealer"][deck]:
                        cards += blackjack_card_art.spades[card]
                elif deck == "hearts":                    
                    for card in players_cards["dealer"][deck]:
                        cards += blackjack_card_art.hearts[card]   
        print(cards)
    else:
        print(player)
        for deck in players_cards[player]:
            if len(players_cards[player][deck]) > 0:
                if deck == "clubs":
                    for card in players_cards[player][deck]:
                        cards += blackjack_card_art.clubs[card]
                elif deck == "diamonds":                    
                    for card in players_cards[player][deck]:
                        cards += blackjack_card_art.diamonds[card]
                elif deck == "spades":                    
                    for card in players_cards[player][deck]:
                        cards += blackjack_card_art.spades[card]
                elif deck == "hearts":                    
                    for card in players_cards[player][deck]:
                        cards += blackjack_card_art.hearts[card]                                     

        merge_art(cards)