# -*- coding:utf-8 -*-


def fix(data):
    if isinstance(data, str):
        string = str.replace(data, "﻿", "")
        string = str.replace(string, " ", "")
        return string
    else:
        return data
