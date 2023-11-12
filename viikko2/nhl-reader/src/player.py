class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nation = dict['nationality']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.points = int(self.goals) + int(self.assists)
    
    def __str__(self):
        return f"{self.name:20}" + f"{str(self.team):5}" + f"{str(self.goals):3}" + f"{'+':3}" + f"{str(self.assists):3}" + f"{'=':3}" + f"{str(self.points):3}"
