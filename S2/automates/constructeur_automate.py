def prompt(message:str) -> str:
     return input(message)

# (1)   A FAIRE ENCAPSULER CES LIGNES DE LECTURE DANS UNE FONCTION
def lire(ligne:str)->list:
     liste_caracteres = []
     for c in ligne:
          liste_caracteres.append( c )
     print( 'vous avez entré  les mots : {0}'.format( liste_caracteres  ))
     return liste_caracteres
#------ fin de l'entrée  du message à analyser    
class gestion_nom():
     def __init__( self ):
          self.compteur = 0
     def nom_etat( self ):
          nv = 'etat_' + str( self.compteur )
          self.compteur += 1
          return nv

gnom = gestion_nom()
#--------- les données de l'automate -------
alphabet_lexique = [  ]
etat_initial = gnom.nom_etat()
etats_finaux = [ ]
les_etats = [ etat_initial ]
les_transitions = { }

#----- la boucle  d'analyse du message par l'automate (le "moteur" de l'automate)
erreur = False
etat_courant = etat_initial

phrase = prompt("veuillez entrer une phrase : ")
while phrase != "STOP":
     liste_caracteres = lire( phrase )
     for i in range( 0, len( liste_caracteres )):  
          token_lu = liste_caracteres[ i ]
          if token_lu not in alphabet_lexique:
               alphabet_lexique.append(token_lu)
          print( 'dans l\'etat {0} je lis "{1}"'.format( etat_courant , token_lu ))
          if etat_courant in les_transitions.keys():
               #  l'état courant est une clef de la table de transition, on verrra plus tard
               if token_lu in les_transitions[ etat_courant ].keys():
                    etat_courant = les_transitions[ etat_courant ][ token_lu ]
               else:
                    #  l'état courant n'est pas une clef de la table de transition
                    nouvel_etat = gnom.nom_etat()
                    les_etats.append(nouvel_etat)
                    les_transitions[ etat_courant ][ token_lu ] = nouvel_etat
                    etat_courant = nouvel_etat
          else:
               #  l'état courant n'est pas une clef de la table de transition
               nouvel_etat = gnom.nom_etat()
               les_etats.append(nouvel_etat)
               les_transitions[ etat_courant ] = {  token_lu : nouvel_etat }
               etat_courant = nouvel_etat
     if etat_courant not in etats_finaux:          
          etats_finaux += [ etat_courant ]  #  on enregistre l'état final s'il ne l'est pas déjà.
     phrase = prompt("veuillez entrer une phrase : ")
     etat_courant = etat_initial
print( '-----au revoir' )


# (5) A FAIRE SAUVEGARDER L'AUTOMATE DANS UN FICHIER
with open("automate.py", mode="w") as file:
     file.write(f"alphabet_lexique = {alphabet_lexique}\n")
     file.write(f"etat_initial = '{etat_initial}'\n")
     file.write(f"etats_finaux = {etats_finaux}\n")
     file.write(f"les_etats = {les_etats}\n")
     file.write(f"les_transitions = {les_transitions}\n")
