from wordcloud import WordCloud
from imageio import imread
import matplotlib.pyplot as plt
import jieba

def stopwordslist():
    stopwords = [line.strip() for line in open('stopwords/baidu_stopwords.txt',encoding='UTF-8').readlines()]
    return stopwords

def read_deal_text():

    inputs = open("Init.txt", 'r', encoding='UTF-8')

    words = jieba.lcut(inputs)  # 使用精确分词模式

    stopwords = stopwordslist()
    outstr = ''
    # 去停用词
    for word in words:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "

    with open("out.txt", 'w') as file:
        file.write(outstr)
    print("文本处理完成")


def img_grearte():
    mask = imread("1.jpeg")
    with open("out.txt", "r") as file:
        txt = file.read()
    word = WordCloud(background_color="white", \
                     width=800, \
                     height=800,
                     font_path='C:\Windows\Fonts\simsunb.ttf',
                     mask=mask,
                     ).generate(txt)
    word.to_file('test.png')
    print("词云图片已保存")

    plt.imshow(word)  # 使用plt库显示图片
    plt.axis("off")
    plt.show()


read_deal_text()
img_grearte()