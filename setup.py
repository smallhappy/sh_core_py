# -*- coding: UTF-8 -*-

# 初始化虛擬環境
# python -m venv env-name
# 啟動虛擬環境
# windows: env-name\Scripts\activate.bat
# unix:    source env-name/bin/activate
# 終止虛擬環境(在虛擬環境模式下)
# deactivate

# 查看專案環境套件
# pip list --format=columns (或 pip freeze ，但有點不知道在幹嘛)
# 導出專案環境套件
# pip freeze > requirements.txt
# 安裝 requirements.txt 記錄的套件
# pip install -r requirements.txt

# TODO 添加例外處理
# 參考資料1 https://www.runoob.com/python/python-exceptions.html
# 參考資料2 https://openhome.cc/Gossip/Python/TryRaise.html
# 參考資料3 https://openhome.cc/Gossip/Python/Assert.html

import gc

from setuptools import setup, find_packages


def packaging():
    # 可用「 python setup.py check 」來檢測資訊是否正確。
    # 可用「 python setup.py sdist 」來進行打包，產生 *.tar.gz 。
    # 可用「 pip install *.tar.gz 」來進行本地安裝。
    # 安裝完畢後，可用「import SHUtils」引入專案，並以「SHUtils.base64.encode()」呼叫。
    packages = find_packages(exclude=['dev'])  # 自動查找含有 __init__.py 的資料夾。
    print('find_packages:', packages)
    setup(
        name='SHCorePy',  # pip list --format=columns 或 pip uninstall 時的名稱
        version='0.1.1',
        author='jeff',
        author_email='neonn800885@hotmail.com',
        url='https://github.com/smallhappy',
        packages=packages,  # 需要打包的目錄列表
        install_requires=[
            'flask', 'gunicorn',
            'qrcode==6.1', 'image==1.5.33',
            'mysql-connector-python==8.0.21',
            'requests', 'beautifulsoup4'
        ],  # 依賴的套件
    )
    # 釋放記憶體
    del packages
    gc.collect()


if '__main__' == __name__:
    packaging()
