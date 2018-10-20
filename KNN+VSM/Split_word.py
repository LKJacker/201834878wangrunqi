from textblob import TextBlob, Word
import os

def word_deal(wordlist):
    words_dealed = []
    for word in wordlist:
        #变成单数
        word =word.singularize()
        #修正 拼写
        # word = word.correct()
        #词形还原
        word =Word(word).lemmatize()
        word =Word(word).lemmatize("v")
        word =word.lower()
        flag = False
        for cha in word:
            if not ((cha >= 'a' and cha <= 'z') or cha == '-'):
                flag = True
                break
        if flag:
            continue
        words_dealed.append(word)
    return words_dealed
        #
def get_data(Datapath):
    for dir in os.listdir(Datapath):
        for dir_name in os.listdir(Datapath+dir+"/"):
            doc_dir = Datapath+dir+"/"+dir_name
            word_list =[]
            with open(doc_dir, 'r', encoding='utf-8',errors ='ignore') as f:
                for line in f.readlines():
                    textblob = TextBlob(line.strip())
                    #分词
                    word_list.extend(textblob.words)
            # 处理得到的wordlist
            words = word_deal(word_list)
            filename = "word_file/"+dir
            if not os.path.exists(filename):
                os.makedirs(filename)
            with open(filename+"/"+dir_name ,'w',encoding='utf-8', errors='ignore') as f:
                for word in words:
                    f.write(word+" ")
            f.close()
            print(filename+" have done")



def main():
    Datapath  = "data/origin_data/"
    get_data(Datapath)

if __name__ == '__main__':
    main()