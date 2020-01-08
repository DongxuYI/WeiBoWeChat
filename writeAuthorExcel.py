import xlwt

try:
    with open("author.txt", 'r', encoding='utf-8') as f:
        xls = xlwt.Workbook()
        # 生成excel的方法，声明excel
        sheet = xls.add_sheet('sheet1', cell_overwrite_ok=True)
        sheet.write(0, 0, '图片地址')
        sheet.write(0, 1, '姓名')
        sheet.write(0, 2, '朝代')
        sheet.write(0, 3, '作品数')
        sheet.write(0, 4, '简介')
        sheet.write(0, 5, '代表作')

        x = 1
        while True:
            # 按行循环，读取文本文件
            line = f.readline()
            if not line:
                break  # 如果没有内容，则退出循环
            for i in range(0, len(line.split('\t'))):
                item = line.split('\t')[i]
                sheet.write(x, i, item)  # x单元格行，i 单元格列
            x += 1  # excel另起一行
    xls.save("author.xls")  # 保存xls文件
except:
    raise