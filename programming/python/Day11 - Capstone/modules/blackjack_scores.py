def calculate_players_aces(players_total, number_of_aces, aces_array):
    is_over = False
    for ace in range(0, len(aces_array)):
        if (players_total + 11) > 21:
            players_total += 1
            is_over = True
        elif is_over == True and number_of_aces > 1:
            playesrs_total -= 11
            players_total += 1
        elif is_over == True:
            players_total += 1
        else:
            players_total += 11
        
    return players_total 

def calculate_players_total(players_cards, player):
    players_total = 0
    aces = []
    num_aces = 0
    
    number_of_cards = 0
    for deck in players_cards[player]:
        number_of_cards += len(players_cards[player][deck])
        for item in players_cards[player][deck]:
            if deck == "status":
                break                
            elif item == 1:
                num_aces += 1
                aces.append(item)
            elif item == 11 or item == 12 or item == 13:
                players_total += 10
            else:
                players_total += item
    players_total =  calculate_players_aces(players_total=players_total,number_of_aces=num_aces, aces_array=aces)

    return players_total        

def get_scores(dealers_cards, players_cards):
    for player in players_cards:
        total = calculate_players_total(players_cards, player)
        players_cards[player]["final_score"] = total
    total = calculate_players_total(dealers_cards, "dealer")
    dealers_cards["dealer"]["final_score"] = total
    verdict(dealers_cards, players_cards)

def verdict(dealers_cards, players_cards):
    high_score = 0
    busts = 0
    players_name = ""
    dealer_wins = False

    for player in players_cards:
        if players_cards[player]["status"] != "bust":
            if players_cards[player]["final_score"] > high_score:
                high_score = players_cards[player]["final_score"] 
                players_name = player

        elif players_cards[player]["status"] == "bust":
            busts += 1
                

    if dealers_cards["dealer"]["status"] != "bust":
        if dealers_cards["dealer"]["final_score"] > high_score and dealers_cards["dealer"]["status"] != "bust":
            dealers_cards["dealer"]["verdict"] = "wins"
            dealer_wins = True
        elif dealers_cards["dealer"]["final_score"] == high_score:
            dealers_cards["dealer"]["verdict"] = "tied"
        elif dealers_cards["dealer"]["final_score"] < high_score:
            dealers_cards["dealer"]["verdict"] = "loses"
        elif busts == len(players_cards):
            dealers_cards["dealer"]["verdict"] = "wins"
            dealer_wins = True           
        
    else:
        dealers_cards["dealer"]["verdict"] = "loses"
    
    if dealers_cards["dealer"]["verdict"] == "tied":  
        if players_cards[player]["final_score"] == dealers_cards["dealer"]["final_score"]:
            print(f"Dealer and {player} tied with a {players_cards[player]['final_score']}!")
        elif dealers_cards["dealer"]["verdict"] == "wins":
            print(f"Dealer won with a {dealers_cards['dealer']['final_score']}")
    
    elif  dealer_wins == True:
        print(f"Dealer wins with a {dealers_cards['dealer']['final_score']}!")
    elif dealer_wins == False :
        print(f"{players_name} won with a {high_score}!")
    
    print(f"\nDealer's cards: {dealers_cards}")

    for player in players_cards:
        print(f"{player}'s cards: {players_cards[player]}")
    print("")