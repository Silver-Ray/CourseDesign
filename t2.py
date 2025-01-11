import pandas as pd
from sqlalchemy import create_engine
from BERT_analysis.bert_tuili import CommentClassifier
classifier = CommentClassifier()
data = pd.read_csv('comment.csv')
post = pd.DataFrame(data.iloc[0,:]).transpose()
post_json = {"name":post["blogger_name"],"content":post["content"][0], "likes":post["likes"][0], "comment_num":post["comment_num"][0], "repost_num":post["repost_num"][0]}
comment = data.iloc[1:,0:4].reset_index(drop=True)
result = classifier.predict_dataframe(comment)
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/weibo?charset=utf8mb4')
pd.io.sql.to_sql(result,'comments',con=engine,schema='weibo',if_exists='replace',index=False)
