import re
from numpy import random
import json

file_con = 'test_con.txt'
file_label = 'test_label.txt'
f_con = open(file_con,'r',encoding='utf-8')
f_lable = open(file_label,'r',encoding='utf-8')

def get_CP(label, sentence):
    content = sentence
    dict = {}
    if label == "noncause":
        cp = ''
    else :
        for n in ['e1','e2']:
            pattern = "<{}>(.*)</{}>".format(n, n)
            #print(pattern)
            result = re.findall(pattern, sentence)
            for x in result:
                dict[n] = x
        #print(dict)
        pattern_ca = "cause-effect\((.*)\)"
        entity =[]
        result = re.findall(pattern_ca, label)
        for x in result:
            x = str(x)
            y = x.replace('(', '').replace(')', '')
            entity = y.split(',')
            #print(entity)
        i = 0
        while i < len(entity):
            #print(i)
            n = random.randint(1,6)
            ent1 = entity[i]
            #print(ent1)
            e1 = dict[ent1]
            #print(e1)
            ent2 = entity[i + 1]
            #print(ent2)
            e2 = dict[ent2]
            #print(e2)
            i += 2
            cp = Pattern(n,e1,e2)
            content = content + cp
    return content

def Pattern(n,e1,e2):
    if n == 1:
        sentence = e1 + " make " + e2 + " take place. "
    elif n == 2:
        sentence = e1 + " cause " + e2 + ". "
    elif n == 3:
        sentence = e1 + " lead to " + e2 + ". "
    elif n == 4:
        sentence = e1 + " is the reason of " + e2 + ". "
    elif n == 5:
        sentence = e1 + " result in " + e2 + ". "
    elif n == 6:
        sentence = e1 + " induce " + e2 + ". "
    return sentence

labels = f_lable.readlines()

id = 0

fw_train = open('train_aug.json', 'w', encoding='utf-8')
fw_test = open('test_aug.json', 'w', encoding='utf-8')

line = f_con.readline()
while line != None:
    content = line
    label = labels[id]
    if label == 'noncause\n':
        label = 'noncause'
    elif label == 'cause-effect((e1,e2))\n':
        label == 'cause-effect((e1,e2))'
    else:
        label == 'cause-effect((e2,e1))'
    sentence = get_CP(label,content)
    sentences = sentence.split()
    meta = dict(id=id,relation=label,sentence=sentences)
    json.dump(meta, fw_test, ensure_ascii=False)
    fw_test.write('\n')
    id += 1
    line = f_con.readline()
    if line == '\n':
        line = f_con.readline()
    else:
        continue
fw_train.close()
fw_test.close()
file_label.close()
file_con.close()
