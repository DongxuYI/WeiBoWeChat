import time
import pymysql  # 连接数据库
from pymysql.cursors import DictCursor
import xlrd


def main():
    conn = pymysql.connect(host='47.101.170.173', user='root', passwd='YI.9694482664', port=3306, db='poetry', charset='utf8')
    try:

        page = 0
        cur = conn.cursor(DictCursor)
        cur.execute("SELECT name,dynasty from author")
        total = cur.fetchall()
        totalLen = len(total)
        print(page, totalLen)
        while True:
            if page >= totalLen:
                break
            sql = "UPDATE poem set dynasty = (%s) where author = (%s)"  # SQL语句
            cur.execute(sql, [total[page]['dynasty'], total[page]['name']])  # 执行SQL语句
            print(page, total[page]['dynasty'], total[page]['name'])
            conn.commit()
            page += 1
        cur.close()
        conn.close()  # 关闭连接
    except:
        print("error")
        conn.close()  # 关闭连接
        pass


if __name__ == '__main__':
    main()
