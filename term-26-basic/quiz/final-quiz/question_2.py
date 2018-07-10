"""
filename = question_2.py
author = 孔德成
"""

def main():
    try:
        print(a) # raise NameError
    except NameError as e:
        print('捕获到异常<NameError: {}>'.format(e))

if __name__ == "__main__":
    main()
