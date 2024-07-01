class Player:

  def __init__(self, name, team):
    self.name = name
    self.xp = 1500
    self.team = team

  def introduce(self):
    print(f"Hello! I'm {self.name} and I play for {self.team}")


class Team:

  def __init__(self, team_name):
    self.team_name = team_name
    self.players = []
    self.players_sum_xp = 0

  def show_players(self):
    for player in self.players:
      player.introduce()

  def add_player(self, player_name):
    new_player = Player(player_name, self.team_name)
    self.players.append(new_player)

  def remove_player(self, player_name):
    for player in self.players:
      if player.name == player_name:
        self.players.remove(player)
        break

  def sum_xp(self):
    for player in self.players:
      self.players_sum_xp += player.xp
    print(
        f"The Total XP of {self.team_name} Players is {self.players_sum_xp}.")


team_a = Team("Team A")

team_a.add_player("Dorj")
team_a.add_player("Bat")

team_a.show_players()

team_a.remove_player("Bat")
team_a.show_players()

team_b = Team("Team B")

team_b.add_player("Elbegdorj")
team_b.add_player("SukhBaatar")

team_b.show_players()

team_a.sum_xp()
team_b.sum_xp()
