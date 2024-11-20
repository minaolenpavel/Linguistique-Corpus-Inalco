from char_extract import extract_char

diacritique:dict = extract_char()
text = []
with open("samples/sample.txt", encoding="UTF-8", mode="r") as file:
    for line in file:
        text.append(line)
    file.close()

modified_text = []
for i in text:
    for key in diacritique.keys():
        if key in i:
            i = i.replace(key, diacritique[key])
    modified_text.append(i)

print(modified_text)

# Optionnellement on peut écrire la liste dans un fichier ?