from textblob import TextBlob, Word
import os

def word_deal(wordlist):
    words_dealed = []
    for word in wordlist:
        #变成单数
        word =word.singularize()
        #修正 拼写
        word = word.correct()
        #词形还原
        word =Word(word).lemmatize()
        word =Word(word).lemmatize("v")

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
            word_deal(word_list)


def main():
    Datapath  = "data/origin_data/"
    get_data(Datapath)

if __name__ == '__main__':
    main()