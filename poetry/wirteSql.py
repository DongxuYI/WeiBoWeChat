import pymysql  # 连接数据库
import xlrd
import sys

sys.setrecursionlimit(1000000000)  # 例如这里设置为

conn = pymysql.connect(host='47.101.170.173',
                       user='root',
                       passwd='YI.9694482664',
                       port=3306,
                       db='poetry',
                       charset='utf8'
                       )

# 没有导入
startIndex = 924
def readexcel(startIndex):
    # 1175
    if startIndex > 1174:
        return
    conn.commit()
    print(startIndex)
    # 打开文件
    data = xlrd.open_workbook('content/'+str(startIndex)+'.xls')

    # 通过文件名获得工作表,获取工作表
    try:
        table = data.sheet_by_name('sheet1')
        # 获取行数和列数
        # 行数：table.nrows
        # 列数：table.ncols
        print("总行数：" + str(table.nrows))
        print("总列数：" + str(table.ncols))
        # 获取某个单元格的值
        row = 1

        def insertSql(startIndex, row, total):
            if row > total - 1:
                startIndex += 1

                readexcel(startIndex)
                return

            title1 = table.cell(row, 0).value
            author1 = table.cell(row, 1).value
            content1 = table.cell(row, 2).value
            cur = conn.cursor()  # 生成游标对象
            sql = "insert into poem (title, content, author) values (%s, %s, %s)"  # SQL语句
            values = (title1, content1, author1)
            print(startIndex, author1, row, total)
            cur.execute(sql, values)  # 执行SQL语句
            cur.close()  # 关闭游标

            row += 1
            insertSql(startIndex, row, total)

        insertSql(startIndex, row, table.nrows)
    except:
        startIndex += 1

        readexcel(startIndex)


readexcel(startIndex)

conn.close()  # 关闭连接
