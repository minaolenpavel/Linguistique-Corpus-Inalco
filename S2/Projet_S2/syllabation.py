import re

class Syllabifier:
    def __init__(self):
        self.etat_initial:str = 'etat_i'
        self.etats_finaux:list = ['etat_f']
        self.etats:list = ['etat_i', 'etat_1', 'etat_2', 'etat_3', 'etat_f']
        self.transitions:dict = {'etat_i': {'C': 'etat_1', 'V':'etat_2'}, 'etat_1':{'V':'etat_2', 'C':'etat_3'}, 'etat_2':{'C': 'etat_3', 'V': 'etat_2'}, 'etat_3':{'#': 'etat_f', 'V': 'etat_i', 'C': 'etat_i'}}

    def vowel_or_cons(self, char:str) -> str:
        re_vowels = r'[aAeEiIoOuUyY]'
        re_cons = r'[B-DF-HJ-NP-TV-Zb-df-hj-np-tv-z]'
        re_end = r'#'

        if re.match(re_vowels, char):
            return "V"
        elif re.match(re_cons, char):
            return "C"
        elif re.match(re_end, char):
            return "#"

    def map_word(self, word:str) -> str:
        mapped_word = ""
        for char in word:
            mapped_word += self.vowel_or_cons(char)
        mapped_word += "#"
        return mapped_word

    def combine_map_word(self, word:str) -> tuple:
        mapped_word = self.map_word(word)
        return (word, mapped_word)

    def syllabify(self, text:str):
        msg = text
        pair = self.combine_map_word(msg)
        etat_courant = self.etat_initial
        mot_syll = []
        syllable = []
        for i in range(len(pair[1])-1):
            char = pair[1][i]
            letter = pair[0][i]
            if char in self.transitions[etat_courant].keys():
                print(f"{etat_courant} {char} {letter} {self.transitions[etat_courant][char]}")
                etat_prev = etat_courant
                etat_courant = self.transitions[etat_courant][char]
                if etat_courant in self.etats_finaux:
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
                print(f"{etat_courant} {char} {self.transitions[etat_courant][char]}")
                break
        # Repêchage pour les syllabes qui ont pu être épargnées
        if syllable:
            mot_syll.append(list(syllable))

        return mot_syll

if __name__ == "__main__":
    syllaby = Syllabifier()
    print(syllaby.syllabify("eclectique"))
