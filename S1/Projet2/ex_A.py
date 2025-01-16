import nltk
import os 
jar = r"C:\Users\M3500\AppData\Roaming\nltk_data\taggers\stanford-postagger-full-2020-11-17\stanford-postagger.jar"
model = r"C:\Users\M3500\AppData\Roaming\nltk_data\taggers\stanford-postagger-full-2020-11-17\models\french-ud.tagger"

raw = []
with open("DDHC.txt", mode='r', encoding='utf-8') as file:
    for line in file:
        raw.append(line.strip())
    file.close()

raw = [x for x in raw if x != ""]
text = " ".join(raw)

tokens = nltk.tokenize.word_tokenize(text)
new_tokens = []
for token in tokens:
    if "'" in token: 
        parts = token.split("'")
        formatted_parts = [part + "'" if i == 0 else part for i, part in enumerate(parts) if part]
        new_tokens.extend(formatted_parts)
    else:
        new_tokens.append(token)

for i, token in enumerate(new_tokens):
    if token == "n" or token == "l":
        new_tokens[i]+="'"

print(new_tokens)

pos_tagger = nltk.tag.StanfordPOSTagger(model, jar, encoding = 'utf-8')
tagged_text = pos_tagger.tag(new_tokens)

with open("DDHC_A.txt", "w", encoding='utf-8') as file:
    for t in tagged_text:
        file.write(f"{t[0]} {t[1]}\n")
    file.close()





