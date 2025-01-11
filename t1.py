from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
import jieba.posseg as pseg
from collections import Counter
import PIL.Image as Image
from matplotlib import colors
 
# 阅读文本（这里yourfile.txt，根据文本所在具体位置进行设置）
text = open("result.csv", encoding="utf-8").read()
words = pseg.cut(text)
 
# 按指定长度和词性提取词
report_words = []
for word, flag in words:
    if (len(word) >= 2) and ('n' in flag): #这里设置统计的字数
        report_words.append(word)
 
# 统计高频词汇
result = Counter(report_words).most_common(200) #词的个数
 
# 建立词汇字典
content = dict(result)
#输出词频统计结果
for i in range(len(result)):
    word,flag=result[i]
    print("{0:<10}{1:>5}".format(word,flag))
 
# 设置停用词
stopwords = set(STOPWORDS)
stopwords.update(["的", "感谢", "我代表", "以上", "报告", "表示诚挚感谢","战略"])
 
#设置png掩膜（yourfile.png根据实际路径进行替换）
# background = Image.open("yourfile.png").convert('RGB')
# mask = np.array(background)
'''
# 如果当前位深是32的话，可以不用写转RGBA模式的这一句，但是写上也没啥问题
# 从RGB（24位）模式转成RGBA（32位）模式
img = Image.open("yourfile.png").convert('RGBA')
W, L = img.size
white_pixel = (0, 0, 0, 0)  # 白色
for h in range(W):
    for i in range(L):
        if img.getpixel((h, i)) == white_pixel:
            img.putpixel((h, i), (255, 255, 255, 0))  # 设置透明
img.save("yourfile_new.png")  # 自己设置保存地址
'''
# 设置字体样式路径
font_path = r"C:\Windows\Fonts\STLITI.TTF"
 
# 设置字体大小
max_font_size =200
min_font_size =10
 
# 建立颜色数组，可更改颜色
color_list = ['#FF274B']
# 调用颜色数组
colormap = colors.ListedColormap(color_list)
 
# 生成词云
wordcloud = WordCloud(scale=4,                         #输出清晰度
                      font_path=font_path,             #输出路径
                      colormap=colormap,               #字体颜色
                      width=1600,                      #输出图片宽度
                      height=900,                      #输出图片高度
                      background_color='white',        #图片背景颜色
                      stopwords=stopwords,             #停用词
                    #   mask=mask,                       #掩膜
                      max_font_size=max_font_size,     #最大字体大小
                      min_font_size=min_font_size)     #最小字体大小
wordcloud.generate_from_frequencies(content)
 
# 使用 matplotlib 显示词云
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
# 保存词云图
wordcloud.to_file("wordcloud.png")