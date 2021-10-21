import spacy
from spacy import displacy
from collections import Counter
import csv
import en_core_web_sm
from pprint import pprint
nlp = en_core_web_sm.load()

file = open('../Data/data.csv','r',encoding='utf-8')
reader = csv.reader(file)
f = open('../Data/Entity.txt','w',encoding='utf-8')

t = 0
for row in reader:
    text = row[1]
    doc = nlp(text)
    f.write(str(t) +'\n')
    for X in doc:
        f.write(str(X)+ ',    ' +str(X.ent_iob_) +',    ' + str(X.ent_type_))
        f.write('\n')
    f.write('\n')
    t += 1

f.close()