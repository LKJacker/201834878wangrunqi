import os
import numpy as np

def getLabel(url):
    return url.split('/')[1]
def CreateTrainClass():
    data="newTrain/"
    if not os.path.exists(data):
        os.makedirs(data)
    f= open('train.txt','r')
    lines= f.readlines()
    f.close()
    for line in lines:
        label = getLabel(line.strip())
        save_file= data+label+"/"
        if not os.path.exists(save_file):
            os.makedirs(save_file)
        f= open(save_file+'train.txt','a')
        f.write(line.strip()+'\n')

def countCnum():
    dir="newTrain/"
    save_file = "num_class.txt"
    writer = open(save_file,'w', encoding='utf-8',errors='ignore')
    for clas in os.listdir(dir):
        count=0
        file = dir+clas+"/"+"train.txt"
        f= open(file,'r',encoding='utf-8',errors='ignore')
        lines = f.readlines()
        for line in lines:
            count+=1
        writer.write(clas+" "+(str)(count)+"\n")
def createZIDIAN():
    #创建保存每个类的字典，key 为类名 value 是类中word的每个数目 先创建词典。
    worddir ="StopWords"
    wordnum=[]
    word =[]
    f = open(worddir,'r',encoding='utf-8',errors='ignore')
    lines = f.readlines()
    for line in lines:
        # word.append([,])
        list=[]

        list.append(line.strip().split(" ")[1])
        list.append(line.strip().split(" ")[2])
        wordnum.append(list)
        word.append(line.strip().split(" ")[1])
    # word 为 二元数组，其中0 为 单词名 1 为频数
    # print(len(word))
    # print(word)
    print(word)
    f.close()
    dir = "word_file/"
    CNum={}
    for clas in os.listdir(dir):
        Wordlist = {}
        for i in word:
            Wordlist[i] = 0
        doc = dir+clas+"/"
        for d in os.listdir(doc):
            f= open(doc+d,'r',encoding='utf-8',errors='ignore')
            Word_in_class = f.readlines()[0].strip().split(" ")
            for w in Word_in_class:
                if w in word:
                    Wordlist[w]+=1
        CNum[clas] = Wordlist
        print("one class")
    print(CNum)
    return CNum
def NB():
    clasnum = createZIDIAN()
    clasSum = {}
    sumwordss=0
    for key in clasnum.keys():
        c=0
        for v in clasnum[key].values():
            c+=int(v)
        clasSum[key]=c
        sumwordss+=c
    print(clasSum)
    worddir = "StopWords"
    wordnum = {}
    word = []
    f = open(worddir, 'r', encoding='utf-8', errors='ignore')
    lines = f.readlines()
    for line in lines:
        wordnum[line.strip().split(" ")[1]]=line.strip().split(" ")[2]
        word.append(line.strip().split(" ")[1])
    f.close()
    te = open('test', 'r', encoding='utf-8', errors='ignore')
    tlines= te.readlines()
    Acc=0.0
    sum= 3766
    current=0

    for doc in tlines:
        pinc = {}
        for clas in os.listdir("word_file/"):
            pinc[clas] = 0
        #pinc 中保存着 每个种类的概率
        label =getLabel(doc)
        f=open(doc.strip(), 'r', encoding='utf-8', errors='ignore')
        derepeat=[]
        words= (f.readlines()[0].split(" "))
        for w in words:
            if w in word:
                if w not in derepeat:
                    derepeat.append(w)
                    for c in pinc.keys():
                    #c 类 对word 求 概率
                        pwc= clasnum[c][w]/clasSum[c]
                        pc= clasSum[c]/sumwordss
                        pw= int(wordnum[w])/sumwordss
                        p = np.log(1+((pwc*pc)/pw))
                        pinc[c]+=p
        sort = sorted(pinc.items(), key=lambda x: x[1], reverse=True)
        nlabel =sort[0][0]
        if nlabel==label:
            current+=1
        print("one have done %d true"%current)
    Acc= current/3766.0
    print(current)
    print(Acc)
    print("acc:%f"%Acc)


def change():
    dir ="train.txt"
    save="train"
    f=open(dir,'r')
    t=open(save,'w')
    lines= f.readlines()
    for line in lines:
        c= line.strip().split("/")
        c[0]="word_file"
        t.write(c[0]+"/"+c[1]+"/"+c[2]+"\n")


def main():
    # CreateTrainClass()
    # countCnum()
    # change()
    NB()
    # print(2932/3766.0)
    # print(float(2932/3766.0) )
if __name__ == '__main__':
    #p(c|x)= p(x|c1)p(c1)/p(x|c1)p(c1)+p(x|c2)p(c2)
    main()