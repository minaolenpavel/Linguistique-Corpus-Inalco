import re

def extract_or_not(line:str) -> bool:
    """
    Détermine si la ligne doit-être considéré dans la version finale du fichier donné au syllabeur.
    """
    pattern_text_bal = re.compile(r'(<Sync .*\/>)|(^[a-zA-Z].*)')
    if pattern_text_bal.match(line):
        return True
    else:
        return False


def extract_text(xml_path:str) -> str:
    """
    Trie les balises inutiles du texte et de la balise <Sync/>
    """
    text = []
    with open(xml_path, encoding='utf-8', mode='r') as xml_file:
        for i in xml_file:
            i = i.strip()
            if extract_or_not(i):
                text.append(i)
    return text

if __name__ == "__main__":
    print(extract_text("Projet_S2/transcript.xml"))