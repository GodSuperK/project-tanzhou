"""
question_1.py
"""

def main():
    data_type = {
            '[数值类型]': {
                '[int]': ('a = 1', ),
                '[float]': ('a = 1.1', ),
                '[bool]': ('a = True', 'b = False'),
                '[decimal.Decimal]': (
                    'from decimal import Decimal', 'a = Decimal(1.12)'),
                '[complex]': ('a = 1 + 2j', ) 
                },
            '[序列类型]': {
                '[list]': (
                    'li_1 = [1, 2, "a string"]',
                    'li_2 = [1, [3, 4], True]'),
                '[tuple]': ('tu_1 = (1, )', 'tu_2 = (1, 2)'),
                '[str]': ('s1 = "Hello, World!"', ),
                '[bytes]': ('b1 = b"Hello, World!"', )
                },
            '[散列类型]': {
                '[set]': ('set_a = set("abc")', 'set_b = {"a", "b", "c"}'),
                '[dict]': ('{"name": "abu", "age": 20}', )
                }
            }
    for k1, v1 in data_type.items():
        print(k1)
        for k2, v2 in v1.items():
            print('\t', k2,)
            for i in v2:
                print('\t\t', i)
    

if __name__ == "__main__":
    main()
