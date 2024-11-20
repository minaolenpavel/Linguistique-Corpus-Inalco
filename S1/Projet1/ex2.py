SPACE = hex(int('0020', 16))
NO_BREAK_SPACE = hex(int('00A0', 16))
OGHAM_SPACE_MARK  = hex(int('1680', 16))
MONGOLIAN_VOWEL_SEPARATOR  = hex(int('180E', 16))
EN_QUAD  = hex(int('2000', 16))
EM_QUAD  = hex(int('2001', 16))
EN_SPACE  = hex(int('2002', 16))
EM_SPACE  = hex(int('2003', 16))
THREE_PER_EM_SPACE  = hex(int('2004', 16))
FOUR_PER_EM_SPACE  = hex(int('2005', 16))
SIX_PER_EM_SPACE  = hex(int('2006', 16))
FIGURE_SPACE  = hex(int('2007', 16))
PUNCTUATION_SPACE  = hex(int('2008', 16))
THIN_SPACE  = hex(int('2009', 16))
HAIR_SPACE  = hex(int('200A', 16))
ZERO_WIDTH_SPACE  = hex(int('200B', 16))
NARROW_NO_BREAK_SPACE  = hex(int('202F', 16))
MEDIUM_MATHEMATICAL_SPACE  = hex(int('205F', 16))
IDEOGRAPHIC_SPACE  = hex(int('3000', 16))
ZERO_WIDTH_NO_BREAK_SPACE  = hex(int('FEFF', 16))
#---line separators---
LINE_FEED = hex(int('000A', 16))
CARRIAGE_RETURN = hex(int('000D', 16))    
INFORMATION_SEPARATOR_FOUR = hex(int('001C', 16))
INFORMATION_SEPARATOR_THREE = hex(int('001D', 16))
INFORMATION_SEPARATOR_TWO = hex(int('001E', 16))
NEL_NEXT_LINE = hex(int('0085', 16))
LINE_SEPARATOR = hex(int('2028', 16))
PARAGRAPH_SEPARATOR = hex(int('2029', 16))

space_and_separator_list = [
    SPACE, NO_BREAK_SPACE, OGHAM_SPACE_MARK, MONGOLIAN_VOWEL_SEPARATOR,
    EN_QUAD, EM_QUAD, EN_SPACE, EM_SPACE, THREE_PER_EM_SPACE,
    FOUR_PER_EM_SPACE, SIX_PER_EM_SPACE, FIGURE_SPACE, PUNCTUATION_SPACE,
    THIN_SPACE, HAIR_SPACE, ZERO_WIDTH_SPACE, NARROW_NO_BREAK_SPACE,
    MEDIUM_MATHEMATICAL_SPACE, IDEOGRAPHIC_SPACE, ZERO_WIDTH_NO_BREAK_SPACE,
    LINE_FEED, CARRIAGE_RETURN, INFORMATION_SEPARATOR_FOUR,
    INFORMATION_SEPARATOR_THREE, INFORMATION_SEPARATOR_TWO, NEL_NEXT_LINE,
    LINE_SEPARATOR, PARAGRAPH_SEPARATOR
]

def charToHex(char:str) -> str:
    return hex(ord(char))

def isSpace(char:str) -> bool:
    for space in space_and_separator_list:
        if charToHex(char) == space:
            return True
        else:
            return False

text = []
with open("Projet1\samples\sample2.txt", encoding="UTF-8", mode="r") as file:
    for line in file:
        mot = []
        for char in line:
            if isSpace(char):
                text.append("".join(mot))
                mot = []
            else:
                mot.append(char)

for i in text:
    print(i)