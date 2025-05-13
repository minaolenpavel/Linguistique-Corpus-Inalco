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

def remove_empty_sublists(liste:list) -> list:
    return [x for x in liste if x]

def map_word(word:str) -> str:
    mapped_word = ""
    for char in word:
        mapped_word += vowel_or_cons(char)
    mapped_word += "#"
    return mapped_word

def map_char(char:list) -> str:
    if len(char) == 1:
        return [vowel_or_cons(char)]
    else:
        return [vowel_or_cons(x) for x in char]

def combine_map_word(word:str) -> tuple:
    mapped_word = map_word(word)
    return (word, mapped_word)

def couple_cons(text:str):
    text = list(text)
    word = []
    cons = []
    vows = []
    for i, char in enumerate(text):
        if vowel_or_cons(char) == "C":
            cons.append(char)
            if i+1 < len(text):
                if (char.lower() == "n" or char.lower() =="m") and vowel_or_cons(text[i-1]) == "V" :
                    word.append(list(cons))
                    cons.clear()
                if vowel_or_cons(text[i+1]) == "V":
                    word.append(list(cons))
                    cons.clear()
        elif vowel_or_cons(char) == "V":
            vows.append(char)
            if i+1 < len(text):
                if vowel_or_cons(text[i+1]) == "C":
                    word.append(list(vows))
                    vows.clear()
        else:
            continue
    if len(cons) > 0 or len(vows) > 0:
        word.append(list(cons))
        word.append(list(vows))
    return ["".join(x) for x in word if x != []]

def syllabation(word:list):
    print(word)
    etat_initial = 'etat_i'
    etat_final = 'etat_f'
    etats = ['etat_i', 'etat_1', 'etat_2', 'etat_3', 'etat_f']
    transitions = {'etat_i': {'C': 'etat_1', 'V':'etat_2'}, 'etat_1':{'V':'etat_2', 'C':'etat_1'}, 'etat_2':{'C': 'etat_3', 'V': 'etat_2'}, 'etat_3':{'#': 'etat_f', 'V': 'etat_i', 'C': 'etat_i'}}

    etat_courant = etat_initial
    mot_syll = []
    syllable = []
    i = 0
    char = word[i]
    while i < len(word):
        mapped_char = vowel_or_cons(char)
        if mapped_char in transitions[etat_courant].keys():
            print(f"{etat_courant} {char} {mapped_char} {transitions[etat_courant][mapped_char]}")
            print(syllable)
            print(mot_syll)
            etat_prev = etat_courant
            etat_courant = transitions[etat_courant][mapped_char]
            if etat_courant == etat_final:
                pass
            elif etat_courant == "etat_1":
                syllable.append(char)
            elif etat_courant == "etat_2":
                if i+1 < len(word):
                    if (word[i+1].lower() == "m" or word[i+1].lower() == "n") and vowel_or_cons(word[i+2]) == "C":
                        syllable.append(word[i])
                        syllable.append(word[i+1])
                        mot_syll.append(list(syllable))
                        syllable.clear()
                        i+=1
                    else:
                        syllable.append(char)
                else:
                    syllable.append(char)
            elif etat_prev == "etat_3" and etat_courant == "etat_i":
                syllable.append(char)
                mot_syll.append(list(syllable))  
                syllable.clear()
            elif etat_courant == "etat_3":
                mot_syll.append(list(syllable))
                syllable.clear()
                syllable.append(char)
            i+=1
        if i < len(word):
            char = word[i]
        else:
            break
        
    if syllable:
        mot_syll.append(list(syllable))
        syllable.clear()
    print(syllable)
    mot_syll = remove_empty_sublists(mot_syll)
    if len(mot_syll[-1]) == 1:
        mot_syll[-2].extend(mot_syll.pop())
    print(mot_syll)




msg ="champagne"

msg = couple_cons(msg)
syllabation(msg)




