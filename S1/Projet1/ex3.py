import nltk

text = []
with open("Projet1\samples\sample2.txt", encoding="UTF-8", mode="r") as file:
    for line in file:
        text.append(line)

for line in text:
    print(nltk.word_tokenize(line))