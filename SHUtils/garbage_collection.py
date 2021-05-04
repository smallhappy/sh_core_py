# -*- coding: utf-8 -*-

import gc


def gc_enable():
    # 記憶體控管
    gc.enable()
    if gc.isenabled():
        print('啟用自動(記憶體)垃圾回收，並提高第一代垃圾與第二代垃圾回收的頻率')
        gc.set_threshold(550, 8, 4)
    else:
        raise Exception('啟用記憶體控管失敗')
