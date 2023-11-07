class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.players = reader.get_players()

    def top_scorers_by_nat(self, nat:str):
        players = []
        for player in self.players:
            if player.nationality == nat:
                players.append(player)
        return sorted(players, key=lambda x: x.goals, reverse=True)