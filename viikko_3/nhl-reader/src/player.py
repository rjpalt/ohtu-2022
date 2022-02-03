class Player:
    def __init__(self, name: str, nationality: str, assists: int, goals: int, penalties: int, team: str, games: int):

        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games

    def getPoints(self):

        return self.goals + self.assists
    
    def __str__(self):
        return f'{self.name:25}{self.team} {str(self.goals):>3} + {str(self.assists):>2} = {str(self.getPoints()):>3}'
