import requests
from bs4 import BeautifulSoup
import xlrd
import xlwt
import time
index = 1

try:
    with open("poetry.xls", 'a+', encoding='utf-8') as f:
        xls = xlwt.Workbook()
        sheet = xls.add_sheet('sheet1', cell_overwrite_ok=True)
        row = 1
        while index <= 100:
            r = requests.get("https://so.gushiwen.org/shiwen/default_0AA"+str(index)+".aspx")
            bs = BeautifulSoup(r.content, features="lxml")

            for x in bs.select(".left > .sons"):
                # print(x)
                title = x.select(".cont > p")[0].select("a > b")[0].get_text()
                author = x.select(".cont > p")[1].select("a")[1].get_text()
                content = x.select(".cont > .contson")[0].get_text()
                tags = x.select(".tag > a")
                tagList = []
                for tag in tags:
                    tagList.append(tag.get_text())
                tagStr = '，'.join(tagList)
                # # 保存文本
                for i in range(1, 5):  # 1,2,3,4
                    if i == 1:
                        item = title
                    if i == 2:
                        item = author
                    if i == 3:
                        item = content
                    if i == 4:
                        item = tagStr
                    print(row, i, item)
                    sheet.write(row, i - 1, item)  # x单元格行，i 单元格列

                    xls.save("poetry.xls")  # 保存xls文件
                row += 1  # excel另起一行
            index += 1
            print("正在爬取第" + str(index) + "页")
            time.sleep(10)

except:
    raise




