import random

potA = ["Real Madrid", "Napoli", "Porto", "Bayern Munich", "Tottenham", "Chelsea", "Manchester City", "Benfica"]
potB = ["Liverpool", "Brugge", "Internazionale", "Eintracht Frankfurt", "Milan", "RB Leipzig", "Borussia Dortmund", "Paris Saint-Germain"]

def can_play(team1, team2):
    if team1 == "Napoli" and team2 in ["Milan", "Internazionale"]:
        return False
    if team1 == "Liverpool" and team2 in ["Manchester City", "Chelsea", "Tottenham"]:
        return False
    if team1 == "Bayern Munich" and team2 in ["Eintracht Frankfurt", "RB Leipzig", "Borussia Dortmund"]:
        return False
    return True

def simulate_round_of_16():
    random.shuffle(potA)
    random.shuffle(potB)
    round_of_16 = []
    for i in range(len(potA)):
        team1 = potA[i]
        for j in range(len(potB)):
            team2 = potB[j]
            if can_play(team1, team2):
                round_of_16.append((team1, team2))
                potB.pop(j)
                break
    return round_of_16

results = simulate_round_of_16()
for match in results:
    print(f"\n{match[0]} vs {match[1]}")
