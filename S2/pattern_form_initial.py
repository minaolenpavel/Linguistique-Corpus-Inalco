import re

sample = []
with open("gram2.txt", mode='r', encoding='utf-8') as file:
    for line in file:
        sample.append(line.strip())

pattern_circo = re.compile(r'^\^ [A-Z] - [a-z] [A-Z] \+?')
pattern_wcirco = re.compile(r'[A-Z] - [a-z] [A-Z] \+?')
pattern = r'(\^ )?[A-Z] - [a-z] [A-Z] (\+)?\n'

#sample = "^A - a A + \nB - b C + \nC - c D + \nD - d E \nY - z A +".splitlines()

circo_match = False
matches = []
for line in sample:
    if line.startswith("^") :
        if not circo_match and pattern_circo.match(line):
            matches.append(line)
            circo_match = True
    else:
        if pattern.match(line):
            matches.append(line)
print(matches)
    
