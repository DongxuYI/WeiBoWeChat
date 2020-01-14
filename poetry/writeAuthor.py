import xlwt


def txt_xls(filename, xlsname):
    """
    :文本转换成xls的函数
    :param filename txt文本文件名称、
    :param xlsname 表示转换后的excel文件名
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            xls = xlwt.Workbook()
            # 生成excel的方法，声明excel
            sheet = xls.add_sheet('sheet1', cell_overwrite_ok=True)
            # 页数、条数、微博地址、发布时间、微博内容、点赞数、评论数、转发数
            sheet.write(0, 0, '爬取页数')
            sheet.write(0, 1, '爬取当前页数的条数')
            sheet.write(0, 2, '微博地址')
            sheet.write(0, 3, '发布时间')
            sheet.write(0, 4, '微博内容')
            sheet.write(0, 5, '点赞数')
            sheet.write(0, 6, '评论数')
            sheet.write(0, 7, '转发数')
            sheet.write(0, 8, '图片链接')
            sheet.write(0, 9, '是否原创')
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
        xls.save(xlsname)  # 保存xls文件
    except:
        raise


if __name__ == '__main__':
    txt_xls("author.txt", "otherAuthor.xls")
