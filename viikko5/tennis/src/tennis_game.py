class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
            return
        self.player2_score += 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.equal_scores()
        if self.player1_score >= 4 or self.player2_score >= 4:
            return self.score_over_four()
        return self.inequal_scores()
    
    def equal_scores(self):
        options = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
            3: "Deuce",
            4: "Deuce"
        }
        return options[self.player1_score]
    
    def score_over_four(self):
        options = {
            1: "Advantage player1",
            2: "Win for player1",
            3: "Win for player1",
            4: "Win for player1",
            -1: "Advantage player2",
            -2: "Win for player2",
            -3: "Win for player2",
            -4: "Win for player2"
        }
        return options[self.player1_score - self.player2_score]
    
    def inequal_scores(self):
        options = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }
        return f"{options[self.player1_score]}-{options[self.player2_score]}"