# -*- coding:utf-8 -*-
"""
@Project : CourseDesign
@File    : comment_process.py.py
@Author  : Ray
@Date    ：2024/11/19 下午8:33
"""
import os
import sys
import pandas as pd
import re


ROOT_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)
import config

config = config.Config()
data_folder: str = config.get_config("spider", "data_folder")

DATA_DIR: str = os.path.join(ROOT_DIR, data_folder)


class CommentFilter:
    def __init__(
        self,
        file_name: str,
        is_filter_cn_emoji: bool = True,
        is_filter_symbol_emoji: bool = True,
    ):
        self.file_name: str = file_name
        self.data: pd.DataFrame = pd.read_csv(os.path.join(DATA_DIR, file_name))
        self.is_filter_cn_emoji: bool = is_filter_cn_emoji
        self.is_filter_symbol_emoji: bool = is_filter_symbol_emoji

    def cn_emoji_filter(self) -> None:
        """
        中文表情过滤，删除text_raw中的中文表情([any])
        """
        self.data["text_raw"] = self.data["text_raw"].apply(
            lambda x: re.sub(r"\[.*?\]", "", x)
        )

    def symbol_emoji_filter(self) -> None:
        """
        符号表情过滤，删除text_raw中的符号表情
        """
        filter_inst = re.compile(
            "["
            "\U0001F300-\U0001F64F"
            "\U0001F680-\U0001F6FF"
            "\u2600-\u2B55 \U00010000-\U0010ffff]+"
        )
        self.data["text_raw"] = self.data["text_raw"].apply(
            lambda x: re.sub(filter_inst, "", x)
        )

    def filter(self) -> None:
        """
        根据选项过滤中文表情和符号表情
        """
        if self.is_filter_cn_emoji:
            self.cn_emoji_filter()
        if self.is_filter_symbol_emoji:
            self.symbol_emoji_filter()

    def save_filtered(self, save_name: str) -> None:
        """
        保存过滤后的数据
        :param save_name: 保存的文件名
        """
        # 去除text_raw为空的行
        self.data = self.data[self.data["text_raw"].notnull()]
        self.data.to_csv(os.path.join(DATA_DIR, save_name), index=False)


if __name__ == "__main__":
    comment_filter = CommentFilter("test.csv")
    comment_filter.cn_emoji_filter()
    comment_filter.symbol_emoji_filter()
    comment_filter.save_filtered("filtered_test1228.csv")
