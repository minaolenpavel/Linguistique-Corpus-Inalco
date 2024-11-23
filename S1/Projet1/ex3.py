import nltk
import ex2

def cleanApostrophes(tokens:list) -> list:
    return [token for token in tokens if token != "''" and token != "’"]

def nltkTokens() -> list:
    text = []
    with open("samples/sample2.txt", encoding="UTF-8", mode="r") as file:
        for line in file:
            text.append(nltk.word_tokenize(line))
        file.close()
    new_text = []
    for line in text:
        for word in line:
            if ex2.wordFormat(word):
                new_text.append(ex2.wordFormat(word))
    return cleanApostrophes(new_text)



if __name__ == "__main__":
    tokens = nltkTokens()
    print(tokens)