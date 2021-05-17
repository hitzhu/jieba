
stopwords=[]
outfilename="stopwords/stopwords.txt"
stopwords_list=["baidu_stopwords.txt","cn_stopwords.txt","hit_stopwords.txt","scu_stopwords.txt","stopwords_other1.txt","stopwords_other2.txt"]
for i in range(len(stopwords_list)):
    for line in open('stopwords/'+stopwords_list[i], encoding='UTF-8').readlines():
        line=line.strip()
        if(line not in stopwords):
            stopwords.append(line)
        #else:print(line)

outputs = open(outfilename, 'w', encoding='UTF-8')
for word in stopwords:
    outputs.write(word+'\n')

