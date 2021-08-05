import jieba
from wordcloud import WordCloud
from imageio import imread
import matplotlib.pyplot as plt
import re

word_dir = {}
other=["收到","明天","昨天",'谢谢',"多久","你妹","不用","干嘛","早上","刚刚","一份","一点","几张","东西","地方","我记",
       "好不好"
       ]

# 创建停用词列表
def stopwordslist():
    stopwords = [line.strip() for line in open('stopwords/stopwords.txt', encoding='UTF-8').readlines()]
    return stopwords

def remove_emoji(sentence):
    start=sentence.find("[")
    while start!=-1:
        end=sentence.find("]")
        sentence=sentence[0:start]+sentence[end+1:]
        start = sentence.find("[")
    return sentence

# 对句子进行中文分词
def seg_depart(sentence):
    # 对文档中的每一行进行中文分词
    print("正在分词")
    sentence=remove_emoji(sentence)
    k=re.findall(r'[\u4e00-\u9fa5]+',sentence)
    #print(k)
    if len(k)>0:
        sentence_depart = jieba.lcut(k[0],cut_all=False)

    # 创建一个停用词列表
        stopwords = stopwordslist()
        # 输出结果为outstr
        outstr = ''
        # 去停用词
        for word in sentence_depart:
            if word not in stopwords and word not in other:
                if word != '\t' and len(word)>1:
                    outstr += word
                    outstr += " "
                    if word in word_dir.keys():
                        word_dir[word] += 1
                    else:
                        word_dir[word] = 1
        return outstr
    return ""


def img_grearte():
    mask = imread("1.bmp")
    with open("out.txt", "r", encoding="utf-8") as file:
        txt = file.read()
    word = WordCloud(background_color="white",
                     width=1000,
                     height=1000,
                     font_path='C:\Windows\Fonts\simkai.ttf',
                      mask=mask,
                     ).generate_from_frequencies(word_dir)
    word.to_file('微信聊天.png')
    print("词云图片已保存")

    plt.imshow(word)  # 使用plt库显示图片
    plt.axis("off")
    plt.show()


# 给出文档路径
filename = "微信聊天.txt"
outfilename = "out.txt"
inputs = open(filename, 'r', encoding='UTF-8')
outputs = open(outfilename, 'w', encoding='UTF-8')

# 将输出结果写入out.txt中
for line in inputs:
    if not re.search("wxid_", line) and not re.search("voip_content_voice", line) \
            and not re.search("推送信息", line) and not re.search("~",line) and not re.search("…",line)\
            and not re.search("撤回了一条消息",line):
        line_seg = seg_depart(line)
        outputs.write(line_seg + '\n')
        print("-------------------正在分词和去停用词-----------")
outputs.close()
inputs.close()
print("删除停用词和分词成功！！！")
sorted(word_dir.items(), key=lambda item: item[1])

img_grearte()
