import io

from nltk import word_tokenize

with open( 'vecteurs/jv80.txt', 'r', encoding='iso-8859-1')  as corpus:
      txt = corpus.read()
      corpus_word_sequence = word_tokenize( txt )
      corpus_lexicon = []
      for w in corpus_word_sequence:
           if w not in corpus_lexicon:
                corpus_lexicon.append( w )
                
corpus_lexicon.sort() # on trie le lexique par ordre alpahbétique

print( 'la liste des lexies du corpus est :\nindex\tlexie\n')
last_index = None
for lexie in corpus_lexicon :
     last_index = corpus_lexicon.index( lexie )
     print( '{0}\t{1}'.format( last_index, lexie ))
print(len(corpus_lexicon))
print('--- fin du lexique du corpos' )

##print( 'la liste des lexies du corpus est :\nindex\tlexie\n')
##i = 0
##for lexie in corpus_lexicon:
##     print( '{0}\t{1}'.format( i, lexie ))
##     i += 1
##print('--- fin du lexique du corpos' )
##     

               
           
      
