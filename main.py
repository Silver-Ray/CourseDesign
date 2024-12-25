# -*- coding:utf-8 -*-
"""
@Project : CourseDesign
@File    : main.py
@Author  : Ray
@Date    ：2024/10/19 下午4:58
"""
from weibo_spider.getComment import WeiboComment
from comment_process.comment_process import CommentFilter
from config import Config

# load config
user_config = Config()
COOKIE = user_config.get_config('spider', 'COOKIE')
save_name = user_config.get_config('spider', 'save_name')
URL = user_config.get_config('spider', 'URL')
data_folder = user_config.get_config('spider', 'data_folder')
times = int(user_config.get_config('spider', 'times'))
interval = float(user_config.get_config('spider', 'interval'))
columns = user_config.get_config('spider', 'columns').split(',')
weiboComment = WeiboComment(post_url=URL, cookie=COOKIE, referer=URL, times=times, sleep_time=interval, columns=columns,
                            data_folder=data_folder)
weiboComment.get_comment()
weiboComment.save_comment(save_name)
comment_filter = CommentFilter(save_name, True, True)
comment_filter.filter()
comment_filter.save_filtered('filtered_' + save_name)
