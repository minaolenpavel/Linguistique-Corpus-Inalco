import re

BI_CONS = ["ch", "gn", "gu", "ph", "qu"]

BI_VOWS = ["ai", "am", "an", "au", "ay", "ei", "eu","in", "im", "oi", "on", "om", "ou", "oy", "ui", "un", "um", "uy"]

TRI_VOWS = ["aim", "ain","eau", "eaux","ein", "eim", "eil", "oin","ion"]

QUA_VOWS = ["euil","ouil"]



def vowel_or_cons(char:str) -> str:
    re_vowels = r'[aAeEiIoOuUyY]'
    re_cons = r'[B-DF-HJ-NP-TV-Zb-df-hj-np-tv-z]'
    re_end = r'#'

    if re.match(re_vowels, char):
        return "V"
    elif re.match(re_cons, char):
        return "C"
    elif re.match(re_end, char):
        return "#"


def couple_letters(word:str) -> list:
    