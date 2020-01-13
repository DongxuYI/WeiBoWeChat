import requests
from bs4 import BeautifulSoup
import xlrd
import xlwt
import time

# 上次爬到了2000页
user = 2000


def spider(user):
    try:
        index = 1
        with open(str(user) + ".xls", 'a+', encoding='utf-8') as f:
            xls = xlwt.Workbook()
            sheet = xls.add_sheet('sheet1', cell_overwrite_ok=True)
            row = 1

            r = requests.get("http://www.shicimingju.com/chaxun/zuozhe/" + str(user) + ".html")
            page = BeautifulSoup(r.content, features="lxml")
            all = len(page.select("#list_nav_all > a")) or len(page.select("#list_nav_part > a")) or 1
            try:
                author = page.select(".about_zuozhe > div > div > h4")[0].get_text()
            except:
                author = ""
            print(user, author)
            while index <= all:
                print("正在爬取第" + str(index) + "页")
                if index == 1:
                    url = "http://www.shicimingju.com/chaxun/zuozhe/" + str(user) + ".html"
                else:
                    url = "http://www.shicimingju.com/chaxun/zuozhe/" + str(user) + "_" + str(index) + ".html"

                r = requests.get(url)
                bs = BeautifulSoup(r.content, features="lxml")

                # print(bs)

                for x in bs.select(".shici_card > div"):
                    # print(x)
                    if not x.get_text():
                        continue

                    title = x.select(".shici_list_main > h3 > a")[0].get_text()
                    content = x.select(".shici_content")[0].get_text().replace(' ', '').replace("\n", "").replace("\r", "")
                    # print(index, title)
                    # print(content)
                    # # 保存文本
                    for i in range(1, 4):  # 1,2,3
                        if i == 1:
                            item = title
                        if i == 2:
                            item = author
                        if i == 3:
                            item = content
                        # print(row, i, item)
                        sheet.write(row, i - 1, item)  # x单元格行，i 单元格列

                        xls.save(str(user) + ".xls")  # 保存xls文件
                    row += 1  # excel另起一行
                index += 1
                time.sleep(1)
            else:
                pass
                # user += 1
                # spider(user)
    except:
        raise


startIndex = 1040


def readexcel(startIndex):
    if startIndex > 2000:
        return
    print(startIndex)
    # 打开文件
    data = xlrd.open_workbook(str(startIndex) + '.xls')

    try:
        # 通过文件名获得工作表,获取工作表
        table = data.sheet_by_name('sheet1')
        # 获取某个单元格的值
        cel_B3 = table.cell(1, 0).value
        if not cel_B3:
            pass
            print(startIndex)
        else:
            startIndex += 1
            readexcel(startIndex)
    except:
        spider(startIndex)
        startIndex += 1
        readexcel(startIndex)






if __name__ == '__main__':
    readexcel(startIndex)



