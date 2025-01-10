GRACE = {"NOUN" : "N", 
        "VERB" : "V",
        "AUX" : "V",
        "PRON": "P", 
        "ADJ" : "A",
        "DET":"D",
        "ADV" : "R",
        "SCONJ" : "Cs",
        "CCONJ" : "Cc",
        "UH" : "I", # Selon la documentation du tagger (https://aclanthology.org/J93-2004.pdf), l'interjection est UH, je l'ai ajouté tout en sachant qu'il n'y en a pas dans la DDHC. 
        "PUNCT" : "F",
        "NUM" : "NUM" # Marqué en numéro pour la traduction de l'annotation, va être plus tard formalisée précisement 
        }
# Liste les terminaisons des participes passé (ou au minimum des plus courants)
TERM_PARTICIPE = ("é", "ée", "és", "ées", "t", "te", "ts", "tes", "i", "ie", "is", "ies", "s", "se", "ses", "u", "ue", "us", "ues")

def verb(word:str, index:int):
    pattern = "V"
    # Analyse si le nom suivant dans le corpus est classé comme un participe, si oui, alors le string "word" est considéré comme un verbe auxiliaire 
    # Possibilité de noter tous les index et les retenir comme des participes
    if corpus_grace[index+1][1] == "V":
        if corpus_grace[index+1][0].endswith(TERM_PARTICIPE):        
            pattern += "a"
        

corpus = []
with open("S1/Projet2/DDHC_A.txt", "r", encoding='utf-8') as file:
    for line in file:
        split_line = line.strip().split(" ")
        corpus.append(split_line)
    file.close()


corpus_grace = []
for i in corpus:
    for keys, value in GRACE.items():
        if i[1] == keys:
            if i[0] == "l'instant":
                corpus_grace.append((i[0], "Ncms"))
            else:
                corpus_grace.append((i[0], value))


for i, item in enumerate(corpus_grace):
    if item[1] == "V":
        verb(item[0], i)

#with open("S1/Projet2/DDHC_B.txt", "w", encoding='utf-8') as file:
#    for i in corpus_grace:
#        file.write(f"{i[0]} {i[1]}\n")

