"""
filename = question_5.py
author = 孔德成
"""

def foo(letter):
    """去重字符串,并按照ascii码表排序字符"""

    result = list(set(letter))
    result.sort()
    return '"{}"这个字符串由{}组成 '.format(letter, ' '.join(result))


def foo1(letter):
    """去重字符串,使用字符串默认排序"""
    result = []
    for i in letter:
        if letter.count(i) > 1 and i in result:
            pass
        else:
            result.append(i)
        
    return '"{}"这个字符串由{}组成 '.format(letter, ' '.join(result))


def main():
   print(foo('aadbbca')) 
   print(foo1('aadbbca')) 


if __name__ == "__main__":
    main()
