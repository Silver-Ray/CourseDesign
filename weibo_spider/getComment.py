import requests
import pandas as pd
from pandas import DataFrame
from time import sleep
import re
from tqdm import tqdm
import sys
import os
from jsonpath_ng import parse

# 将CourseDesign文件夹添加到系统路径中
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from weibo_spider.weiboMID import url_to_mid


class WeiboComment:
    def __init__(
        self,
        cookie: str,
        referer: str,
        post_url: str,
        data_folder: str = "data",
        times: int = 10,
        sleep_time: float = 1,
        columns: list = None,
    ):
        if columns is None:
            columns = ["created_at", "id", "text_raw", "source"]
        self.headers = {
            # 用户身份信息
            "cookie": cookie,
            # 防盗链
            "referer": referer,
            # 浏览器基本信息
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
        }
        self.post_url: str = post_url
        self.times: int = times
        self.sleep_time: float = sleep_time
        self.columns: list[str] = columns
        self.comment_req_url: str = "https://weibo.com/ajax/statuses/buildComments"
        self.post_req_url: str = "https://weibo.com/ajax/statuses/show"
        self.data: DataFrame = pd.DataFrame(columns=self.columns)
        self.data_folder: str = data_folder

    def get_url_param(self) -> dict:
        """
        根据URL获取评论的id和用户id
        """
        match = re.search(r"https://weibo\.com/(\d+)/(\w+)", self.post_url)
        if match:
            user_id: int = int(match.group(1))
            mid_raw: str = match.group(2)
        else:
            raise ValueError("Invalid URL")
        mid: int = url_to_mid(mid_raw)
        params: dict = {
            "flow": 0,
            "is_reload": 1,
            "id": mid,  # 评论的微博由原始id转换为int型
            "is_show_bulletin": 2,
            "is_mix": 0,
            "max_id": 0,  # 评论的起始id
            "count": 20,
            "uid": user_id,  # 微博博主的用户id
            "mid": mid_raw,  # 评论的微博原始id
        }
        return params

    def get_comment(self) -> None:
        """
        获取评论
        """
        params: dict = self.get_url_param()
        with requests.Session() as session:
            for _ in tqdm(range(self.times), desc="Fetching comments"):
                try:
                    response = session.get(
                        url=self.comment_req_url, headers=self.headers, params=params
                    )
                    response.raise_for_status()
                    json_data = response.json()
                except requests.RequestException as e:
                    print(f"Request failed in getting comment: {e}")
                    continue

                try:
                    df_temp: DataFrame = pd.DataFrame(json_data["data"])
                except KeyError:
                    print("\nNo data")
                    continue
                if df_temp.empty:
                    continue
                df_temp["created_at"] = pd.to_datetime(
                    df_temp["created_at"], format="%a %b %d %H:%M:%S %z %Y"
                ).dt.strftime("%Y-%m-%d %H:%M:%S")
                # NOTE: 强制添加name列
                df_temp["name"] = df_temp["user"].apply(lambda x: x["screen_name"])
                self.data = pd.concat(
                    [self.data, df_temp[["name"] + self.columns]], ignore_index=True
                )
                params["max_id"] = json_data["max_id"]
                sleep(self.sleep_time)
            self.data.dropna().reset_index(drop=True)

    def save_comment(self, file_name: str) -> None:
        path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), self.data_folder
        )
        if not os.path.exists(path):
            os.makedirs(path)
        file_name = os.path.join(path, file_name)
        self.data.to_csv(file_name, index=False, encoding="utf-8-sig")

    def get_post(self) -> dict:
        """
        获取微博正文内容，包括内容、点赞数、评论数、转发数
        :return: 微博正文内容
        """
        mid_raw = self.get_url_param()["mid"]
        params: dict = {
            "locale": "zh-CN",
            "isGetLongText": "True",
            "id": mid_raw,
        }
        try:
            post = requests.get(self.post_req_url, headers=self.headers, params=params)
            post_json = post.json()
            post.close()
        except requests.RequestException as e:
            print(f"Request failed in getting post: {e}")
            return {}
        content_matches = [match.value for match in parse("$..content").find(post_json)]
        content = (
            content_matches[0]
            if content_matches
            else [match.value for match in parse("$..text_raw").find(post_json)][0]
        )
        name = [match.value for match in parse("$..screen_name").find(post_json)][0]
        likes = [match.value for match in parse("$..attitudes_count").find(post_json)][
            0
        ]
        comment_num = [
            match.value for match in parse("$..comments_count").find(post_json)
        ][0]
        repost_num = [
            match.value for match in parse("$..reposts_count").find(post_json)
        ][0]
        post_data = {
            "content": content,
            "name": name,
            "likes": likes,
            "comment_num": comment_num,
            "repost_num": repost_num,
        }
        return post_data


if __name__ == "__main__":
    # 用户身份信息
    cookie = "SCF=ApEj9sNUAs6Q6qECaLgUkAS9qE_l1245d4cUSrxtG-DNdgPb6Lpn1-Ww_dcHx9oVkvgb03t5_D0TKyJLZPnokV8.; SINAGLOBAL=6502505958420.25.1729328476798; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5S.77Uc_09SwMjB2bmVC6q5JpX5KMhUgL.FoMNSoMpSo27SK22dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNS0qNeKqpeh-p; ULV=1732603224517:6:4:2:1597940990394.8838.1732603224421:1732018418082; XSRF-TOKEN=UDYUlkcbUKVQnrjn1A8_9Zcf; ALF=1735382880; SUB=_2A25KTDoPDeRhGeFJ7VUQ9i_Mzj2IHXVpIDPHrDV8PUJbkNAGLRPjkW1Nf05FtxQIFN41IyBPJvPPvureiiGIkTNJ; WBPSESS=CIq1nOqC6X2VXYb4WSS3wMMZgAxDuEFKpcViCkzq5bBMgc2xrKrIuhLrc3ODgw3JL4jwW1LKp5rEzRjFeETwq8J33BnbtFaVvVMGcSczZ6IqPSkIF1fdbjfNUlNwokISvnGPewU0sg0QAztjGus7mA=="
    # 防盗链
    referer = "https://weibo.com/7724913317/P2iofcS15"
    post_url = "https://weibo.com/7724913317/P2iofcS15"

    comment = WeiboComment(cookie, referer, post_url, times=200)
    comment.get_comment()
    comment.save_comment("out.csv")
