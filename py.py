import random

hitCount1 = 0
missCount = 0
runCount1 = 0
count = 0
score1 = 0
innings = 1
hitCount2 = 0
runCount2 = 0
score2 = 0
homeRunCount = []
visitRunCount = []


def hits(team):
    global hit
    global runCount1
    global hitCount1
    global runCount2
    global hitCount2
    global missCount
    global average
    # average=50
    hit = False
    for s in range(0, 8):
        if team == 1:
            average = team1.players[s].average
        else:
            average = team2.players[s].average
    else:
        s = 0
    # print(team)
    if random.randrange(0, 1001) <= average:

        if team == 1:
            hit = True
            hitCount1 += 1

        if team == 2:
            # print("hi")
            hit = True
            hitCount2 += 1

    else:
        missCount += 1


def baseCount(team):
    bases = [False, False, False, False, False, False, False]
    global hit
    global missCount
    global homeRunCount
    global visitRunCount
    score1 = 0
    score2 = 0
    score1_print = ""
    score2_print = ""
    global runCount1
    global runCount2
    while missCount < 3:
        hits(team)
        if hit == True:
            for k in range(0, 8):
                if team == 1:
                    if team1.players[k].speed <= 3 and team1.players[k].speed > 1:
                        advanceType = 3
                        team1.players[k].addTrips()
                    if team1.players[k].speed <= 5 and team1.players[k].speed > 3:
                        advanceType = 2
                        team1.players[k].addDubs()
                    if team1.players[k].power < 10:
                        advanceType = 4
                        team1.players[k].addHR()
                    else:
                        advanceType = 1
                        team1.players[k].addSings()
                else:
                    if team2.players[k].speed <= 30 and team2.players[k].speed > 10:
                        advanceType = 3
                        team2.players[k].addTrips()
                    if team2.players[k].speed <= 50 and team2.players[k].speed > 30:
                        advanceType = 2
                        team2.players[k].addDubs()
                    if team2.players[k].power < 10:
                        advanceType = 4
                        team2.players[k].addHR()
                    else:
                        advanceType = 1
                        team2.players[k].addSings()
            # print("type",advanceType)
            for i in range(2, -1, -1):
                bases[i + advanceType] = bases[i]
            if advanceType == 2:
                bases[0] = False
            if advanceType == 3:
                bases[1] = False
                bases[0] = False
            if advanceType == 4:
                bases[2] = False
                bases[1] = False
                bases[0] = False
            bases[advanceType - 1] = True

            for i in range(3, 7, 1):
                if bases[i] == True:
                    if team == 1:
                        score1 += 1
                        runCount1 += 1
                    if team == 2:
                        score2 += 1
                        runCount2 += 1
                    bases[i] = False

                    # print(bases)
    # print("home score",score1)
    # print("visit score",score2)
    if team == 1:
        homeRunCount.append(score1)
        visitRunCount.append(0)
    if team == 2:
        visitRunCount.append(score2)
        homeRunCount.append(0)
    if missCount == 3:
        missCount = 0
    for g in range(len(homeRunCount)):
        score1_print = score1_print + " " + str(homeRunCount[g])

    for l in range(len(visitRunCount)):
        score2_print = score2_print + " " + str(visitRunCount[l])

    print("home: " + score1_print + " " + str(sum(homeRunCount)) + "R" + " " + str(hitCount1) + "H")
    print("visit: " + score2_print + " " + str(sum(visitRunCount)) + "R" + " " + str(hitCount2) + "H")
    print("Your Team Stats:")
    team1.show_Stats()
    print("The other team's Stats:")
    team2.show_Stats()
    # print("home array",homeRunCount)
    # print("visit array",visitRunCount)
    # print("run count Team 1:",runCount1)
    # print("run count Team 2:",runCount2)
    return team


def startGame():
    innings = 1
    homeRunCount = []
    visitRunCount = []
    team = 1
    k = 0
    while innings < 10:
        if innings % 2 == 0:
            team = 2
        else:
            team = 1
        # print(team)
        baseCount(team)
        missCount = 0
        innings += 1
        k += 1
    if sum(homeRunCount) == sum(visitRunCount):
        innings -= 1
    reset = input("Would you like to play again? Yes or No:")
    reset = reset.lower()
    if reset == "yes":
        change = input("Would you like to change your stats? Yes or No:")
        while change == "yes":
            print("You are this team:")
            print("Name   AVG   SPD   POW")
            team1 = Team()
            team1.add_players()
            keep = input("Do you like your team? yes or no:")
            keep = keep.lower()
            if keep == "no":
                change = "yes"
            else:
                resets()
        if change == "no":
            resets()
    else:
        print("GAME OVER")

        exit()


def resets():
    for o in homeRunCount:
        homeRunCount.remove(o)
    for i in visitRunCount:
        visitRunCount.remove(i)
    score1 = 0
    score2 = 0
    score1_print = ""
    score2_print = ""
    startGame()

    # print("inning:",innings)
    # print("score Team 1:",homeRunCount)
    # print("score Team 2:", visitRunCount)


names = ["Chan  ", 'Ross  ', 'Joey', 'Mike ', 'Luke ', 'Mark ', 'John ', 'Matt', 'Jack']


class Player(object):
    def __init__(self):
        self.name = random.choice(names)
        self.average = random.randint(0, 1001)
        self.speed = random.randint(0, 11)
        self.power = random.randint(0, 101)
        self.single = 0
        self.double = 0
        self.triple = 0
        self.HR = 0

    def displayPlayer(self):
        print(str(self.name) + "    " + str(self.average) + "   " + str(self.speed) + "   " + str(self.power))

    def displayStats(self):
        print(str(self.name) + " " + str(self.single) + " " + str(self.double) + " " + str(self.triple) + " " + str(
            self.HR))

    def addSings(self):
        self.single = self.single + 1

    def addDubs(self):
        self.double = self.double + 1

    def addTrips(self):
        self.triple = self.triple + 1

    def addHR(self):
        self.HR = self.HR + 1


class Team(object):
    def __init__(self):
        self.players = []

    def add_players(self):
        for i in range(0, 9):
            self.players.append(Player())
            self.players[i].displayPlayer()

    def show_Stats(self):
        for i in range(0, 9):
            self.players[i].displayStats()


print("You are playing this team:")
print("Name   AVG   SPD   POW")
team2 = Team()
team2.add_players()
keep = "no"
print("You are this team:")
while keep == "no":
    print("Name   AVG   SPD   POW")
    team1 = Team()
    team1.add_players()
    keep = input("Do you like your team? yes or no:")
    keep = keep.lower()
if keep == "yes":
    startGame()
