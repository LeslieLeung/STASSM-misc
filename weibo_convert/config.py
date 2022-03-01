# -*- coding:utf-8 -*-

REQUIRED_COLUMNS = ["content", "comment_num", "like_num", "publish_time"]

V2_DS_MAP = {
    "content": "content",
    "comment_num": "comment_num",
    "like_num": "like_num",
    "publish_time": "created_at",
}

CRAWL_DS_MAP = {
    "content": "content",
    "comment_num": "comment_num",
    "like_num": "like_num",
    "publish_time": "publish_time",
}

path_to_convert = "./data/convert/"
path_to_crawl = "./data/crawl/"
path_to_v2 = "./data/v2/"
