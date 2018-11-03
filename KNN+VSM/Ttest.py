import math
import os

from nltk.corpus import stopwords
from textblob import TextBlob
import numpy as np
def StopWords():
    WordList = []
    stopWords = []
    with open("stopwords.txt", 'r', encoding="utf-8", errors='ignore') as f:
        for line in f.readlines():
            stopWords.append(line.strip())
    f.close()
    with open("derepeat_t", 'r', encoding="utf-8", errors='ignore') as f:
        for line in f.readlines():
            word = line.strip().split(" ")[1]
            count = (int)(line.strip().split(" ")[2])
            # Word = TextBlob(word)
            # word=Word.correct()
            if word not in stopWords and count < 10000 and count > 50:
                WordList.append((word, count))
    f.close()
    print(WordList)
    print(WordList[0][1])
    # sorted(WordList, key=)
    Words = sorted(WordList, key=lambda word: word[1], reverse=True)  # sort by age
    print(Words)
    count = 1

    with open("StopWords", 'a', encoding="utf-8", errors='ignore')as f:
        for word in Words:
            f.write(str(count) + " " + word[0] + " " + str(word[1]) + "\n")
            count += 1
    f.close()
def tf_idf():
    #tf = C(t)该单词在该文本中的次数
    #idf=
    count=0 #用于计算 文档中出现该词的个数
    DataDir="word_file/"
    Vector = "vector/"
    Wordlist=[]

    W = {}
    with open("StopWords",'r',encoding="utf-8",errors='ignore')as f:
        line = f.readlines()
        for txt in line:
            Wordlist.append(txt.strip().split(" ")[1])
            W[txt.strip().split(" ")[1]]=0
    co=0
    for dir in os.listdir(DataDir):
        new_Dir = DataDir + dir + "/"

        for doc in os.listdir(new_Dir):
            co+=1
            docdir = new_Dir + doc
            docWord=[]
            with open(docdir, 'r', encoding='utf-8', errors='ignore')as f:
                line = f.readlines()
                words = TextBlob(line[0].strip()).words
                docWord=words
            derepeat=[]
            for word in docWord:
                if word in Wordlist and word not in derepeat:
                    derepeat.append(word)
                    W[word]+=1
            print("%d doc have done"%co)
    k=0
    for dir in os.listdir(DataDir):
        new_Dir=DataDir+dir+"/"
        save_vec= Vector+dir+"/"
        for doc in os.listdir(new_Dir):
            docdir= new_Dir+doc
            savedir=save_vec+doc
            if not os.path.exists(save_vec):
                os.makedirs(save_vec)
            with open(docdir,'r',encoding="utf-8",errors='ignore')as f:
                line =f.readlines()
                words = TextBlob(line[0].strip())
                vector={}
                for vect in Wordlist:
                    vector[vect]=0
                print("vector Create")
                DocWords = []
                DocWords.extend(words.words)
                for word in DocWords:
                    # print(word in Wordlist)
                    derepeat=[]
                    if word in Wordlist and word not in derepeat:
                        derepeat.append(word)
                        idf=math.log(18828/(W[word]+1))
                        tf=count_num(word,DocWords)
                        idf_tf=tf*idf
                        vector[word]=idf_tf

                with open(savedir, 'a', encoding="utf-8", errors='ignore')as v:
                    for w in Wordlist:
                        v.write(' '+str(vector[w]))
                print("END_%d"%k)
                k+=1
def Del():
    DataDir = "word_file/"
    Vector = "deDoc/"
    Wordlist = []
    with open("StopWords", 'r', encoding="utf-8", errors='ignore')as f:
        line = f.readlines()
        for txt in line:
            Wordlist.append(txt.strip().split(" ")[1])
    for dir in os.listdir(DataDir):
        new_Dir=DataDir+dir+"/"
        save_vec= Vector+dir+"/"
        k=0
        for doc in os.listdir(new_Dir):
            with open(new_Dir+doc, 'r', encoding="utf-8", errors='ignore')as f:
                line =f.readlines()

                u= open(save_vec+doc,'a', encoding="utf-8", errors='ignore')



def get_index(word,wordlist):
    count =0
    for w in wordlist:
        if w==word:
            return count
        count+=1
    return -1
def get_idf(word):
    DataDir = "word_file/"
    count=0
    Nterm=0
    for dir in os.listdir(DataDir):
        new_Dir = DataDir + dir + "/"
        count+= len(os.listdir(new_Dir))
        for doc in os.listdir(new_Dir):
            docdir=new_Dir+doc
            with open(docdir,'r',encoding='utf-8',errors='ignore')as f:
                line=f.readlines()
                words = TextBlob(line[0].strip())
                if word in words:
                    Nterm+=1
    idf = math.log(18828 / Nterm+1)
    return idf
def count_num(w,list):
    count=0
    for word in list:
        if word == w:
            count+=1
    return count
def countword():
    Dir="StopWords"
    DataDir="word_file/"
    DocWords="DopWords"
    Words=[]
    W={}
    with open(Dir, 'r', encoding='utf-8', errors='ignore')as f:
        lines = f.readlines()
        for line in lines:
            Words.append(line.strip().split(" ")[1])
            W[line.strip().split(" ")[1]]=0
    for dir in os.listdir(DataDir):
        new_Dir = DataDir + dir + "/"
        for doc in os.listdir(new_Dir):
            docdir = new_Dir + doc
            docWord=[]
            with open(docdir, 'r', encoding='utf-8', errors='ignore')as f:
                line = f.readlines()
                words = TextBlob(line[0].strip()).words
                docWord.extend(words)
            derepeat=[]
            for word in docWord:
                if word in Words and word not in derepeat:
                    derepeat.append(word)
                    W[word]+=1
            print('one have')
    print(W)
def allData():
    DataDir = "word_file/"
    Vector = "vector/"
    for dir in os.listdir(DataDir):
        new_Dir = DataDir + dir + "/"
        save_vec = Vector + dir + "/"
        k = 0
        # for doc in os.listdir(new_Dir):
            # docdir = new_Dir + doc
            # savedir = save_vec + doc
            # if not os.path.exists(save_vec):
            #     os.makedirs(save_vec)
            # with open(docdir, 'r', encoding="utf-8", errors='ignore')as f:

if __name__ == '__main__':
    # StopWords()
    tf_idf()
    # countword()