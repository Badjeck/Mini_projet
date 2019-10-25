
ville = {
    "Marseille Nimes": 122,
    "Marseille Perpignan": 317,
    "Nimes Perpignan": 203
}

# prend les villes
print("Les villes disponnibles sont Marseille Nimes Perpignan")
print("Ville de départ")
depart = input()
print("ville d'arrivé")
arrive = input()

#récupère la distance
tri = sorted ([depart, arrive])
trajet = "{} {}".format(tri[0], tri[1])
distance = ville.get(trajet)

# acceleration de 10km/h par minute
# 90km/h de moyenne
# toute les 2h, 15min de pause

def acceleration() :
    for 