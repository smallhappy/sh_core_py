# -*- coding: utf-8 -*-

from .config import Config


class DatabaseConfig(Config):
    """ 資料庫設定檔 """

    def __init__(self, path):
        super().__init__(path)
        self.host = self.child('DATABASE')['HOST']
        self.user = self.child('DATABASE')['USER']
        self.password = self.child('DATABASE')['PASSWORD']
        self.database = self.child('DATABASE')['DATABASE']
