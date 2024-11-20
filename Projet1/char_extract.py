def extract_char():
        chars = {}
        with open("diacritique_accents.txt", encoding='UTF-8') as file:
            for line in file:
                char, latex = line.split(maxsplit=1)
                chars[char] = latex.strip()
            file.close()
        return chars
    


if __name__ == "__main__":
    print(extract_char())
