


with open('test/sentences.txt','r',encoding='utf-8') as f:
    for i, line in enumerate(f):
        print(i)
        e1, e2, sent = line.strip().split('\t')