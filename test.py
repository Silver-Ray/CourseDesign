import pandas as pd
from sqlalchemy import create_engine
import re

# 创建数据库连接
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/weibo?charset=utf8mb4')

# 读取所有数据
query = """
SELECT source, predicted_label
FROM comments;
"""

# 读取数据
df = pd.read_sql_query(query, engine)

# 定义所有情感标签
all_labels = ['happiness😁', 'sadness😭', 'like😘', 'anger😡', 'disgust🤮', 'surprise😲', 'fear😱']

# 使用 pivot_table 生成所需的 DataFrame
result = pd.pivot_table(df, values='predicted_label', index='source', columns='predicted_label', aggfunc='size', fill_value=0)

# 重新索引，确保所有标签都出现在结果集中
result = result.reindex(columns=all_labels, fill_value=0)

# 重置索引，使 'source' 成为一列
result = result.reset_index()
print(type(result))

list = []
emoList = [0, 0, 0, 0, 0, 0, 0]
checklist = ['anger', 'disgust', 'happiness', 'like', 'sadness', 'surprise', 'fear']
for index, row in result.iterrows():
  row = dict(row)
  emo = { 'province': row['source'][2::],
          'happiness': row['happiness😁'],
          'sadness': row['sadness😭'],
          'like': row['like😘'],
          'anger': row['anger😡'],
          'disgust': row['disgust🤮'],
          'surprise': row['surprise😲'],
          'fear': row['fear😱']}
  print(emo)
  # emoList[0] = emoList[0] + emo['anger😡']
  # emoList[1] = emoList[1] + emo['disgust🤮']
  # emoList[2] = emoList[2] + emo['happiness😁']
  # emoList[3] = emoList[3] + emo['like😘']
  # emoList[4] = emoList[4] + emo['sadness😭']
  # emoList[5] = emoList[5] + emo['surprise😲']
  # emoList[6] = emoList[6] + emo['fear😱']
  emoList[0] = emoList[0] + emo['anger']
  emoList[1] = emoList[1] + emo['disgust']
  emoList[2] = emoList[2] + emo['happiness']
  emoList[3] = emoList[3] + emo['like']
  emoList[4] = emoList[4] + emo['sadness']
  emoList[5] = emoList[5] + emo['surprise']
  emoList[6] = emoList[6] + emo['fear']
  # temp = {"province": emo['source'][2::], "emotion": emo}
  list.append(emo)
emodict = dict(zip(checklist, emoList))
print(emodict)
print({'provinceResult': list, 'wholeEmotion': emodict})



# # 读取所有 unique predicted_label 值
# unique_labels_query = """
# SELECT DISTINCT predicted_label
# FROM comments;
# """

# # 读取 unique predicted_label 值
# unique_labels = pd.read_sql_query(unique_labels_query, engine)

# # 遍历每个 unique source 值，统计 predicted_label 元素的个数
# for source in unique_sources['source']:
#     query = f"""
#     SELECT 
#         predicted_label,
#         COUNT(*) AS count
#     FROM 
#         comments
#     WHERE 
#         source = '{source}'
#     GROUP BY 
#         predicted_label
#     ORDER BY 
#         count DESC;
#     """
#     # 读取查询结果
#     result = pd.read_sql_query(query, engine)
    
#     # 创建一个包含所有 predicted_label 的 DataFrame
#     all_labels = pd.DataFrame({'predicted_label': unique_labels['predicted_label'], 'count': 0})
    
#     # 合并结果，确保所有 predicted_label 都在结果中
#     merged_result = pd.merge(all_labels, result, on='predicted_label', how='left').fillna(0)
#     merged_result['count'] = merged_result['count_y'].astype(int)
#     merged_result = merged_result[['predicted_label', 'count']]
    
#     # 打印结果
#     print(f"Source: {source}")
#     # print(merged_result)
#     print("\n")