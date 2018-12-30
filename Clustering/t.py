
if __name__ == '__main__':

    f =  open("data/Tweets.txt",'r',encoding='utf-8',errors="ignore")
    r = f.readlines()
    t = []
    for line in r:
        if line.strip().split(" ")[-1] not in t:
            t.append(line.strip().split(" ")[-1])
    print(len(t))
