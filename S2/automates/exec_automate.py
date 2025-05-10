# 1. Prend un msg et rend une liste du msg puis sort au revoir

# message = input("Entrée un message: ")
message = "le petit château"

liste_msg = message.split()
# mot = "\n".join(liste_msg) # retourne la liste avec des sauts de ligne entre chaque mot
# print(f"Message de départ: {message}\nListe de mot:\n{mot}\nAu revoir !")
print(f"Message de départ: {message}\nListe de mot:\n{liste_msg}\nAu revoir !")

# 2. table de transition d'états des automates

dico_table = {
  "S":{"le":"D"},
  "D":{"petit":"D", "château":"E"},
  "E":{}
}

etat_courant = "S"
etat_finaux = "E"

# print(dico_table.values())


for n in range(len(liste_msg)):
  mot_lst = liste_msg[n]
  if mot_lst in dico_table[etat_courant].keys() :
    print(f"{etat_courant} {mot_lst} {dico_table[etat_courant][mot_lst]}")
    etat_courant = dico_table[etat_courant][mot_lst]
    if etat_courant == etat_finaux:
      if n == len(liste_msg)-1 :
        print(f"{etat_finaux} {mot_lst}")
        print("Bravo, vous êtes arrivé à la fin")
  # elif mot_lst in dico_table[etat_finaux].keys() :
  #   if n == max(len(liste_msg)):
  #     print(f"{etat_finaux} {mot_lst}")
  #     print("Bravo, vous êtes arrivé à la fin")
  else : 
    print("ERROR !")

