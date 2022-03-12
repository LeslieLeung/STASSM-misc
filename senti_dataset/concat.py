# -*- coding:utf-8 -*-
import csv
import os

header = ["content", "label"]

def concat(file, writer):
    with open("data/convert/" + file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            writer.writerow(row)

if __name__ == '__main__':
    write_file = open("data/senti_dataset.csv", "w", encoding="utf-8", newline="")
    writer = csv.DictWriter(write_file, header)
    writer.writeheader()
    for filename in os.listdir("data/convert"):
        concat(filename, writer)
    write_file.close()