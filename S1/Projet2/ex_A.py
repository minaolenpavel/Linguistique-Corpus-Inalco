import nltk
import os 
jar = r"C:\Users\M3500\AppData\Roaming\nltk_data\taggers\stanford-postagger-full-2020-11-17\stanford-postagger.jar"
model = r"C:\Users\M3500\AppData\Roaming\nltk_data\taggers\stanford-postagger-full-2020-11-17\models\french-ud.tagger"

raw = []
with open("S1\Projet2\ddhc.txt", mode='r', encoding='utf-8') as file:
    for line in file:
        raw.append(line.strip())
    file.close()

raw = [x for x in raw if x != ""]
text = " ".join(raw)

tokens = nltk.tokenize.word_tokenize(text)

pos_tagger = nltk.tag.StanfordPOSTagger(model, jar, encoding = 'utf-8')
tagged_text = pos_tagger.tag(tokens)

with open("S1/Projet2/DDHC_A.txt", "w", encoding='utf-8') as file:
    for t in tagged_text:
        file.write(f"{t[0]} {t[1]}\n")
    file.close()





