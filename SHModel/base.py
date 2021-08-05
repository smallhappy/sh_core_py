# -*- coding: utf-8 -*-

import gc


class Base:
    """ 物件父類別 """

    # noinspection SpellCheckingInspection
    def __get_menbers(self):
        """ 取得所有成員變數 """
        return ', '.join("%s: %s" % item for item in vars(self).items())

    def __repr__(self):
        return self.__get_menbers()

    def __str__(self):
        return self.__get_menbers()

    def show_me_members(self):
        """ 顯示所有成員變數 """
        print(self.__get_menbers())

    def create_sql_table(self, table_name):
        """ 產生 sql 表格的語句 """

        def data_handler(member):
            """ 產生欄位名稱與欄位型態的描述 """
            classify = 'TEXT'
            if type(member[1]) is int or type(member[1]) is float:
                classify = 'NUMERIC'
            return f"\t`{member[0]}` {classify}"

        members = vars(self).items()
        members = list(members)
        members = map(data_handler, members)
        sql = f"CREATE TABLE IF NOT EXISTS `{table_name}` (\n"
        sql += ', \n'.join(members)
        sql += '\n);'
        print(sql)
        # 釋放記憶體
        del table_name, members
        gc.collect()
        return sql

    def insert_sql_table(self, table):
        """ 物件成員變數插入資料庫語法 """
        members = vars(self).items()
        members = list(members)
        keys = map(lambda member: f"`{member[0]}`", members)
        values = map(lambda member: "'" + str(member[1]).replace("'", "''").replace("\\", "\\\\") + "'", members)
        sql = f'INSERT INTO `{table}` ('
        sql += ', '.join(keys)
        sql += ') VALUES ('
        sql += ', '.join(values)
        sql += ')'
        # 釋放記憶體
        del members, keys, values
        gc.collect()
        return sql
