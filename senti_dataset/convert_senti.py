# -*- coding:utf-8 -*-
import csv

header = ["content", "label"]
column_map = {
    "content": "review",
    "label": "label"
}

def convert_file():
    write_file = open("data/convert/weibo_100k.csv", "w", encoding="utf-8", newline="")
    writer = csv.DictWriter(write_file, header)
    writer.writeheader()
    with open("data/weibo_senti_100k.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row_data = {}
            for column in header:
                if column == "label":
                    row_data[column] = 1 if row[column_map[column]] == 1 else -1
                else:
                    row_data[column] = row[column_map[column]]
            writer.writerow(row_data)
    write_file.close()


if __name__ == '__main__':
    convert_file()
