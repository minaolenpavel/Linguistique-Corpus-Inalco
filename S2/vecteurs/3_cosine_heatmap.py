import io
from nltk import word_tokenize
from scipy.spatial import distance # importantion de la fonction cosinus de vecteurs

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
window_size = 500
corpus = ''
corpus_input = open( corpus_path, 'r', encoding='iso-8859-1' )
corpus = corpus_input.read()
corpus_input.close()
# Attention, on construit le lexique du corpus une seule fois
# (PAS à l'occasion du calcul du vecteur de chaque segment!)
corpus_lexicon = lexique_du_corpus( corpus_path )

print( 'corpus lexicons has size {0}'.format( len( corpus_lexicon) ))

all_segment_vectors = []
s = 0 ; lasts = 0 ; num_seg = 0
corpus_token_sequence = word_tokenize( corpus )
for s in range( 0, len( corpus_token_sequence ), window_size):
     example_segment_words = corpus_token_sequence[ s : min( len( corpus_token_sequence  ),
                                                             (s + window_size)) ]
     print( "l'exemple {0} à indexer est \n________________\n {1}".format( num_seg,
                                                                           example_segment_words ))
     print( '________________\n' )
     vec = segment_vector( example_segment_words, corpus_lexicon )
     all_segment_vectors.append( vec )
     last_s = s
     num_seg += 1
# traitement du dernier segment s'il est plus court que window_size
if last_s < len( corpus_token_sequence ):
  example_segment_words = corpus_token_sequence[ last_s : ]
  print( "l'exemple {0} à indexer est \n________________\n {1}".format( num_seg,
                                                                        example_segment_words ))
  print( '________________\n' )
  vec = segment_vector( example_segment_words, corpus_lexicon )
  all_segment_vectors.append( vec )
  num_seg += 1

cosine_matrix = [ [0.0 for j in range( 0, len( all_segment_vectors ))] for i in range( 0, len( all_segment_vectors)) ]
# calcul des cosinus de vecteurs 2 à 2
for i in range( 0, len( all_segment_vectors)):
     for j in range( 0, len( all_segment_vectors )):
          # "1 - distane.cosine(..." car on veut la valeur de similarité cosinus et pas la distance
          cosine_matrix[ i ][ j ] = 1 - distance.cosine( all_segment_vectors[ i ],
                                                     all_segment_vectors[ j ] )

# affichage sous forme de carte thermique
import numpy as np
import matplotlib.pyplot as plt
np_cosmatx = np.array( cosine_matrix )

plt.imshow( np_cosmatx, cmap='hot', interpolation='nearest')
plt.show()



