import nltk
import os 
jar = r"C:\Users\M3500\AppData\Roaming\nltk_data\taggers\stanford-postagger-full-2020-11-17\stanford-postagger.jar"
model = r"C:\Users\M3500\AppData\Roaming\nltk_data\taggers\stanford-postagger-full-2020-11-17\models\french-ud.tagger"


text = "il arrive en retard"
tokens = nltk.tokenize.word_tokenize(text)
print(tokens)

pos_tagger = nltk.tag.StanfordPOSTagger(model, jar, encoding = 'utf-8')
tagged_text = pos_tagger.tag(tokens)
print(tagged_text)