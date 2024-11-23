import ex2, ex3
import dynprog_align

# Conversion des tokens dans un format compatible
tokens1 = dynprog_align.text_to_indexed_obj_lst(" ".join(ex2.tokenizedText()))
tokens2 = dynprog_align.text_to_indexed_obj_lst(" ".join(ex3.nltkTokens()))

aligner = dynprog_align.dynprogalign(tokens1, tokens2)
result = aligner.levenshtein_map()

cleaned_result = []
for i in result:
    for y in i:
        cleaned_result.append(y)

#print(cleaned_result)

#print(f"{cleaned_result[0][0]}; {cleaned_result[0][1][0]}; {cleaned_result[0][2][0][0]}; {cleaned_result[0][3][0][0]}")

#for i, word in enumerate(cleaned_result):
#        try:
#            print(f"{word[0]}; {word[1][0]}; {word[2][0][0]}; {word[3][0][0]}")
#        except IndexError:
#            print(word[0], "<EMPTY>")


with open("result.txt", encoding='utf-8', mode="w") as file:
    for i, word in enumerate(cleaned_result):
        # Dans l'ordre : token du flux ex2; index des lettres flux ex2; token du flux ex3; index des lettres flux ex3
        # Utilisation des indices [0] pour éviter d'imprimer les listes nestées et récupérer les valeurs voulues
        # De cette manières les deux flux ont la même structure de données
        try:
            file.write(f"{word[0]}; {word[1][0]}; {word[2][0][0]}; {word[3][0][0]}\n")
        except IndexError:
            file.write(f"{word[0]}, <EMPTY>\n")


