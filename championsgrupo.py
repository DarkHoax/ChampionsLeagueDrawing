import random

# Potes de times
pote_a = ["Real Madrid", "Eintracht Frankfurt", "Manchester City", "Milan", "Bayern München", "Paris Saint-Germain", "Porto", "Ajax"]

pote_b = ["Liverpool", "Chelsea", "Barcelona", "Juventus", "Atlético de Madrid", "Sevilla", "RB Leipzig", "Tottenham"]

pote_c = ["Borussia Dortmund", "RB Salzburgo", "Shakhtar Donetsk", "Internazionale", "Napoli", "Benfica", "Sporting", "Bayer Leverkusen"]

pote_d = ["Rangers", "Dínamo Zagreb", "Olympique de Marseille",	"Copenhague", "Brugge", "Celtic", "Viktoria Plzeň", "Maccabi Haifa"]

# Dicionário para armazenar os times de cada grupo
grupos = {"A": [], "B": [], "C": [], "D": [], "E": [], "F": [], "G": [], "H": []}

# Restrições
restricoes = [
    {"times": ["Real Madrid", "Barcelona", "Sevilla", "Atletico Madrid"], "grupos": []},
    {"times": ["Eintracht Frankfurt", "Bayern Munchen", "Borussia Dortmund", "Bayer Leverkusen", "RB Leipzig"], "grupos": []},
    {"times": ["Manchester City", "Liverpool", "Chelsea", "Tottenham"], "grupos": []},
    {"times": ["Milan", "Juventus", "Inter Milan", "Napoli"], "grupos": []},
    {"times": ["Benfica", "Porto", "Sporting CP"], "grupos": []},
    {"times": ["Rangers", "Celtic"], "grupos": []},
    {"times": ["Paris Saint-Germain", "Marseille"], "grupos": []}
]

# Função para verificar se uma determinada restrição está sendo violada em um grupo
def verifica_restricao(time, grupo):
    for restricao in restricoes:
        if time in restricao["times"]:
            if grupo in restricao["grupos"]:
                return True
    return False

# Remove times do mesmo pote que já estão em grupos escolhidos
def remove_opcoes(pote):
    for time in pote:
        for grupo in grupos.values():
            if time in grupo:
                pote.remove(time)

# Itera sobre cada grupo para selecionar os times
for grupo in grupos.keys():
    print(f"Grupo {grupo}:")
    # Seleciona um time de cada pote
    for i in range(4):
        pote = eval(f"pote_{chr(ord('a')+i)}")
        remove_opcoes(pote)
        time = random.choice(pote)
        while verifica_restricao(time, grupo):
            pote.remove(time)
            if len(pote) == 0:
                break
            time = random.choice(pote)
        grupos[grupo].append(time)
        print(f"  {time}")
    print()

# Imprime os times de cada grupo
print("Times de cada grupo:")
for grupo, times in grupos.items():
    print(f"Grupo {grupo}: {', '.join(times)}")
