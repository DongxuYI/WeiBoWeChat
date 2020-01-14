import xlrd


def readexcel(startIndex):
    print(startIndex)
    # 打开文件
    data = xlrd.open_workbook('content/'+str(startIndex)+'.xls')

    # 通过文件名获得工作表,获取工作表
    table = data.sheet_by_name('sheet1')
    # 获取行数和列数
    print("总行数：" + str(table.nrows))
    print("总列数：" + str(table.ncols))
    # 获取某个单元格的值
    row = 1

    def getInfo(row, total):
        if row > total:
            return

        avatar = table.cell(row, 0).value
        name = table.cell(row, 1).value
        print(name, avatar)
        row += 1
        getInfo(row, total)

    getInfo(row, table.nrows)