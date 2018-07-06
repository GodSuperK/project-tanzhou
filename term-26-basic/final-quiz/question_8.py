"""
filename = question_8.py
author = 孔德成
"""
def exchange_body_1(d, l):
    if len(d) == len(l):
        print('参数长度不符合要求')
        return

    d1 = dict(zip(d, l))
    d_v = d.values() 
    t1 = tuple(list(d_v)[:len(d1)])
    return d1, t1

def main():
    # len(d) < len(l)
    d = {'a': 'a', 'b': 'b'}
    l = [1, 2, 3]
    # len(d) > len(l)
    d1 = {'a': 'a', 'b': 'b', 'c': 'c'}
    l1 = [1, 2]
    print("len(d) < len(l)", exchange_body_1(d, l))
    print("len(d) > len(l)", exchange_body_1(d1, l1))

if __name__ == "__main__":
    main()
