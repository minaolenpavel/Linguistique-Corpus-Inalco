import re

text = []
with open("robur.txt", encoding='latin1', mode="r") as file:
    for line in file:
        if line != '\n':
            text.append(line.strip())
text = " ".join(text)
print(text)
