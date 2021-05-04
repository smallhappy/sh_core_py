# -*- coding: utf-8 -*-

import gc

import qrcode

ERROR_CORRECT = qrcode.constants


def quick_executing(content: str, path: str = 'output.png'):
    """
    :param content: 內容
    :type content: str
    :param path: 產出的圖檔路徑
    :type path: str
    快速產生 QRcode 圖檔
    """
    image = qrcode.make(content)
    image.save(path)
    # 釋放記憶體
    del image
    gc.collect()


def advanced_executing(
        content: str,
        version: int = None,
        error_correction: ERROR_CORRECT = ERROR_CORRECT.ERROR_CORRECT_M,
        box_size: int = 8,
        border: int = 4,
        path: str = 'output.png'
):
    """
    :param str content: 內容。
    :param int version: 決定尺寸，值為 1~40 的整數，預設值為 None ，可配合 fit 參數自動生成二維碼。
    :param ERROR_CORRECT error_correction: 誤差率。
    :param int box_size: 決定每個單元格有多少相素。
    :param int border: 決定每條邊線有多少個單元格，預設值為 4 ，也是最小值。
    :param str path: 產出的圖檔路徑。
    帶入詳細參數，產生 QRcode 圖檔
    """
    code = qrcode.QRCode(
        version=version,
        error_correction=error_correction,
        box_size=box_size,
        border=border
    )
    code.add_data(content)
    code.make(fit=True)
    image = code.make_image()
    image.save(path)
    # 釋放記憶體
    del code, image
    gc.collect()


if '__main__' == __name__:
    # quick_executing(content='test data')
    advanced_executing(content='test data', version=8, error_correction=ERROR_CORRECT.ERROR_CORRECT_H)
