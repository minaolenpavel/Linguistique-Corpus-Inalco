import re

class Occurrence:
    def __init__(self, line:re.Match):
        self.isInitial:bool = False
        self.Etat_depart:str
        self.Transition:str = "-"
        self.Label:str
        self.Etat_final:str
        self.isFinal:bool = False
        self.formalize_line(line)

    def formalize_line(self, line:re.Match):
        groups = line.groups()
        print(groups)
        if groups[0] == "^":
            self.isInitial = True
            self.Etat_depart = groups[1]
            self.Label = groups[2]
            self.Etat_final = groups[3]
            if groups[4] == "+":
                self.isFinal = True
        else:
            self.Etat_depart = groups[0]
            self.Label = groups[1]
            self.Etat_final = groups[2]
            if groups[3] == "+":
                self.isFinal = True
    
    def __str__(self):
        return f"{'^' if self.isInitial else ''} {self.Etat_depart} {self.Transition} {self.Label} {self.Etat_final} {'+' if self.isFinal else ''}"



sample = []
with open("gram2.txt", mode='r', encoding='utf-8') as file:
    for line in file:
        sample.append(line.strip())

pattern_circo = re.compile(r'^(\^) ([A-Z]) - ([a-z]) ([A-Z]) (\+)?')
pattern_wcirco = re.compile(r'([A-Z]) - ([a-z]) ([A-Z]) (\+)?')
pattern = r'(\^ )?[A-Z] - [a-z] [A-Z] (\+)?\n'

#sample = "^A - a A + \nB - b C + \nC - c D + \nD - d E \nY - z A +".splitlines()

circo_match = False
matches = []
for line in sample:
    if line.startswith("^") :
        if not circo_match and pattern_circo.match(line):
            matches.append(pattern_circo.match(line))
            circo_match = True
    else:
        if pattern_wcirco.match(line):
            matches.append(pattern_wcirco.match(line))

occurrences = []
for m in matches:
    occurrence = Occurrence(m)
    occurrences.append(occurrence)
    
for o in occurrences:
    print(o)
