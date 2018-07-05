"""
filename = question_7.py
author = 孔德成
"""

def which_order(seq):
    try:
        li_seq = list(seq)
    except Exception:
        print("'seq' object is not iterable.")
    if sorted(li_seq) == li_seq:
        print("UP")
    elif sorted(li_seq, reverse=True) == li_seq:
        print("DOWN")
    else:
        print(None)
    



