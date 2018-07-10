"""
filename = question_3.py
author = 孔德成
"""

    
def main():
    with open('log.txt', 'r', encoding='utf8') as f:
        for i in f:
            print(i, end='')

if __name__ == "__main__":
    main()
