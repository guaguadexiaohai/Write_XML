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
multi_train = open('train.csv','w',encoding = 'utf-8',newline='')
multi_test = open('test.csv','w',encoding = 'utf-8',newline='')
multi_test_writer = csv.writer(multi_test)
multi_test_writer.writerow(['No','Label','Sentence'])
multi_train_writer = csv.writer(multi_train)
multi_train_writer.writerow(['No','Label','Sentence'])

# single_train = open('train.csv', 'w', encoding ='utf-8', newline='')
# single_test = open('test.csv', 'w', encoding ='utf-8', newline='')
# test_writer = csv.writer(single_test)
# test_writer.writerow(['No','Label','Sentence'])
# train_writer = csv.writer(single_train)
# train_writer.writerow(['No','Label','Sentence'])
test_id = 6580
train_id = 1
cnt = 0
for num in file_num:
    cnt = 0
    file_path = path + '\\' + num
    with open(file_path,'r',encoding='gbk') as f:
        reader = csv.reader(f)
        for line in reader:
            cnt += 1
            print(cnt)
            print(num)
            content = line[0]
            x = re.sub(r"\\n", "", content)
            x = x.replace('\\n','')
            x = x.replace('\n', '')
            x = x.replace('\r', '')
            x = x.replace('.', '. ')
            x = x.replace('#', '')
            x = x.replace('\t', '')
            x = x.replace('\\t', '')
            x = x.replace('$', '')
            y = re.sub(r"\"\"", "", x)
            z = re.sub\
                (r"\"", "", y)
            content = re.sub(r"\\", "", z)
            results = re.compile(r'[http|https]*://[a-zA-Z0-9.?/&=:]*', re.S)
            content = re.sub(results, '', content)
            #content = search_entity(content)
            label = line[1].lower()
            words = content.split()
            if label not in ['noncause','cause-effect((e1,e2))', 'cause-effect((e2,e1))']:
                if len(words) <= 250:
                    if id % 5 == 0:
                        multi_test_writer.writerow([test_id, str(label), content])
                        test_id += 1
                    else:
                        multi_train_writer.writerow([train_id, str(label), content])
                        train_id += 1
            # else:
            #     if id % 5 == 0:
            #         test_writer.writerow([test_id,label,content])
            #         test_id += 1
            #     else:
            #         train_writer.writerow([train_id, label, content])
            #         train_id += 1
            id += 1
    f.close()
    print(id)
multi_test.close()
multi_train.close()