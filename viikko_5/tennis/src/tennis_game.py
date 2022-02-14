from shutil import register_unpack_format


class TennisGame:

    def __init__(self, p1_name, p2_name):

        self.player1_name = p1_name
        self.player2_name = p2_name
        self.numeral_score_player1 = 0
        self.numeral_score_player2 = 0
        self.stringified_points = ["Love", "Fifteen", "Thirty", "Forty"]


    def won_point(self, player_name):
        
        if player_name == self.player1_name:
            self.numeral_score_player1 += 1
        else:
            self.numeral_score_player2 += 1
    

    def check_if_scores_are_equal(self, score_p1: int, score_p2: int) -> bool:

        return score_p1 == score_p2



    def check_if_advantage_situation(self, score_p1: int, score_p2: int) -> bool:

        return self.numeral_score_player1 >= 4 or self.numeral_score_player2 >= 4



    def determine_advantage_winner(self, score_p1, score_p2) -> int:

            score_difference = score_p1 - score_p2

            if score_difference == 1:
                return "Advantage player1"
            elif score_difference == -1:
                return "Advantage player2"
            elif score_difference >= 2:
                return "Win for player1"
            else:
                return "Win for player2"



    def get_score(self):

        # Handle tie scores
        if self.check_if_scores_are_equal(self.numeral_score_player1, self.numeral_score_player2):

            if self.numeral_score_player1 >= len(self.stringified_points):
                return "Deuce"
            else:
                return self.stringified_points[self.numeral_score_player1] + "-All"


        # Handle tie-breaks / Advantage situations
        elif self.check_if_advantage_situation(self.numeral_score_player1, self.numeral_score_player2):            
            return self.determine_advantage_winner(self.numeral_score_player1, self.numeral_score_player2)


        # Handle rest of situations
        else:
            return self.stringified_points[self.numeral_score_player1] + "-" + self.stringified_points[self.numeral_score_player2]
