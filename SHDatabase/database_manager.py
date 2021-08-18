# -*- coding: utf-8 -*-

import mysql.connector
from SHModel.Configuration.database_config import DatabaseConfig
from mysql.connector import Error


class DatabaseManager:
    """ 資料庫 """

    sleep_time: float = 0.055
    """ 避免連續操作，導致錯誤的間隔時間 """

    show_console: bool = False
    """ 是否印出資料庫操作 """

    def __init__(self, config: DatabaseConfig):
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

    def __del__(self):
        if self.__db.is_connected():
            self.__cursor.close()
            self.__db.close()

    def execute_sql(self, sql: str, with_commit: bool = False):
        if self.show_console:
            print(sql)
        try:
            self.__cursor.execute(sql)
            if with_commit:
                self.__db.commit()
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

    def create_table(self, sql: str):
        self.execute_sql(sql)

    def select_data(self, sql: str, fetchone: bool = False):
        """ 讀取數據 """
        self.execute_sql(sql)
        return self.__cursor.fetchall() if not fetchone else self.__cursor.fetchone()

    def select_amount(self, sql: str) -> int:
        self.execute_sql(sql)
        self.__cursor.fetchall()
        return self.__cursor.rowcount

    def select_exist(self, sql: str) -> bool:
        is_exist = self.select_data(sql=f"SELECT EXISTS({sql})", fetchone=True)
        return bool(is_exist[0])

    def modify_data(self, sql: str):
        """ 插入或更新數據 """
        self.execute_sql(sql, with_commit=True)

    def delete_data(self, sql: str):
        """ 插入數據 """
        self.execute_sql(sql, with_commit=True)
