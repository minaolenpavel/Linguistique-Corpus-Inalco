import re

pattern_marcher = r"\b[Mm]arch(?!and|age)\w*\b"

text = []
with open("dimaju.txt", encoding="utf8", mode="r") as file:
    for line in file:
        if line.strip():
            text.append(line.strip())
text = " ".join(text)

prefiltrage = re.findall(pattern_marcher, text)
pattern_groups= r"([Mm]arch)(\w*)"
#with open("terminaisons.txt", encoding="utf8", mode="w") as file:
#    for i in prefiltrage:
#        file.write(re.findall(pattern_groups, i)[0][1]+"\n")
#    file.close()

terminaisons = []
with open("terminaisons.txt", encoding="utf8", mode="r") as file:
    for line in file:
        terminaisons.append(line.strip())
terminaisons = list(set(terminaisons))

pattern = r"\b([Mm]arch)("
for term in terminaisons:
    pattern+=term+r"|"
pattern+=r")\b"
filtrage = re.findall(pattern, text)
for i in filtrage:
    print("".join(i))