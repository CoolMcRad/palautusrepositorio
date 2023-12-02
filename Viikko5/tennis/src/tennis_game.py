from score import Score

class TennisGame:

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        game_status = TennisGame.get_current_player_statuses(self)
        if TennisGame.is_the_game_a_tie(self):
            game_status = TennisGame.set_status_for_a_tie(self)
        elif TennisGame.endgame_reached(self):
            game_status = TennisGame.calculate_advantage_or_victory(self)

        return game_status
    
    def calculate_advantage_or_victory(self):
        score = self.player1_score - self. player2_score
        if score == 1:
            return "Advantage player1"
        elif score == -1:
            return "Advantage player2"
        elif score >= 2:
            return "Win for player1"
        return "Win for player2"

    def endgame_reached(self):
        if self.player1_score >= 4 or self.player2_score >= 4:
            return True
        return False

    def is_the_game_a_tie(self):
        if self.player1_score == self.player2_score:
            return True
        return False
    
    def set_status_for_a_tie(self):
        if self.player1_score == Score.LOVE.value:
            return "Love-All"
        elif self.player1_score == Score.FIFTEEN.value:
            return "Fifteen-All"
        elif self.player1_score == Score.THIRTY.value:
            return "Thirty-All"
        return "Deuce"

    def get_current_player_statuses(self):
        status = TennisGame.get_player_status(self, self.player1_score)
        status += "-"
        status += TennisGame.get_player_status(self, self.player2_score)
        return status

    def get_player_status(self, players_score):
        if players_score == Score.LOVE.value:
            return "Love"
        elif players_score == Score.FIFTEEN.value:
            return "Fifteen"
        elif players_score == Score.THIRTY.value:
            return "Thirty"
        return "Forty"