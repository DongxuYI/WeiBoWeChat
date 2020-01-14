import requests
from bs4 import BeautifulSoup
import xlrd
import xlwt
import time


def txt_xls(filename):
    print(filename)
    try:
        with open(filename, 'a+', encoding='utf-8') as f:
            xls = xlwt.Workbook()
            # 生成excel的方法，声明excel
            sheet = xls.add_sheet('sheet1', cell_overwrite_ok=True)
            index = 1
            row = 1
            while index <= 652:
                r = requests.get("http://www.shicimingju.com/category/all__" + str(index))
                bs = BeautifulSoup(r.content, features="lxml")
                for x in bs.select(".zuozhe_card"):
                    try:
                        p = x.select(".zuozhe_list_item > .zuozhe_list_des > img")[0]["src"]
                    except:
                        p = "https://"
                    name = x.select(".zuozhe_list_item > h3 > a")[0].get_text()
                    worksCount = x.select(".zuozhe_good_shici_div > a")
                    workStr = ""
                    for work in worksCount:
                        workStr += work.get_text()
                    intro = x.select(".zuozhe_list_item > .zuozhe_list_des")[0].get_text()

                    print(row, name)
                    sheet.write(row, 0, p)
                    sheet.write(row, 1, name)
                    sheet.write(row, 2, workStr)
                    sheet.write(row, 3, intro)
                    xls.save(filename)  # 保存xls文件
                    row += 1
                print("正在爬取第" + str(index) + "页")
                time.sleep(3)
                index += 1
    except:
        raise


if __name__ == '__main__':
    txt_xls("otherAuthor.xls")

