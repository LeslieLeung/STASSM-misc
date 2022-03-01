# weibo_convert

将两个来源的微博数据统一成能够导入到MongoDB的格式。

## 目录结构

- weibo_convert
    - data
        - convert 转换输出文件夹
        - crawl 爬取数据集
        - v2 v2数据集
    - config.py 配置类
    - convert_crawl.py 转换爬取数据集
    - convert_V2.py 转换v2数据集
    - README.md 本文件
    - utils.py 工具函数

## 使用方法

分别运行`convert_crawl.py`和`convert_V2.py`，输出文件会在`data/convert`文件夹中。