# -*- coding: utf-8 -*-

from flask import jsonify

from .base import Base


class Response(Base):
    __error = {
        'code': '',
        'message': ''
    }
    """ 錯誤物件 """
    __content = ''
    """ 資料內容 """

    def __init__(self):
        pass

    def __init__(self, error_code='', error_message='', content=''):
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


default_response = Response().set_error_message('未知的錯誤').set_content('failure')
""" 預設回應，未知錯誤 """
