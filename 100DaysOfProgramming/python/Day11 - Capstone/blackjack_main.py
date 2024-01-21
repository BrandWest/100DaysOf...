from modules import blackjack_how_to_play
from modules import blackjack_play

def get_player_info(number_of_players):
    """
    get_player_info Get the players in the game

    Loop through the number of players provided by the player

    :param number_of_players: The number of players playing
    :type number_of_players: int
    :return: The dictionary of players {name:score}
    :rtype: dictionary
    """
    players = []

    for index in range(int(number_of_players)):
        print(index)
        name = input(f"What is Player {index+1}'s name? ")
        players.append(name)

    return players        

if __name__ == "__main__":
    play_again = True
    number_of_players = input("How many players are playing? ")
    if input("Do you know how to play? Y/N ").lower() == "n":
        blackjack_how_to_play.how_to()
    players_info = get_player_info(number_of_players)
        
    while play_again:
        blackjack_play.play(players_info, number_of_players)
        while True:
            decision = input ("Do you want to play again? ")
            if decision == 'n':
                play_again = False
                break
            elif decision == 'y':
                break
            else:
                print("Did you make a mistake?")
