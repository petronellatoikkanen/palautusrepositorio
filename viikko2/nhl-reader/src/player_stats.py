from player_reader import PlayerReader 

def sorter (self):
    return self.goals+self.assists
    
class PlayerStats: 
    def __init__(self, players):
        self.players = players

    def top_scorers_by_nationality(self, nationality):
        players = self.players.sort(reverse=True, key=sorter)

        players_list = []
        for player in self.players:
            if player.nationality == 'FIN':
                players_list.append(f"{player.name:20} {player.team:5} {player.goals:5} + {player.assists} = {player.goals + player.assists}")

        return players_list
    



