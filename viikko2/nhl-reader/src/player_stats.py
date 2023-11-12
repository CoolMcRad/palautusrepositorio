class PlayerStats:
    def __init__(self, reader):
        self._reader = reader
        self._players = reader.get_players()

    def points_sort(self):
        def sort_by_points(player):
            return player.points

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_by_points
        )

        return list(sorted_players)

    def nation_sort(self, nation):
        players_of_team = filter(lambda player: player.nation == nation, self._players)
        return list(players_of_team)

    def top_scorers_by_nationality(self, nation):
        self._players = self.nation_sort(nation)
        self._players = self.points_sort()
        return self._players

    def team(self, team_name):
        players_of_team = filter(lambda player: player.team == team_name, self._players)
        return list(players_of_team)

