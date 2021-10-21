import csv
import os
import re
import json
from nltk.tokenize import word_tokenize
from numpy import random
path = 'E:\Code\Python\Project\Causality_Extraction\Write_XML\yichakan'

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

label_train = open('./label_sentence/train/labels.txt', 'w', encoding='utf-8')
sentence_train = open('./label_sentence/train/sentences.txt', 'w', encoding='utf-8')
label_test = open('./label_sentence/test/labels.txt', 'w', encoding='utf-8')
sentence_test = open('./label_sentence/test/sentences.txt', 'w', encoding='utf-8')
test_id = 21620
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
            x = x.replace('#', '# ')
            x = x.replace('\t', '')
            x = x.replace('\\t', '')
            x = x.replace('$', '$ ')
            y = re.sub(r"\"\"", "", x)
            z = re.sub\
                (r"\"", "", y)
            content = re.sub(r"\\", "", z)
            results = re.compile(r'[http|https]*://[a-zA-Z0-9.?/&=:]*', re.S)
            content = re.sub(results, '', content)
            #content = search_entity(content)
            label = line[1].lower()
            content = content.replace('<e1>', ' <e1> ')
            content = content.replace('<e2>', ' <e2> ')
            content = content.replace('</e1>', ' </e1> ')
            content = content.replace('</e2>', ' </e2> ')
            #pattern = '\t<item id="' + str(id) + '" label="' + label + '">\n\t\t<sentence>' + content + '</sentence>\n\t</item>\n'
            words = content.split()
            if len(words) <= 250:
                if label in ['noncause','cause-effect((e1,e2))', 'cause-effect((e2,e1))']:
                    if id % 5 == 0:
                        if label == 'noncause':
                            e1 = words[0].strip()
                            e2 = words[len(words)-1].strip()
                        else:
                            e1, e2 = search_entity2(label,content)
                        label_test.write(label + '\n')
                        sentence_test.write(e1.strip() + '\t' + e2.strip() + '\t' + content + '\n')
                        #sent = cp + content
                        test_id += 1
                    else:
                        if label == 'noncause':
                            e1 = words[0].strip()
                            e2 = words[len(words) - 1].strip()
                        else:
                            e1, e2 = search_entity2(label,content)
                        label_train.write(label + '\n')
                        sentence_train.write(e1.strip() + '\t' + e2.strip() + '\t' + content + '\n')
                        train_id += 1
                        #sent = cp + content
                #e1,e2,e3 = sent.strip().split('\t')
                id += 1
    f.close()
    print(id)
label_test.close()
label_train.close()
sentence_test.close()
sentence_train.close()
print(id)