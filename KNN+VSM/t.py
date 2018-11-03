import os
import random

import matplotlib.pyplot as plt
import nltk
import numpy as np

if __name__ == '__main__':
    # d = " word_file as /"
    # print(d.strip().split(' ')[0])
    data_list = list(range(1, 3766))
    size = random.sample(data_list, 50)
    print(size)
    # distance ={}
    # distance ['a']=5
    # distance ['b']=6
    # distance['e'] = 5
    # distance['d'] = 6
    # distance = sorted(distance.items(), key=lambda x: x[1], reverse=True)
    # print(distance[1][1])
    # x=[10,30,50,100,500]
    # y=[5,4,3,2,6]
    # plt.axis([10, 500, 0, 10])
    # plt.plot(x, y, color="Blue")
    # plt.rcParams['font.sans-serif'] = ['SimHei']
    # plt.title("KNN准确率与Kzhi")
    # plt.xlabel("K-Value")
    # plt.ylabel("Accuracy-Value")
    #
    # plt.savefig("kAcc.png")
    # plt.show()