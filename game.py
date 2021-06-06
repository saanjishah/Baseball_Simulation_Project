import random

names = ["Bob ", "Joey ", "Steve ", "Mike ", "Luke ", "Mark ", "John ", "Jack ", "Matt "]


class Players(object):
  def _init_(self):
    self.name = random.choice(names)
    self.average = random.randint(0, 101)
    self.power = random.randrange(1, 4)
    self.speed = random.randrange(1, 11)

  def displayPlayer(self):
    print(self.average, " ")


class Team(object):
  def __init__(self):
    self.players = []

  def add_players(self):
    for i in range(0, 9):
      self.players.append(Players())
      self.players[i].displayPlayer()


print("You are playing this team:")
print("Name    AVG   PW   SPD")
team2 = Team()
team2.add_players()


