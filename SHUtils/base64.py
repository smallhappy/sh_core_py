# -*- coding: utf-8 -*-

import base64
import gc

ENCODING = 'UTF-8'


def binarize(content: str) -> bytes:
    """
    :param content: 要進行轉換的內文
    :type content: str
    :return: 轉換為 bytes 的結果
    :rtype: bytes
    將字串轉為 bytes ，供 base64 編碼或解碼使用。
    """
    return content.encode(ENCODING)


def encode(content: str) -> str:
    """
    :param content: 要進行編碼的內文
    :type content: str
    :return: 透過 base64 編碼的結果
    :rtype: str
    將字串透過 base64 進行編碼。
    """
    binary = binarize(content)
    result = base64.b64encode(binary).decode(ENCODING)
    # 釋放記憶體
    del binary
    gc.collect()
    return result


def decode(content: str) -> str:
    """
    :param content: 要進行解碼的內文
    :type content: str
    :return: 透過 base64 解碼的結果
    :rtype: str
    將字串透過 base64 進行解碼。
    """
    binary = binarize(content)
    result = base64.b64decode(binary).decode(ENCODING)
    # 釋放記憶體
    del binary
    gc.collect()
    return result


if '__main__' == __name__:
    message = encode('aa1234')
    print('🤧', message)
    message = decode(message)
    print('🤧', message)
    # 釋放記憶體
    del message
    gc.collect()
