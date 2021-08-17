import gc

import requests
from bs4 import BeautifulSoup


class Crawler:
    """ 專案爬蟲父類別 """

    base_url: str = ''
    """ 後台網址 """
    url: str = ''
    """ 爬蟲目標網址 """
    payload: dict
    """ 請求挾帶的參數，此專案用不到 """
    headers: dict
    """ 請求挾帶的參數 """

    def __init__(self, path: str = '', headers: dict = None):
        """
        爬蟲建構子

        :param path: 網址
        :param headers: 可用於設定 cookie
        """
        self.url = self.base_url + path
        self.payload = {}
        if headers:
            self.headers = headers
        else:
            self.headers = {}

    def get_soup(self):
        """ 取得爬取數據 """
        # 發出請求
        response = requests.request("GET", self.url, headers=self.headers, data=self.payload)
        self.headers = response.cookies.get_dict()
        soup = BeautifulSoup(response.text, 'html.parser')
        # 釋放記憶體
        del response
        gc.collect()
        # 回傳結果
        return soup
