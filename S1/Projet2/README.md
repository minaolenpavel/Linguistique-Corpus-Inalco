# Projet №2 Linguistique de Corpus Inalco TAL L3 S1

## Introduction

Ce devoir porte sur l'étiquetage morphosyntaxique de la déclaration des droits de l'Homme et du citoyen de 1789.
L'objectif est d'écrire un script permettant d'étiqueter le corpus sous le format GRACE (*détaillé dans le PDF*) à partir de l'annotation de l'étiqueteur Stanford pour le français.

## Méthodologie 

Après avoir téléchargé le fichier content la déclaration des droits de l'homme et du citoyen, j'ai volontairement tronqué les parties mentionnant le copyright du texte, ainsi que les partie "non-pertinentes".

Après avoir réalisé l'étiquetage avec le postagger de Stanford, j'ai procédé à la conversion vers le format GRACE, ce qui a été plutôt rapide, j'ai alors essayé à travers différent moyens d'écrire un script qui fait un étiquetage précis avec le format GRACE.
Cela est passé non seulement par un grand travail de recherche afin de trouver les flexions qui appartiennent typiquement à un trait, par exemple, les verbes conjugués à la 3ème personne du pluriel finissent nécessairement en *-ent*. Ce premier travail a été fructueux, mais il laissait de côté le genre de la plupart des noms communs. J'ai alors procédé à l'implémentation d'une analyse syntaxique, par exemple, lorsque le script traite un nom qui ne répond à aucune des terminaisons communes du féminin ou du masculin, il regarde le genre grammatical du pronom qui le précède.
Après avoir implémenté cette fonction, la quasi-totalité du travail était faite, il ne restait plus qu'à compléter avec certains mots récurrents qui ne laissaient pas d'indices syntaxiques ou morphologiques en les rentrant manuellement dans le programme.

Après avoir procédé à une relecture de l'étiquetage de référence **DDHC_REF.txt**. J'ai écrit le programme **calcul.py** qui permet de calculer la précision du programme d'étiquetage en comparant pour chaque mot le pattern produit par le script **ex_B.py** ainsi que le contenu du corpus de référence. Une méthode de calcul prend la précision de chaque pattern et fait la moyenne, c'est sur cette méthode de calcul que la précision par catégorie est calculée. La seconde méthode de calcul, ne regarde que la catégorie grammaticale (N, V, D, etc.)

# Analyse des résultats et commentaires

~~~
Précision moyenne par mot = 93.32%
Précision des catégories grammaticales = 99.17%
Les N ont une précision de 85.16%
Les D ont une précision de 94.15%
Les S ont une précision de 96.33%
Les C ont une précision de 98.25%
Les V ont une précision de 91.98%
Les A ont une précision de 91.8%
Les F ont une précision de 100.0%
Les R ont une précision de 100.0%
Les P ont une précision de 97.78%
~~~

Le résultat de la comparaison des patterns est très précis, on voit que pour la catégorie des noms et des verbes, la précision est plus basse. Pour les noms cela est très certainement dû au fait que mon programme se contente d'une analyse syntaxique "superficielle" et ne regarde pas 2 mots en arrière par exemple, et ne regarde pas un mot en avant. Cette spécificité pourrait être corrigée et donner de meilleurs résultats pour cette catégorie. Pour la catégorie des verbes la précision pourrait elle aussi être améliorée, le programme d'étiqutage a été élaboré spécialement pour ce corpus et tend à étiqueter un verbe au présent de l'indicatif facilement. Avec un texte qui comporterait plus de variation de temps, la précision baisserait drastiquement.

J'ai aussi remarqué que mon programme fonctionne sur une base empirique, lorsque j'ai ajouté manuellement les mots réccurents, j'ai naturellement observé une amélioration de la précision pour les noms, mais également pour les adjectifs et déterminants. En implémentant la fonction d'analyse d'un mot devant, la précision pourrait encore augmenter.