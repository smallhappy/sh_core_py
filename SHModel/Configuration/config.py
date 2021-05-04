# -*- coding: utf-8 -*-

# 找到同級路徑的檔案
# import os
# path = os.path.dirname(os.path.abspath(__file__)).join(['database.ini'])

import configparser

from ..base import Base


class Config(Base):
    """ 設定檔父類別 """

    def __init__(self, name):
        self.__config = configparser.ConfigParser()
        self.__config.read(name)

    def child(self, name):
        """ 查找子結點 """
        return self.__config[name]
