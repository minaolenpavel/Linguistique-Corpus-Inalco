from automate import * 

def prompt(message:str) -> str:
     return input(message)

def lire(ligne:str)->list:
     liste_caracteres = []
     for c in ligne:
          liste_caracteres.append( c )
     print( 'vous avez entré  les mots : {0}'.format( liste_caracteres  ))
     return liste_caracteres

def automate(liste_mots:list):
     erreur = False
     etat_courant = etat_initial
     #----- la boucle  d'analyse du message par l'automate
     for i in range( 0, len( liste_mots )): 
          token_lu = liste_mots[ i ]
          print( 'dans l\'etat {0} je lis "{1}"'.format( etat_courant , token_lu ))
          print( 'la_liste_des_départs_de_tansition est {0}'.format( les_transitions[ etat_courant ] ))
          if token_lu  in les_transitions[ etat_courant ].keys():
               # il y a une transition  qui part de l'état courant avec le token courant pour label
               print( '\tje passe dans l\'état {0} '.format( les_transitions[ etat_courant ][ token_lu ] ))
               etat_courant = les_transitions[ etat_courant ][ token_lu ]
          else:
               print( 'automate bloqué sur le tokem "{0}" d\'indice  {1}'.format( token_lu, i ))
               print( 'dans l\'état {0} qui n\'a AUCUNE transition avec {1} pour étiquette'.format( etat_courant,
                                                                                                    token_lu ))
               erreur = True
               break
          
     if (etat_courant in  etats_finaux) and (erreur == False):
          if i == (len( liste_mots ) - 1):     # on  a tout lu ?
               print( 'le message est RECONNU' )
          else:
               print( 'message n\'est PAS reconnu complètement' )
               print( 'automat bloqué sur le tokem "{0}" d\'indice  {1}'.format( token_lu, i ))
               print( 'dans l\'état {1}'.format( etat_courant ))
     else:
          print( 'automate n\'ayant PAS traité tous les tokens et arrêté')
          print( 'dans l\'état {0}'.format( etat_courant ))
          print( 'le message n\'est PAS RECONNU' )
     #----- début de la sortie ( réponse si le message fait partie
     # ou non du langage reconnu par  l'automote)
     print( '-----au revoir' )

if __name__ == "__main__":
     liste_mots = lire( prompt('entrez un message svp: ' ))  

