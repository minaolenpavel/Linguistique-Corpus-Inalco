
GRACE = {"NOUN" : "N", 
        "VERB" : "V",
        "AUX" : "V",
        "PRON": "P", 
        "ADJ" : "A",
        "ADP" : "S", # ADP = Adposition, parapluie pour post/pré.positions
        "DET":"D",
        "ADV" : "R",
        "SCONJ" : "Cs",
        "CCONJ" : "Cc",
        "UH" : "I", # Selon la documentation du tagger (https://aclanthology.org/J93-2004.pdf), l'interjection est UH, je l'ai ajouté tout en sachant qu'il n'y en a pas dans la DDHC. 
        "PUNCT" : "F",
        "NUM" : "NUM", # Marqué en numéro pour la traduction de l'annotation, va être plus tard formalisée précisement 
        "PROPN" : "PROPN" # Marqué en nom propre pour la traduction de l'annotation, va être plus tard formalisée précisement 
        }
# Resources verbs
TERM_PARTICIPE_PASSE = ("é", "ée", "és", "ées", "t", "te", "ts", "tes", "i", "ie", "is", "ies", "s", "se", "ses", "u", "ue", "us", "ues")
TERM_PARTICIPE_PRESENT = "ant"
TERM_INF = ("ir", "er", "re", "oir", "ire")
TERM_SUBJ = ("isse", "isses", "issions", "issiez", "issent", "e", "es", "ions", "iez", "ent")
TERM_CONDITIONNEL_PRESENT = ("erais", "erait", "erions", "eriez", "eraient", "irais", "irait", "irios", "iriez", "iraient", "rais", "rait", "rios", "riez", "raient")
TERM_FUTUR_S = ("rai", "ras", "ra", "rons", "rez", "ront")
AUXILIAIRES = ("être", "avoir", "suis", "es", "est", "sommes", "êtes", "sont",  "été", "étais", "étais", "était", "étions", "étiez", "étaient","serai", "seras", "sera", "serons", "serez", "seront",  "serais", "serais", "serait", "serions", "seriez", "seraient",  "sois", "sois", "soit", "soyons", "soyez", "soient", "ai", "as", "a", "avons", "avez", "ont", "eu", "avais", "avais", "avait", "avions", "aviez", "avaient", "aurai", "auras", "aura", "aurons", "aurez", "auront",  "aurais", "aurais", "aurait", "avions", "aviez", "auraient", "aie", "aies", "ait", "ayons", "ayez", "aient", "n'est", "n'ai", "n'as", "n'a", "n'avons", "n'avez", "n'ont", "n'étais", "n'était", "n'étions", "n'étiez", "n'étaient", "n'aurai", "n'auras", "n'aura", "n'aurons", "n'aurez", "n'auront", "n'aurais", "n'aurais", "n'aurait", "n'avions", "n'aviez", "n'auraient", "n'aie", "n'aies", "n'ait", "n'ayons", "n'ayez", "n'aient")
TERM_1_PERSON_PLURAL = ("ons", "sommes")
TERM_2_PERSON_PLURAL = ("ez", "êtes")
TERM_3_PERSON_PLURAL = ("ent", "ont")

# Resources nouns
TERM_MASC = ('oir', 'age', 'gramme', 'scope', 'drome', 'er', 'phone', 'mètre', 'ment', 'isme', 'cide')
TERM_FEM = ('manie', 'nomie', 'ine', 'erie', 'ssion', 'ure', 'ite', 'esse', 'logie', 'thérapie', 'tion', 'phobie', 'sion', 'ette', 'ie', 'té', 'ée', 'ence', 'ance')

# Resources pronouns 
PRO_PERS_SUJ = ('je','nous', 'tu','vous', 'il', 'elle', 'ils', 'elles')
PRO_PERS_COD = ('me', 'nous', 'te','vous', 'le', 'la', "l'", 'les', 'en')
PRO_PERS_COI = ('me', 'nous', 'te', 'vous', 'lui', 'leur', 'y')
PRO_DEM = ('celui', 'celle', 'ceux', 'celles', 'celui-ci', 'celle-ci', 'ceux-ci', 'celles-ci', 'celui-là', 'celle-là', 'ceux-là', 'celles-là')
PRO_IND = ('certain', 'chaque', 'aucun', 'quelques', 'tout', 'tous', 'plusieurs', 'nul')
PRO_POS = ('le mien',  'le nôtre', 'le tien', 'le vôtre', 'le sien', 'le leur', 'les miens',  'les nôtres', 'les tiens', 'les vôtres','les siens', 'les leurs')
PRO_INT = ('lequel', 'laquelle', 'lesquels', 'lesquelles')
PRO_REL = ("qu'", 'qui', 'que', 'dont', 'lequel', 'laquelle', 'lesquels', 'lesquelles')
PRO_REF = ('se', 'soi')
PRO_CAR = ('un', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept', 'huit', 'neuf', 'dix')

# Resources determiners
DET_ART_DEF = ('le', 'la', 'les', "l'", "aux")
DET_ART_IND = ('un', 'une', 'des', 'de', 'du')
DET_DEM = ('ce', 'cet', 'cette', 'ces')
DET_POS = ('mon', 'ma', 'mes', 'ton', 'ta', 'tes', 'son', 'sa', 'ses', 'notre', 'nos', 'votre', 'vos', 'leur', 'leurs')
DET_IND = ('certains', 'certaines', 'quelques', 'tout', 'toutes', 'chaque', 'aucun', 'aucune', 'certaine', 'certain', 'tous', 'toute')
DET_INT_EXC = ('quel', 'quelle', 'quels', 'quelles')
DET_REL = ('lequel', 'laquelle', 'lesquels', 'lesquelles')

# Resources adverbs 
ADV_INTER_EXCL = ("pourquoi", "comment", "combien", "où", "quand", "que", "quoi", "comme", "quel", "quelle", "si")
ADV_PARTIC = ("ne", "n'" "pas", "plus", "jamais", "rien", "guère", "aucun", "personne", "nulle part", "non", "afin")


# FUNCTION FOR DEBUG ONLY
def print_context(index:int):
    word_before = corpus_grace[index-1][0]
    word_after = corpus_grace[index+1][0]
    word = corpus_grace[index]
    print(f"Index: {index}")
    print(f"Index -1: {index-1}")
    print(f"Index +1: {index+1}")
    print(f"Word Before: '{word_before}'")
    print(f"Current Word: '{word}'")
    print(f"Word after : {word_after}")
    print(f"Corpus Slice: {corpus_grace[index-2:index+2]}") 
    print("\n")


def verb(word:str, index:int) -> str:
    pattern = "V"
    word_before = corpus_grace[index-1][0]
    word_after = corpus_grace[index+1][0]

    # Type
    if word in AUXILIAIRES:
        if corpus_grace[index+1][1] == "V" or corpus_grace[index+2][1] == "V":
            if word_after.endswith(TERM_PARTICIPE_PASSE) or corpus_grace[index+2][0].endswith(TERM_PARTICIPE_PASSE): 
                pattern += "a"
        else:
            pattern += "m"
    else:
        pattern += "m"

    # Mood
    # Infinitif
    if word.endswith(TERM_INF):
        pattern += "n"
    # Subjonctif
    # Regarde si la form conjuguée a un des terminaisons du subjonctif, si oui, on regarde si le mot qui précède est "qu'elle" ou "qu'il"
    elif word.endswith(TERM_SUBJ) and (word_before == "qu'elle" or word_before == "qu'il"):
        pattern += "s"
    # Participe
    elif word.endswith(TERM_PARTICIPE_PRESENT):
        pattern+= "p"
    elif word.endswith(TERM_PARTICIPE_PASSE) and (("Va" in corpus_grace[index-1][1] or "Va" in corpus_grace[index-2][1]) or word_after == "par"): 
        pattern += "p"
    # Conditionnel 
    elif word.endswith(TERM_CONDITIONNEL_PRESENT):
        pattern += "c"
    # Spécifique pour la forme conjuguée "a" du verbe avoir qui est récurrente
    elif word == "a":
        pattern += "i"
    else:
        pattern += "-"

    # Tense
    if pattern[-1] == "p" and word.endswith(TERM_PARTICIPE_PRESENT):
        pattern += "p"
    elif pattern[-1] == "p" and word.endswith(TERM_PARTICIPE_PASSE):
        pattern += "s"
    elif word.endswith(TERM_FUTUR_S):
        if pattern[-1] == "-":
            pattern = pattern[:-1]
            pattern += "if"
        else:
            pattern+="f"
    else:
        pattern+="-"
    
    # Person
    if word.endswith(TERM_1_PERSON_PLURAL):
        pattern+="1"
    elif word.endswith(TERM_2_PERSON_PLURAL):
        pattern+="2"
    elif word.endswith(TERM_3_PERSON_PLURAL):
        pattern+="3"
    else:
        pattern+="-"

    # Number 
    if word.endswith(TERM_1_PERSON_PLURAL) or word.endswith(TERM_2_PERSON_PLURAL) or word.endswith(TERM_3_PERSON_PLURAL):
        pattern+="p"
    elif pattern[2] == "p":
        if word.endswith("s"):
            pattern+="p"
        else:
            pattern+="s"
    else:
        pattern+="-"

    # Gender
    if pattern[2] == "p":
        if word.endswith("e") or word.endswith("es"):
            pattern+="f"
        else:
            pattern+="m"
    else:
        pattern+="-"
    return pattern

def noun(word:str, index:int, init_pattern:str) -> str:
    pattern = "N"

    # Type
    if init_pattern == "NUM":
        pattern += "k"
    elif init_pattern == "PROPN":
        pattern+="p"
    else:
        pattern += "c" 
    # Gender
    if word.endswith(TERM_MASC):
        pattern+="m"
    elif word.endswith(TERM_FEM):
        pattern+="f"
    else:
        pattern+="-"
    

    return pattern

def pronoun(word:str, index:int) -> str:
    pattern = "P"
    ref_word = word.lower()

    
    # Type
    if ref_word in PRO_PERS_SUJ or ref_word in PRO_PERS_COD or ref_word in PRO_PERS_COI :
        if corpus_grace[index+1][1] == "V":
            pattern+="p"
        else:
            pattern+="s"
    elif ref_word in PRO_DEM:
        pattern+="d"
    elif ref_word in PRO_IND:
        pattern+="i"
    elif ref_word in PRO_POS:
        pattern+="s"
    elif ref_word in PRO_INT:
        pattern+="t"
    elif ref_word in PRO_REL:
        pattern+="r"
    elif ref_word in PRO_REF:
        pattern+="x"
    elif ref_word in PRO_CAR:
        pattern+="k"
    else:
        pattern+="-"

    # Person
    if pattern[1] == "p":
        if ref_word in PRO_PERS_SUJ[0:1] or ref_word in PRO_PERS_COD[0:1] or ref_word in PRO_PERS_COI[0:1]:
            pattern+="1"
        elif ref_word in PRO_PERS_SUJ[2:3] or ref_word in PRO_PERS_COD[2:3] or ref_word in PRO_PERS_COI[2:3]:
            pattern+="2"
        else:
            pattern+="3"
    elif pattern[1] == "s":
        if ref_word in PRO_POS[0:1]:
            pattern+="1"
        elif ref_word in PRO_POS[2:3]:
            pattern+="2"
        else:
            pattern+="3"
    else:
        pattern+="-"

    # Gender
    if "elle" in ref_word:
        pattern+="f"
    else:
        pattern+="m"
    
    # Number
    if "s" in ref_word or "x" in ref_word:
        pattern+="p"
    else:
        pattern+="s"
    
    # Case
    if pattern[1] == "p":
        if ref_word in PRO_PERS_SUJ:
            pattern+="n"
        elif ref_word in PRO_PERS_COD:
            pattern+="a"
        elif ref_word in PRO_PERS_COI:
            pattern+="d"
    else:
        pattern+="-"
    
    # Possessor
    if pattern[1] == "s":
        if "ô" in ref_word or "leur" in ref_word:
            pattern+="p"
        else:
            pattern+="s"
    else:
        pattern+="-"


    return pattern

def determiners(word:str, index:int) -> str:
    pattern ="D"
    ref_word = word.lower()

    # Type
    if ref_word in DET_ART_DEF or ref_word in DET_ART_IND:
        pattern+="a"
    elif ref_word in DET_DEM:
        pattern+="d"
    elif ref_word in DET_POS:
        pattern+="s"
    elif ref_word in DET_IND:
        pattern+="i"
    elif ref_word in DET_INT_EXC:
        pattern+="t"
    elif ref_word in DET_REL:
        pattern+="r"
    else:
        pattern+="-"

    # Person
    if pattern[1] == "s":
        if ref_word.startswith("m") or ref_word.startswith("n"):
            pattern+="1"
        elif ref_word.startswith("t") or ref_word.startswith("v"):
            pattern+="2"
        elif ref_word.startswith("s") or ref_word.startswith("l"):
            pattern+="3"
    else:
        pattern+="-"

    # Gender
    if pattern[1] == "a":
        if ref_word == "la" or ref_word == "une":
            pattern+="f"
        elif ref_word == "le" or ref_word == "un":
            pattern+="m"
        else:
            pattern+="-"
    elif pattern[1] == "d":
        if ref_word == "cette":
            pattern+="f"
        elif ref_word == "ces":
            pattern+="-"
        else:
            pattern+="m"
    elif pattern[1] == "s":
        if "a" in ref_word:
            pattern+="f"
        elif "s" not in ref_word:
            pattern+="m"
    elif pattern[1] == "i":
        if ref_word.endswith(("es", "e")):
            pattern+="f"
        else:
            pattern+="m"
    elif pattern[1] == "t" or pattern[1] == "r":
        if ref_word.endswith(("elle", "elles")):
            pattern+="f"
        else:
            pattern+="m"
    else:
        pattern+="-"

    # Number 
    if ref_word.endswith("s"):
        pattern+="p"
    else:
        pattern+="s"

    # Nature
    if ref_word in DET_ART_DEF:
        pattern+="d"
    elif ref_word in DET_ART_IND:
        pattern+="i"
    else:
        pattern+="-"

    return pattern

def adverbs(word:str, index:int) -> str:
    pattern = "R"
    ref_word = word.lower()

    # Type 
    if ref_word in ADV_INTER_EXCL:
        pattern+="x"
    elif ref_word in ADV_PARTIC:
        pattern+="p"
    else:
        pattern+="g"

    # Degree
    # Ajouter le critère du participe/adjectif qui suit pour le comparatif
    # Eventuellement le fait qu'il soit suivi de "de" ou "que"
    if corpus_grace[index+1][1].startswith(("Vmp", "A")):
        pattern+="c"
    elif ref_word in ADV_PARTIC[0:10]:
        pattern+="n"
    else:
        pattern+="p"

    return pattern




corpus = []
with open("S1/Projet2/DDHC_A.txt", "r", encoding='utf-8') as file:
    for line in file:
        split_line = line.strip().split(" ")
        corpus.append(split_line)
    file.close()


corpus_grace = []
for i in corpus:
    if i[1] in GRACE:
        corpus_grace.append(list((i[0], GRACE[i[1]])))
    else:
        corpus_grace.append(list((i[0], i[1])))



for i, item in enumerate(corpus_grace):
    if item[1] == "V":
        corpus_grace[i] = (item[0], verb(item[0], i))
        #print(item[0], verb(item[0], i))
    elif item[1] == "P":
        corpus_grace[i] = (item[0], pronoun(item[0], i))
        #print(item[0], pronoun(item[0], i))
    elif item[1] == "N" or item[1] == "NUM" or item[1] == "PROPN":
        corpus_grace[i] = (item[0], noun(item[0], i, item[1]))
        #print(item[0], noun(item[0], i, item[1]))
    elif item[1] == "D":
        corpus_grace[i] = (item[0], determiners(item[0], i))
        #print(item[0], determiners(item[0], i))
    elif item[1] == "R":
        corpus_grace[i] = (item[0], adverbs(item[0], i))
        #print(item[0], adverbs(item[0], i))
    elif item[1] == "R":
        corpus_grace[i] = (item[0], adverbs(item[0], i))
        print(item[0], adverbs(item[0], i))


with open("S1/Projet2/DDHC_B.txt", "w", encoding='utf-8') as file:
    for i in corpus_grace:
        file.write(f"{i[0]} {i[1]}\n")

