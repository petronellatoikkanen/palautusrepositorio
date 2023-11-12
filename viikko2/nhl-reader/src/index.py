import requests
from player import Player
from player_reader import PlayerReader
from player_stats import PlayerStats


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    reader = PlayerReader(url)
    players = reader.get_players()
    stats = PlayerStats(players)
    players_list = stats.top_scorers_by_nationality("FIN")
    
    for player in players_list:
        print(player)

if __name__ == "__main__":
    main()
