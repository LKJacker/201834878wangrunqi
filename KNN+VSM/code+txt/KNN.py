import os
import random
import matplotlib.pyplot as plt

def divide():

    DataDir="vector/"
    SaveFile="alldata.txt"
    for dir in os.listdir(DataDir):
        firstDir= DataDir+dir+"/"
        for doc in os.listdir(firstDir):
            with open(SaveFile,'a',encoding="utf-8",errors='ignore')as f:
                f.write(firstDir+doc+"\n")
def createTrainandTest():
    train = "train.txt"
    test = "test.txt"
    SaveFile = "alldata.txt"
    data_list = list(range(1, 18828))
    #测试集大小为 原文档数的20%
    testsize = random.sample(data_list, 3766)
    count=0
    with open(SaveFile, 'r', encoding="utf-8", errors='ignore')as f:
        ft= open(train, 'a',encoding='utf-8',errors='ignore')
        fte= open(test, 'a',encoding='utf-8',errors='ignore')
        for line in f.readlines():
            text=line.strip()
            if count in testsize:
                fte.write(text+"\n")
            else:
                ft.write(text+"\n")
            count+=1
def cal_cosine(v1,v2):
    #计算余弦相似度
    sumab = 0
    suma2 = 0
    sumb2 = 0
    for i in range(5506):
        sumab += v1[i] * v2[i]
        suma2 += v1[i] * v1[i]
        sumb2 += v2[i] * v2[i]
    if sumb2 * suma2 > 0:
        return sumab / ((pow(sumb2, 0.5) * pow(suma2, 0.5)))
    else:
        # 其中一个 向量为0 bad
        return 0
def KNN(k):
    sum=50
    data_list = list(range(1, 3766))
    size = random.sample(data_list, 50)
    correct=0
    train=[]
    test=[]
    with open("train.txt", 'r', encoding="utf-8", errors='ignore') as f:
        for line in f.readlines():
            train.append(line.strip())
    f.close()
    with open("test.txt", 'r', encoding="utf-8", errors='ignore') as f:
        c=0
        # for line in f.readlines():
        line = f.readlines()
        for i in range(sum):
            test.append(line[size[i]].strip())
    f.close()
    for t in test:
        print("进入测试")
        tlabel= getLabel(t)
        knn={}
        vtest = getVector(t)
        for tr in train:
            vtrain = getVector(tr)
            # print(len(vtrain),len(vtest))
            dic = cal_cosine(vtest,vtrain)
            knn[tr]=dic
        sort = sorted(knn.items(), key=lambda x: x[1], reverse=True)
        maxlabel={}
        for i in range(k):
            maxlabel[getLabel(sort[i][0])]=0
        for i in range(k):
            maxlabel[getLabel(sort[i][0])]+=1
        sort = sorted(maxlabel.items(), key=lambda x: x[1], reverse=True)
        klabel=sort[0][0]
        if tlabel==klabel:
            correct+=1
        print(correct)
        print("one have done")
    print("ACC",correct/sum)
    return correct/sum

def getVector(url):
    vector=[]
    with open(url,'r',encoding='utf-8',errors='ifnore') as f:
        line = f.readlines()
        for i in line[0].strip().split(' '):
            vector.append(float(i))
    return vector
def getLabel(url):
    return url.split('/')[1]
if __name__ == '__main__':
    # divide()
    # print(getLabel("vector/alt.atheism/51120"))
    # createTrainandTest()
    draw=[]
    x=[]
    y=[]
    k_all = [10, 30, 50, 100, 300, 500]
    for k in k_all:
        acc = KNN(k)
        draw.append((k, acc))
    print(draw)
    for i in range(0, 8):
        x.append(draw[i][0])
        y.append(draw[i][1])
    plt.axis([10, 500, 0, 1])
    plt.plot(x, y, color="Blue")
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title("KNN准确率与Kzhi")
    plt.xlabel("K-Value")
    plt.ylabel("Accuracy-Value")
    plt.savefig("kAcc.png")
    plt.show()

    # KNN(50)
    # with open('alldata.txt','r',encoding='utf-8',errors='ifnore')as f:
    #     for line in f.readlines():
    #         lenth=len(getVector(line.strip()))
    #         if lenth>5506 :
    #             print(lenth)