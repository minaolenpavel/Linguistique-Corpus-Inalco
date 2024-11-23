import nltk
import ex2

text = []
with open("samples/sample2.txt", encoding="UTF-8", mode="r") as file:
    for line in file:
        text.append(nltk.word_tokenize(line))

for line in text:
    for word in line:
        if ex2.wordFormat(word):
            print(ex2.wordFormat(word))