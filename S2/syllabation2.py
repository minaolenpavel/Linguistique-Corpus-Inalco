import re

def vowel_or_cons(char:str) -> str:
    re_vowels = r'[aAeEiIoOuUyY]'
    re_cons = r'[B-DF-HJ-NP-TV-Zb-df-hj-np-tv-z]'
    re_end = r'#'

    if re.match(re_vowels, char):
        return "V"
    elif re.match(re_cons, char):
        return "C"
    elif re.match(re_end, char):
        return "#"

def map_word(word:str) -> str:
    mapped_word = ""
    for char in word:
        mapped_word += vowel_or_cons(char)
    mapped_word += "#"
    return mapped_word

def combine_map_word(word:str) -> tuple:
    mapped_word = map_word(word)
    return (word, mapped_word)

diagraphs = ["an", "on", "en", "in", "un", "ou", "ai", "ei"]
etat_initial = 'etat_i'
etats_finaux = ['etat_f']
etats = ['etat_i', 'etat_1', 'etat_2', 'etat_3', 'etat_f']
transitions = {'etat_i': {'C': 'etat_1', 'V':'etat_2'}, 'etat_1':{'V':'etat_2', 'C':'etat_3'}, 'etat_2':{'C': 'etat_3', 'V': 'etat_2'}, 'etat_3':{'#': 'etat_f', 'V': 'etat_i', 'C': 'etat_i'}}

msg = "mangerons"

pair = combine_map_word(msg)
etat_courant = etat_initial
mot_syll = []
syllable = []
i = 0
while i < len(pair[1]) - 1:
    char = pair[1][i]
    letter = pair[0][i]

    # Traite le cas des diphtongues
    # Si la paire de lettres est reconnue comme une des diphtongues listées alors on passe le reste de la logique et on ajoute la diphtongue et la consonne qui précède à la syllabe.
    if i+1 < len(pair[1]) and (pair[0][i:i+2] in diagraphs):
        syllable.append(letter)
        syllable.append(pair[0][i+1])
        mot_syll.append(list(syllable))
        syllable.clear()
        i+=2
        continue
    if char in transitions[etat_courant].keys():
        print(f"{etat_courant} {char} {letter} {transitions[etat_courant][char]}")
        etat_prev = etat_courant
        etat_courant = transitions[etat_courant][char]
        if etat_courant in etats_finaux:
            if i == len(pair[1])-1:
                syllable.append(letter)
                mot_syll.append(list(syllable)) # Conversion en liste pour faire une copie
        elif etat_courant in ['etat_1', 'etat_2', 'etat_3']:
            syllable.append(letter)
        elif etat_prev == 'etat_3' and etat_courant == 'etat_i':
            mot_syll.append(list(syllable)) # Conversion en liste pour faire une copie
            syllable.clear()
            syllable.append(letter)
    else:
        print("erreur")
        breakpoint()
        print(f"{etat_courant} {char} {transitions[etat_courant][char]}")
        break
    i+=1

if syllable:
    mot_syll.append(list(syllable))

if len(mot_syll[-1]) == 1 and (vowel_or_cons(mot_syll[-1][0]) == "C"):
    last_cons = mot_syll.pop()
    mot_syll[-1].extend(last_cons)

print(mot_syll)