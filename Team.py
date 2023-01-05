class Team:
    team_list = {}

    def add_player_to_team(self, player):
        self.team_list[player.firstname] = player


