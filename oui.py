from math import floor

def oulalajeroule(pdistance) :
# acceleration de 10km/h par minute
#7.5km en 10 min
# 90km/h de moyenne
# toute les 2h, 15min de pause
  km = 0
  x=0
  minutes = 0
  pause = 0
  km_max = pdistance

  while x != 100000:
    minutes += 1
    x += 1
    if km <= km_max:
      if x >= 120: 
        minutes += 120
        x = 0
        km_max -= 7.5
        minutes+=35
        pause +=1
      elif x == 10: #quand on accelère en 10 min...
        km += 7.5 # ...on parcour 7.5km
        km_max -= 7.5
        minutes += 10
      elif x > 11 and x < 109:
        km += 1.5 #on parcour 1.5km par minute en roulant a 90km/h
    else:
      break
  return minutes, pause


ville = {
    "Annecy Marseille":421,
    "Marseille Nimes": 122,
    "Marseille Perpignan": 317,
    "Nimes Perpignan": 203,
}

# prend les villes
print("Les villes disponnibles sont:\nAnnecy\nMarseille\nNimes\nPerpignan")
print("Ville de départ")
depart = input()
print("ville d'arrivé")
arrive = input()

#récupère la distance
tri = sorted([depart.capitalize(), arrive.capitalize()])
trajet = "{} {}".format(tri[0], tri[1])
distance = ville.get(trajet)


oui = oulalajeroule(distance)

heure = floor(oui[0] /60)
minutes = oui[0] % 60

print("Le camionneur a mit {}h{} min avec {} pauses pour aller de {} à {}.".format(heure,minutes,oui[1],depart,arrive))