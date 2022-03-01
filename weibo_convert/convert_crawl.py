# -*- coding:utf-8 -*-

import csv
import os

from config import CRAWL_DS_MAP, REQUIRED_COLUMNS, path_to_convert, path_to_crawl


def convert_file(filename):
    write_file = open(
        os.path.join(path_to_convert, filename), "w", newline="", encoding="utf-8"
    )
    writer = csv.DictWriter(write_file, REQUIRED_COLUMNS)
    writer.writeheader()
    with open(os.path.join(path_to_crawl, filename), "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row_data = {}
            for column in REQUIRED_COLUMNS:
                row_data[column] = row[CRAWL_DS_MAP[column]]
            writer.writerow(row_data)
    write_file.close()


if __name__ == "__main__":
    for filename in os.listdir(path_to_crawl):
        convert_file(filename)
