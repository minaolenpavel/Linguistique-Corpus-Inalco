from unidecode import unidecode

def normalize(mot:str) -> str:
    return unidecode(mot).lower()

def state_trans(current_state:str, mot:str) -> str:
    if mot == "":
        return "B"
    mot = normalize(mot)

    if current_state == "S":
        if mot == "le":
            return "D"
        else:
            return "B"
    elif current_state == "D":
        if mot == "petit":
            return "D"
        elif mot == "chateau":
            return "E"
        else:
            return "B"
    return "B"

current_state = "S"
text = input("Entrez une phrase : ")
mots = text.split()
for i, mot in enumerate(mots):
    print(mot)
    print(current_state)
    current_state = state_trans(current_state, mot)
    print(current_state)
    #breakpoint()
    if current_state == "E":
        print("c'est fini !")
        break
    elif current_state == "B":
        print("bloqué !")
        break
    elif current_state != "E" and i+1 == len(mots):
        print("bloqué")
        break


