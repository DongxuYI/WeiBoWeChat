import requests
import xlrd
import time
import pymysql  # 连接数据库
import xlrd


conn = pymysql.connect(host='47.101.170.173', user='root', passwd='YI.9694482664', port=3306, db='poetry', charset='utf8')
try:
    data = xlrd.open_workbook('content/author.xls')
    # 通过文件名获得工作表,获取工作表
    table = data.sheet_by_name('sheet1')
    # 获取行数和列数
    print("总行数：" + str(table.nrows))
    print("总列数：" + str(table.ncols))

    row = 1
    cur = conn.cursor()
    while True:

        if row > table.nrows:
            break
        values = table.cell(row, 1).value
        sql = "select * from author where name = (%s)"  # SQL语句
        res = cur.execute(sql, values)  # 执行SQL语句
        data = cur.fetchone()
        if res:
            id = data[0]
            avatar = data[18]
            updateSql = "UPDATE author SET workscount=(%s), biography=(%s), avatar=(%s) where id = (%s)"
            cur.execute(updateSql, [table.cell(row, 3).value, table.cell(row, 4).value, table.cell(row, 0).value, id])
            conn.commit()
            print("已存在")
        else:
            print("未存在")
            insertSql = "insert into author (name,avatar,dynasty, workscount,biography,masterpiece) values (%s,%s,%s,%s,%s,%s)"
            cur.execute(insertSql, [
                table.cell(row, 1).value,
                table.cell(row, 0).value,
                table.cell(row, 2).value,
                table.cell(row, 3).value,
                table.cell(row, 4).value,
                table.cell(row, 5).value
            ])
            conn.commit()
        # time.sleep(5)
        row += 1
    cur.close()
    conn.close()  # 关闭连接

except:
    conn.close()  # 关闭连接
    pass



