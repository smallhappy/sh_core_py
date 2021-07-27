# -*- coding: UTF-8 -*-

import sys


def deal_recursion(limit: int = 9500):
    sys.setrecursionlimit(limit)  # 遞迴次數，突破預設上限！
    print('trecursion_limit:', sys.getrecursionlimit())
