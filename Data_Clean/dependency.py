from stanfordcorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP(r'E:\python_p\stanford-corenlp-4.2.0')
file = open('dependency.txt','w+',encoding='utf-8')
txt = "i am having tears in my eyes i literally have no idea what i want to do, what my interests are , what my talents are i do not find anything interesting "

ls = nlp.dependency_parse(txt)

for l in ls:
    file.write(str(l))
    file.write('\n')

file.write('\n')

file.close()