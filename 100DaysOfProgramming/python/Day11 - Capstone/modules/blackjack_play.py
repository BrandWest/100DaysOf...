import time

from modules import blackjack_scores
from modules import blackjack_printing
from modules import blackjack_get_cards

def dealer_plays(dealers_cards):
    total = 0
    while total <= 16 or total > 21 and (dealers_cards['dealer']['status'] != 'bust' or dealers_cards['dealer']['status'] != 'stay'):
        total = blackjack_scores.calculate_players_total(dealers_cards, "dealer")
        blackjack_printing.print_hand(dealers_cards, "dealer")        
        if total <= 16:
            print(f"Dealer has {total} less than 16. Hit!")
            dealers_cards = blackjack_get_cards.hit(players_cards=dealers_cards, player="dealer")
            dealers_cards['dealer']['status'] = "hit"
            
        elif total > 16 and total <= 21:
            dealers_cards['dealer']['status'] = "stay"
            return 1
        elif total > 21:
            dealers_cards['dealer']['status'] = "bust"
            return 1
        time.sleep(2)
        
    
def play(players, players_remaining):
    playing = True
    busts = 0
    players_cards, dealers_cards = blackjack_get_cards.deal(players)
    
    while playing:
        for player in players_cards:
            blackjack_printing.print_hand(players_cards, player)
            players_total = blackjack_scores.calculate_players_total(players_cards, player)
            print(f"{player} has {players_total}!")
            next_card = True
            if players_cards[player]["status"] == 'play':
                while next_card:
                    if players_cards[player] == 'stay':
                        next_card = False
                    elif players_cards[player] == "bust":
                        next_card = False
                    else:
                        decision = input(f"{player} do you want to hit, or stay? ")
                        if 'stay' == decision:
                            next_card = False
                            players_cards[player]["status"] = "stay"
                        elif decision == "hit":
                            print("Hit Me!")
                            print(players_cards, player)
                            players_cards = blackjack_get_cards.hit(player=player, players_cards=players_cards)
                            blackjack_printing.print_hand(players_cards, player)
                            players_total = blackjack_scores.calculate_players_total(players_cards, player)
                            print(f"{player} has {players_total}!")
                            if players_total > 21:
                                print(f"{player} Busts with {players_total}.")
                                players_cards[player]["status"] = "bust"
                                next_card = False
                                break
                        else:
                            print("Did you make a mistake?")
                
            else:
                next_card = False
        for player in players_cards:
            if players_cards[player]["status"] == "bust":
                busts += 1
        
        if busts != len(players_cards):
            dealers_turn = dealer_plays(dealers_cards)
        else:
            print("Players bust, dealer wins!")
            playing = False

        if playing == True:
            if dealers_turn == 1:
                blackjack_scores.get_scores(dealers_cards, players_cards)
                playing = False  
            else: 
                playing = False