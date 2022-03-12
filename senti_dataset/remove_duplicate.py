# -*- coding:utf-8 -*-
import pandas as pd

data = pd.read_csv("data/senti_dataset.csv", encoding="utf-8")
data = data.drop_duplicates()
data.to_csv("data/senti_dataset_nodup.csv", index=False, encoding="utf-8")