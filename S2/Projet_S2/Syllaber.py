import re, process_xml

class Syllaber:
    def __init__(self):
        self.etat_initial = 'etat_i'
        self.etat_final = 'etat_f'
        self.etats = ['etat_i', 'etat_1', 'etat_2', 'etat_3', 'etat_f']
        self.transitions = {'etat_i': {'C': 'etat_1', 'V':'etat_2'}, 'etat_1':{'V':'etat_2', 'C':'etat_1'}, 'etat_2':{'C': 'etat_3', 'V': 'etat_2'}, 'etat_3':{'#': 'etat_f', 'V': 'etat_i', 'C': 'etat_i'}}

    def vowel_or_cons(self, char: str) -> str:
        """
        Détermine si le caractère est une voyelle, une consonne ou autre chose.
        """
        char = char.lower()
        re_vowels = r'[aeiouyàâäéèêëîïôöùûüÿ]'
        re_cons = r'[b-df-hj-np-tv-zç]'
        re_end = r'#'

        if re.match(re_vowels, char):
            return "V"
        elif re.match(re_cons, char):
            return "C"
        elif re.match(re_end, char):
            return "#"
        else:
            return "X"


    def remove_empty_sublists(self, liste:list) -> list:
        """
        Efface les listes vides au sein d'une liste
        """
        return [x for x in liste if x]

    def couple_letters(self, text:str):
        """
        Travail de pré-traitement pour combiner les consonnes et les voyelles ensembles.
        """
        text = list(text)
        word = []
        cons = []
        vows = []
        for i, char in enumerate(text):
            if self.vowel_or_cons(char) == "C":
                cons.append(char)
                if i+1 < len(text):
                    # Prise en compte des sons nasaux
                    if (char.lower() == "n" or char.lower() =="m") and self.vowel_or_cons(text[i-1]) == "V" :
                        word.append(list(cons))
                        cons.clear()
                    if self.__init__vowel_or_cons(text[i+1]) == "V":
                        word.append(list(cons))
                        cons.clear()
            elif self.vowel_or_cons(char) == "V":
                vows.append(char)
                if i+1 < len(text):
                    if self.vowel_or_cons(text[i+1]) == "C":
                        word.append(list(vows))
                        vows.clear()
            else:
                continue
        # Repêche les consonnes et les voyelles orphelines
        if len(cons) > 0 or len(vows) > 0:
            word.append(list(cons))
            word.append(list(vows))
        return ["".join(x) for x in word if x != []]

    def syll_to_str(self, mot_syll:list) -> str:
        """
        Transforme les listes de syllabes en chaînes de caractères.
        """
        return " ".join(["".join(x) for x in mot_syll]) 

    def merge_if_orphan(self, mot_syll:list) -> list:
        """
        Repêche les lettres orphelines.
        """
        if len(mot_syll) > 1:
            # Prend en compte la taille totale du mot pour éviter de concatener les mots comme "à"
            if len(mot_syll[-1]) == 1:
                mot_syll[-2].extend(mot_syll.pop())
        return mot_syll

    def syllabation(self, word:list):
        """
        Fonction principale qui découpe les mots en syllabes.
        """
        #print(word)
        etat_courant = self.etat_initial
        mot_syll = []
        syllable = []
        i = 0
        char = word[i]
        while i < len(word):
            mapped_char = self.vowel_or_cons(char)
            if mapped_char in self.transitions[etat_courant].keys():
                #print(f"{etat_courant} {char} {mapped_char} {self.transitions[etat_courant][mapped_char]}")
                etat_prev = etat_courant
                etat_courant = self.transitions[etat_courant][mapped_char]
                if etat_courant == self.etat_final:
                    pass
                elif etat_courant == "etat_1":
                    syllable.append(char)
                elif etat_courant == "etat_2":
                    if i+2 < len(word):
                        if (word[i+1].lower() == "m" or word[i+1].lower() == "n") and self.vowel_or_cons(word[i+2]) == "C":
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
            # Prend en compte les caractères diacritiques comme les apostrophes et la ponctuation
            elif mapped_char == 'X':
                #breakpoint()
                syllable.append(char)
                i+=1
            if i < len(word):
                char = word[i]
            else:
                break
        if syllable:
            mot_syll.append(list(syllable))
            syllable.clear()
        #print(syllable)
        mot_syll = self.remove_empty_sublists(mot_syll)
        mot_syll = self.merge_if_orphan(mot_syll)
        #print(mot_syll)
        return mot_syll



if __name__ =="__main__":
    text = process_xml.extract_text("Projet_S2/transcript.xml")
    syllabateur = Syllaber()
    for i in text:
        if not (i.startswith("<") and i.endswith("/>")):
            mots = i.split()
            for m in mots:
                mot_syll = syllabateur.syllabation(m)
                print(syllabateur.syll_to_str(mot_syll), end=" ")
            print("\n")
        else:
            print(i)
    





