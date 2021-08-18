# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import Error


class DatabaseManager:
    """ 資料庫 """

    sleep_time = 0.055
    """ 避免連續操作，導致錯誤的間隔時間 """

    show_console = False
    """ 是否印出資料庫操作 """

    def __init__(self, config):
        try:
            self.__db = mysql.connector.connect(
                host=config.host,
                user=config.user,
                password=config.password,
                database=config.database,
                charset='utf8',
            )
            """ 資料庫實例 """
            self.__cursor = self.__db.cursor()
            """ 資料庫光標 """
        except Error as error:
            print(f'👻 database_manager error: {error}')
            self.__db.rollback()

    @property
    def db(self):
        return self.__db

    def execute_sql(self, sql):
        if self.show_console:
            print(sql)
        try:
            self.__cursor.execute(sql)
        except mysql.connector.IntegrityError as error:
            print(f'👻 database_manager error: {error}')
            self.__db.rollback()
        except Error as error:
            print(f'👻 database_manager error: {error}')
            self.__db.rollback()

    def show_databases(self):
        """ 顯示資料庫 """
        sql = 'SHOW DATABASES'
        self.execute_sql(sql)
        databases = self.__cursor.fetchall()
        for database in databases:
            print(database)

    def show_tables(self):
        """ 顯示表格 """
        sql = 'SHOW TABLES'
        self.execute_sql(sql)
        tables = self.__cursor.fetchall()
        for table in tables:
            print(table)

    def create_table(self, sql):
        self.execute_sql(sql)

    def select_data(self, sql):
        """ 讀取數據 """
        self.execute_sql(sql)
        return self.__cursor.fetchall()

    def insert_data(self, sql):
        """ 插入數據 """
        self.execute_sql(sql)
        self.__db.commit()

    def delete_data(self, sql):
        """ 插入數據 """
        self.execute_sql(sql)
        self.__db.commit()