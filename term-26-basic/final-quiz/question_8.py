"""
filename = question_5.py
author = 孔德成
"""

def exchange_body(d, iter2):
    if len(d) == len(iter2):
        print('参数长度不符合要求')
        return

    if hasattr(d, 'keys') and not hasattr(iter2, 'keys'):
        if len(d) < len(iter2):
            result_d = dict(zip(d, iter2))
            result_t = tuple(d.values())
        # TODO(len(d)> len(iter2))
        return result_d, result_t
    else:
        print('arg1 is not dict-like object, or arg2不是除类字典对象以外的可迭代对象')
        return


