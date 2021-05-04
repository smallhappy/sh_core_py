# -*- coding: utf-8 -*-

import datetime
import gc
import random
import string


def get_now_time(formatter='%Y-%m-%d %H:%M:%S'):
    """ 取得現在時間 """
    today = datetime.datetime.today()
    formatted_time = today.strftime(formatter)
    # 釋放記憶體
    del today
    gc.collect()
    return formatted_time


def get_random_alphabets(suffix_digits: int = 4) -> str:
    """
    英文大小寫字母的隨機字串。

    :param suffix_digits: 隨機字串數量，預設為 4 碼；若賦值零或負數，則回傳空字串。
    :return: 隨機字串
    """
    results = ''
    for index in range(0, suffix_digits):
        # ascii_letters = string.ascii_lowercase + string.ascii_uppercase
        # 符號: string.punctuation
        results += random.choice(string.ascii_letters)
    return results


def get_auto_id(suffix_digits: int = 4) -> str:
    """
    產生自動編號，由年月日時分秒，加上後綴隨機碼組成。

    :param suffix_digits: 後綴隨機碼數量，預設為 4 碼；若賦值零或負數，則移除後綴隨機碼。
    :return: 自動編號。
    """
    formatted_time = get_now_time(formatter="%Y%m%d%H%M%S")
    suffix_code = format(random.randint(1, 10 ** suffix_digits - 1), f'0{suffix_digits}d') if suffix_digits > 0 else ''
    auto_id = formatted_time + suffix_code
    # 釋放記憶體
    del formatted_time, suffix_code
    gc.collect()
    return auto_id
