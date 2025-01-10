GRACE = {"NOUN" : "N", 
        "VERB" : "V",
        "AUX" : "Va",
        "PRON": "P", 
        "ADJ" : "A",
        "DET":"D",
        "ADV" : "R",
        "SCONJ" : "Cs",
        "CCONJ" : "Cc",
        "UH" : "I", # Selon la documentation du tagger (https://aclanthology.org/J93-2004.pdf), l'interjection est UH, je l'ai ajouté tout en sachant qu'il n'y en a pas dans la DDHC. 
        "PUNCT" : "F" }

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
            corpus_grace.append((i[0], value))

print(corpus_grace)

