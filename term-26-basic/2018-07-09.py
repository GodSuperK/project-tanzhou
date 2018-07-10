"""
闰年（366天，2月29天）
普通闰年：能被4整除，不能被100整除
世纪闰年：能被400整除

平年（365天，2月28天）
1,3,5,7,8,10,12 (31天)
2,4,6,9,11 (30天)
"""
DATE = {
    '1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31,
    '9': 30, '10': 31, '11': 30, '12': 31
}

def is_leap_year(y):
    """判断年份

    y: 年份
    return: bool(True=闰年，False=平年)
    """
    if not y % 400:
        return True
    elif not y % 4 and y % 100:
        return True
    else:
        return False

def day_in_year(date):
    """计算一个日期是一年中的第几天

    date: 日期
    return: str = 程序的期望输出字符串
    """
    n = 0  # n：一年中的第几天

    # 分割日期
    date_list = date.split('-')
    y = date_list[0]
    m = int(date_list[1][1]) if date_list[1][0] == '0' else int(date_list[1])
    d = int(date_list[2][1]) if date_list[2][0] == '0' else int(date_list[2])

    # 判断年份是否为闰年
    if is_leap_year(int(y)):
        DATE['2'] = 29

    # 我的天数计算算法
    for i in range(1, m):
        if not i:
            # 如果 m = 1, 则 i=None
            n += d
        else:
            n += DATE[str(i)]

    if n == d:
        output = "{}是{}年第{}天".format(date, y, n)
    else:
        output = "{}是{}年第{}天".format(date, y, n+d)
    return output

def main():
    while True:
        date = input(">>> ") # 2018-01-01
        output = day_in_year(date)
        print(output)
        if not input("继续？") in ['y', 'Y']: break

if __name__ == "__main__":
    main()
