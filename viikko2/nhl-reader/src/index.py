import requests
from player import Player 

def filter_players(player:dict):
    return player["nationality"] == "FIN"

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    player_dicts = list(filter(filter_players, response))
    players = []

    for player_dict in player_dicts:
        player = Player(player_dict)
        players.append(player)

    print("Players from FIN:\n")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
