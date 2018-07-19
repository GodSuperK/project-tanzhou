import pymysql
import sys

class Task(object):
    def __init__(self, *args, user='abu', password='kaduoxi123',
                 db='mytestdb', charset='utf8'):
        """
        :param args: 用户要执行的sql语句
        """
        self.SQL_STATEMENTS = args
        self.RESULTS = []
        self.db_config = {
            'user': user,
            'password': password,
            'db': db,
            'charset': charset
        }

    def work(self, sql):
        try:
            conn = pymysql.connect(**self.db_config)
        except Exception:
            print('数据库连接失败')
            sys.exit()

        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        result = cursor.execute(sql)
        if result:
            self.RESULTS.append(cursor.fetchall())
        else:
            self.RESULTS.append('语句执行失败')

        cursor.close()
        conn.close()

    def get_result(self):
        """ self.RESULTS 的结构：[[{}, ...], [{}, ...], ...] """
        # 我的格式化输出算法
        for result in self.RESULTS:
            tbl_title = result[0].keys()
            S = "+"
            V = "|"
            for title in tbl_title:
                S = S + "-" * (2 * len(title)+1) + "+"
                V = V + title.ljust(len(title)*2-1) + "|"
            print(S)
            print(V)
            print(S)
            for r in result:
                tr = '|'
                for k in r:
                    tr = tr + str(r[k]).ljust(len(k)*2) + '|'
                print(tr)
            print(S)
            print()

def main():
    SQL = [
        "select gradName as 年级, count(*) as 年级人数 from student group by gradName",
        "select gradName as 年级, count(*) as 年龄大于18 from student where age > 18 group by gradName",
        "select gradName as 年级, count(*) as 年级人数 from student where gradName ='一年级'",
        "select gradName as 年级, count(*) as 年龄大于18 from student where gradName='一年级' and age > 18"
    ]
    t = Task(*SQL)
    for sql in t.SQL_STATEMENTS:
        t.work(sql)
    t.get_result()

if __name__ == "__main__":
    main()
