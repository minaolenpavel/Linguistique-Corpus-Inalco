import io
from nltk import word_tokenize

def lexique_du_corpus( corpus_path = '' ):
  with open( corpus_path, 'r')  as corpus:
    txt = corpus.read()
    corpus_word_sequence = word_tokenize( txt )
    corpus_lexicon = []
    for w in corpus_word_sequence:
      if w not in corpus_lexicon:
        corpus_lexicon.append( w )
    corpus_lexicon.sort() # on trie le lexique par ordre alpahbétique
    return corpus_lexicon

def segment_vector( text_segment_word_lst, corpus_lexicon ):
     vector = [ 0  for i in range( 0,  len( corpus_lexicon )) ]
     for i in range( 0, len( text_segment_word_lst ) ):
          assert( text_segment_word_lst[ i ] in corpus_lexicon )
          vector[ corpus_lexicon.index( text_segment_word_lst[ i ] ) ] = 1
     return vector

corpus_path = 'vecteurs/jv80.txt'
corpus = ''
corpus_input = open( corpus_path, 'r', encoding='iso-8859-1' )
corpus = corpus_input.read()
corpus_input.close()
# un extrait du corpus à indexer choisi "à la main"
example_segment = corpus[ 461 : 800]
example_segment_words = word_tokenize( example_segment )
corpus_lexicon = lexique_du_corpus( corpus_path )

print( "l'exemple à indexer est \n________________\n {0}".format( example_segment ))
print( '________________\n' )

print( "son vecteur booléen d'indexes lexicaux est :" )
vec = segment_vector( example_segment_words, corpus_lexicon )
for k in range( 0, len( vec ) ):
     print( '{0}\t{1}\t{2}'.format( k, corpus_lexicon[ k ], vec[ k ] ))
print( '_____fin du vecteur' )
