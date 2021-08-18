# -*- coding: utf-8 -*-

from typing import Dict

from flask import jsonify

from .base import Base


class Response(Base):
    __error: Dict[str, str]
    """ 錯誤物件 """
    __content: str
    """ 資料內容 """

    def __reset(self):
        self.__error = {
            'code': '',
            'message': ''
        }
        self.__content = ''

    def __init__(self):
        self.__reset()

    def __init__(self, error_code='', error_message='', content=''):
        self.__reset()
        self.set_data(error_code, error_message, content)

    def set_error_code(self, error_code):
        """ 設定錯誤代碼 """
        self.__error['code'] = error_code
        return self

    def set_error_message(self, error_message):
        """ 設定錯誤訊息 """
        self.__error['message'] = error_message
        return self

    def set_content(self, content):
        """ 設定回應內容 """
        self.__content = content
        return self

    def set_data(self, error_code='', error_message='', content=''):
        """ 設定完整參數 """
        self.set_error_code(error_code)
        self.set_error_message(error_message)
        self.set_content(content)
        return self

    def to_json_object(self):
        """ 將 model 轉為 json 物件 """
        result = {
            'error': self.__error,
            'content': self.__content
        }
        return jsonify(result)


default_error = Response(content='failure', error_message='未知的錯誤')
""" 預設回應，未知錯誤 """

default_success = Response(content='success')
""" 預設回應，成功！！ """
