from glob import glob
import re

dico_path = glob( 'dimaju*.txt' )[ 0 ]

print( dico_path )

dico_fdesc_r = open( dico_path, 'r' )

cnt = 0
verb_rex_prefix_1 = '^march'
suffix_lst_1 = 'er|e|es|ons|ez|ent|ais|ait|ions|iez|aient|ai|as|a|âmes|âtes|èrent|é|ée|és|ées|ant'
verb_rex_prefix_2 = '^marcher'
suffix_lst_2 = 'ai|as|a|ons|ont|ez|ent|ais|ait|ions|iez|aient'
verb_rex = '(((' + verb_rex_prefix_1 + ')(' + suffix_lst_1 + '))|((' + verb_rex_prefix_2 + ')(' + suffix_lst_2 + ')))'
pos_list_res = '((\t([^V\n]+)?)V(([^\n]+)\n))'
verb_automat = re.compile( verb_rex + pos_list_res )

output = []
for l in dico_fdesc_r:
     result = verb_automat.search( l )
     if result:
          #print( l )
          output.append(l)
     cnt += 1
dico_fdesc_r.close()

#print(output)
my_exps = []
for i in output:
     exp = re.sub("\t", r"\\t", i)
     exp = re.sub("\n", r"\\n", exp)
     my_exps.append(exp)

final_exp = r"(" + r"|".join(my_exps) + r")"
#print(final_exp)

output2 = []
with open("dimaju.txt", mode='r', encoding='utf-8') as dico_fr:
     for l in dico_fr:
          result = re.search(final_exp, l)
          if result:
               output2.append(l)

pos_list = []
form_list = []
for i in output2:
     line_as_list = i.split('\t')
     #breakpoint()
     form_list.append(line_as_list[0])
     line_as_list.pop(0)
     pos_list.append(list(map(str.strip, line_as_list)))

print(pos_list)
print(form_list)

