# 前端简介

## 大致结构

页面分为两大板块，分别为 首页 和 小组成员。

其中首页如下：

![image-20250107185749482](C:\Users\86138\AppData\Roaming\Typora\typora-user-images\image-20250107185749482.png)
![image-20250107185502491](C:\Users\86138\AppData\Roaming\Typora\typora-user-images\image-20250107185502491.png)
![image-20250107185515404](C:\Users\86138\AppData\Roaming\Typora\typora-user-images\image-20250107185515404.png)

分为三大板块 上传区域，热评 和 情绪分析。

## 上传区域

![image-20250107190006334](C:\Users\86138\AppData\Roaming\Typora\typora-user-images\image-20250107190006334.png)

这个组件向服务器端返回的参数是输入的 URL，以{URL: 返回的url} 形式存储在request.data中。

需要返回此URL下的blog和blog下的评论，可以选择返回嵌套的字典，分成topic和comments两个键值对，topic键值对里面又含content，likes，comment_num，repost_num和name多个键值对，对应blog内容，点赞数，评论数，转发数和博主昵称，comments键值对里面对应一个列表，每个列表都是由time，comment，place和name四个属性键值对，分别对应评论时间，评论内容，ip来源以及评论者昵称。

## 热评区域

此区域没用需要交互的内容。

## 情绪分析

![image-20250107191026816](C:\Users\86138\AppData\Roaming\Typora\typora-user-images\image-20250107191026816.png)

这个组件会向服务器端返回要分析情感的文本，以{text: 文本} 形式存储在request.data中。

当前返回逻辑已经足够，无须修改。

![image-20250107191212439](C:\Users\86138\AppData\Roaming\Typora\typora-user-images\image-20250107191212439.png)

这个组件会在初始化时向服务器发送请求，无返回给服务器的参数。

需要返回的参数是一个列表，是对上述传入文件或者新URL爬取的评论进行分析后的结果，每个元素是一个字典，包含province，positive，negative三个属性，对应省份名，积极得分，消极得分。

![image-20250107192146854](C:\Users\86138\AppData\Roaming\Typora\typora-user-images\image-20250107192146854.png)

这个组件同上，只需要返回所有评论分析后汇总的积极和消极得分，只需要返回含pScore和nScore两个属性的字典。可以和上述图表的数据一起返回，比如将上一图表的元素设置成一个键值对provinceData，然后加上wholePscore和wholeNscore两个键值对即可。

![image-20250107192223465](C:\Users\86138\AppData\Roaming\Typora\typora-user-images\image-20250107192223465.png)

这个组件同上，可以不用数据库进行处理，只需要调用AI模型对输入语句进行分析后返回含pScore和nScore两个属性的字典。

## 汇总

总的来说，涉及三种操作。

1. 输入URL，前端返回{URL:url}给后端，后端需要依据这个url去爬取信息后返回以下内容

   + 爬取的blog

   + 爬取blog的评论区

   + 对评论区进行情感分析后进行汇总，返回各省份的积极和消极得分

   + 返回总体的积极和消极得分

2. 输入要分析的文本，前端返回{text:文本}给后端，后端需要依据这个文本进行情感分析，返回积极和消极得分，这个可以不采用数据库进行存储。当然如果能够进行缓存，将结果记录在数据库中，当输入评论时可以先在数据库中查找此文本是否已经分析过，若分析过则直接返回，未分析过则送给模型进行训练。
