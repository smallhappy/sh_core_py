# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)


def config(
        secret_key: str = 'any_random_string',
        upload_folder: str = 'upload/',
        max_content_length: int = 16 * 1024 * 1024,
        json_as_ascii: bool = False,
):
    # 對 session 進行加密
    app.secret_key = secret_key
    # 定义上传文件夹的路径
    app.config['UPLOAD_FOLDER'] = upload_folder
    # 限制16MB
    app.config['MAX_CONTENT_LENGTH'] = max_content_length
    # 默认情况下 Flask 使用 ascii 编码来序列化对象。如果这个值被设置为 False
    # ， Flask不会将其编码为 ASCII，并且按原样输出，返回它的 unicode 字符串。
    # 比如 jsonfiy 会自动地采用 utf-8 来编码它然后才进行传输。
    app.config['JSON_AS_ASCII'] = json_as_ascii
    app.config['SECRET_KEY'] = secret_key


def run(
        templates_auto_reload: bool = True,
        jinja_env_auto_reload: bool = True,
        host: str = '127.0.0.1',
        port: str = '5000',
        debug: bool = True,
        threaded: bool = True
):
    # 當 flask 偵測到 template 有修改後，會自動去更新。
    app.config['TEMPLATES_AUTO_RELOAD'] = templates_auto_reload
    # 因 jinja 具有 cache ，所以也要設定重啟。
    app.jinja_env.auto_reload = jinja_env_auto_reload
    # host: 要监听的主机名。默认为127.0.0.1（localhost）。设置为“0.0.0.0”以使服务器在外部可用。
    # port: 默认值为5000。
    app.run(host=host, port=port, debug=debug, threaded=threaded)
    # debug 配置也可以用另一種寫法。
    # app.debug = True
    # app.run()


if '__main__' == __name__:
    config()
    run()

# /Users/jeff/Developer/PycharmProjects/SHCorePy/SHFlask/wsgi.py
# 終端機運行指令： gunicorn wsgi:app
# 終端機運行指令： gunicorn --thread=50 main:application
