# -*- coding:utf-8 -*-
import pandas as pd
import pandas_profiling as pp

data = pd.read_csv("data/senti_dataset_nodup.csv")
report = pp.ProfileReport(data)
report.to_file("data/senti_dataset_nodup_report.html")