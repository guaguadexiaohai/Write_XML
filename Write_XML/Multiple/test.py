import csv
import os
import re
import json
from nltk.tokenize import word_tokenize
from numpy import random
path = '../yichakan'

file_num = os.listdir(path)
id = 1

def search_entity(sentence):
    e1 = re.findall(r'<e1>(.*)</e1>', sentence)[0]
    e2 = re.findall(r'<e2>(.*)</e2>', sentence)[0]
    sentence = sentence.replace('<e1>' + e1 + '</e1>', ' <e1> ' + e1 + ' </e1> ', 1)
    sentence = sentence.replace('<e2>' + e2 + '</e2>', ' <e2> ' + e2 + ' </e2> ', 1)
    sentence = word_tokenize(sentence)
    sentence = ' '.join(sentence)
    sentence = sentence.replace('< e1 >', '<e1>')
    sentence = sentence.replace('< e2 >', '<e2>')
    sentence = sentence.replace('< /e1 >', '</e1>')
    sentence = sentence.replace('< /e2 >', '</e2>')
    #sentence = sentence.split()

    return sentence

def search_entity2(label,sentence):
    e1 = re.findall(r'<e1>(.*)</e1>', sentence)[0]
    e2 = re.findall(r'<e2>(.*)</e2>', sentence)[0]
    sentence = sentence.replace('<e1>' + e1 + '</e1>', ' <e1> ' + e1 + ' </e1> ', 1)
    sentence = sentence.replace('<e2>' + e2 + '</e2>', ' <e2> ' + e2 + ' </e2> ', 1)
    # sentence = word_tokenize(sentence)
    # sentence = ' '.join(sentence)
    sentence = sentence.replace('< e1 >', '<e1>')
    sentence = sentence.replace('< e2 >', '<e2>')
    sentence = sentence.replace('< /e1 >', '</e1>')
    sentence = sentence.replace('< /e2 >', '</e2>')

    n = random.randint(1,6)
    e1 = e1.strip()
    e2 = e2.strip()
    #sentence = sentence.split()

    # assert '<e1>' in sentence
    # assert '<e2>' in sentence
    # assert '</e1>' in sentence
    # assert '</e2>' in sentence

    return e1, e2

# single_train = open('train.csv', 'w', encoding ='utf-8', newline='')
# single_test = open('test.csv', 'w', encoding ='utf-8', newline='')
# test_writer = csv.writer(single_test)
# test_writer.writerow(['No','Label','Sentence'])
# train_writer = csv.writer(single_train)
# train_writer.writerow(['No','Label','Sentence'])
test_id = 0
train_id = 0
cnt = 0
label_list = []
for num in file_num:
    cnt = 0
    file_path = path + '\\' + num
    with open(file_path,'r',encoding='gbk') as f:
        reader = csv.reader(f)
        for line in reader:
            cnt += 1
            #print(cnt)
            label = line[1].lower()
            if label not in ['noncause','cause-effect((e1,e2))', 'cause-effect((e2,e1))']:
                if id % 5 == 0:
                    test_id += 1
                else:
                    train_id += 1
                if label not in label_list:
                    label_list.append(label)
            id += 1
    f.close()
    print('test_id=',test_id)
    print('train_id=',train_id)
    print(id)
label_file = open('labels.txt','w',encoding='utf-8')
label_list.sort()
for label in label_list:
    label_file.write(label + '\n')
label_file.close()
