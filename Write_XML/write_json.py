import re
import csv
from numpy import random

test_path = './test_single.csv'
#train_path = './train_single.csv'
#json_file_train = './train.json'



def get_CP(label, sentence):
    content = sentence
    dict = {}
    if label == "noncause":
        cp = ''
    else:
        for n in ['e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10', 'e11', 'e12']:
            pattern = "<{}>(.*)</{}>".format(n, n)
            # print(pattern)
            result = re.findall(pattern, sentence)
            for x in result:
                dict[n] = x
        # print(dict)
        pattern_ca = "Cause-Effect\((.*)\)"
        entity = []
        result = re.findall(pattern_ca, label)
        for x in result:
            x = str(x)
            y = x.replace('(', '').replace(')', '')
            entity = y.split(',')
            # print(entity)
        i = 0
        while i < len(entity):
            # print(i)
            n = random.randint(1, 6)
            ent1 = entity[i]
            # print(ent1)
            e1 = dict[ent1]
            # print(e1)
            ent2 = entity[i + 1]
            # print(ent2)
            e2 = dict[ent2]
            # print(e2)
            i += 2
            cp = Pattern(n, e1, e2)
            content = content + cp
    return content


def Pattern(n, e1, e2):
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


def get_CauAug(trainsent, trainlabel, testsent, testlabel):
    trainLabel = []
    trainSent = []
    testLabel = []
    testSent = []
    CauAug = []
    length = len(trainlabel)
    f = open('./corpus/causality_aug.txt', 'w+', encoding='utf-8')
    for i in range(length):
        label = trainlabel[i]
        sentence = trainsent[i]
        sent = get_CP(label, sentence)
        CauAug.append(sent)
        f.write(sent)
        f.write('\n')
        # print(label, sentence)
        trainLabel.append(label)
        trainSent.append(sentence)

    length = len(testlabel)
    for i in range(length):
        label = testlabel[i]
        sentence = testsent[i]
        # print(label, sentence)
        testLabel.append(label)
        testSent.append(sentence)

    return trainSent, trainLabel, testSent, testLabel, CauAug

def write_test_json():
    file_path = './test_single.csv'
    f = open(file_path,'r',encoding='utf-8-sig')
    reader = csv.reader(f)
    json_file_test = './test.txt'
    writer = open(json_file_test,'w+',encoding='utf-8')
    id = 1
    for line in reader:
        content = line[0]
        label = line[1]
        words = content.split()
        pattern = '{"id": "' + str(id) + '", "relation": "' + label + '", "sentence": ' + str(words) + '}'
        writer.write(pattern)
        id += 1
    print("id:", id)
    f.close()
    writer.close()

write_test_json()