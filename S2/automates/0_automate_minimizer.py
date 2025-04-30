#------ représentation de l'automate "le petit* chateau" non-minimaliste
alphabet_lexique = ['le', 'petit', 'chateau']
etat_initial = 'S'
etats_finaux = ['E1', 'E2']
les_etats = [ 'S', 'D', 'A', 'E1', 'E2' ]
les_transitions = {'S': {'le':'D'}, 'D': {'petit':'A', 'château':'E1'}, 'A': {'petit': 'A', 'château': 'E2'} }

F = etats_finaux
S = [ e for e in les_etats if e not in F ]

P = [ S, F ]
print( 'P=={0}'.format( P ))

def etats_equiv( G  ):
     new_g_lst =  []
     for a in alphabet_lexique:
          new_g  = []
          for e0 in G:
              if e0 in les_transitions.keys():
                   if a in les_transitions[ e0 ].keys():
                        (a, trgt_e0 ) = [ (k,v) for (k,v) in les_transitions[ e0 ].items() if k==a ][0]
                        eqv_found = False
                        for e1 in G:
                             if (e0 != e1) and (e1 in les_transitions.keys()):
                                  if a in les_transitions[ e1 ].keys():
                                       (a, trgt_e1 ) = [ (k,v) for (k,v) in les_transitions[ e1 ].items() if k==a ][0]
                                       if trgt_e0 == trgt_e1:
                                            if e0 not in new_g:
                                                 new_g.append( e0 )
                                            if e1 not in new_g:
                                                 new_g.append( e1 )
                                            eqv_found = True
                        if not eqv_found:
                             if e0 not in new_g:
                                  new_g.append( e0 )
                                             
          if new_g:
               new_g_lst.append( new_g )
     return new_g_lst

old_P_sz = 0
while old_P_sz != len( P ):
     old_P_sz = len( P )
     new_P = []
     for i in range(0, len( P )):
          curr_g = P[i]
          new_g_lst = etats_equiv( curr_g  )
          if new_g_lst:
               new_P += new_g_lst
          else:
               new_P.append( curr_g )
     P = new_P
print( 'now P== {0}'.format( P  ))

#---- renommer les états
nouveau_etats_map = {}
for G in P:
     name = G[0]
     nouveau_etats_map[ name ] = G

def nouveau_nom( e0 ):
     return [x for x in nouveau_etats_map.keys() if e0 in nouveau_etats_map[ x ]][ 0 ]

nouveau_les_etats = [ x for x in nouveau_etats_map.keys() ]
nouveau_etat_initial = [ x for x in nouveau_les_etats if etat_initial in nouveau_etats_map[ x ]]
nouveau_etat_finaux = [ x for x in nouveau_les_etats if [y for y in etats_finaux if y in nouveau_etats_map[ x ]]]
#----- recréer les transitions avec les nouveaux états
nouveau_les_transitions = {}
for (e0, d) in les_transitions.items():
     nouveau_cibles = {}
     for (a, e1) in d.items():
          nouveau_cibles[ a ]= nouveau_nom( e1 )
     nouveau_les_transitions[ nouveau_nom( e0 ) ] = nouveau_cibles

print( 'nouveau_les_etats== ', nouveau_les_etats )
print( 'nouveau_etat_initial== ',  nouveau_etat_initial )
print( 'nouveau_etat_finaux== ',  nouveau_etat_finaux )
print( 'nouveau_les_transitions== ', nouveau_les_transitions )
print( '-----au revoir' )

print("départ\tarrivée\tfinal")
for keys, values in les_transitions.items():
     for keys1, values1 in values.items():
          print(f"{keys}\t {keys1}\t{values1}")

print("départ\tarrivée\tfinal")
for keys, values in les_transitions.items():
     for keys1, values1 in values.items():
          if keys == "S" and "E" in [i[1] for i in les_transitions[values1].items()]:
               print(f"{keys}\t {keys1}\t{values1}")