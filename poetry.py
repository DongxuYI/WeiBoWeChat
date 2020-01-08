import requests
from bs4 import BeautifulSoup
import xlrd
import xlwt
import time
index = 1
while index <= 1:

    r = requests.get("https://so.gushiwen.org/shiwen/default_0AA"+str(index)+".aspx")
    bs = BeautifulSoup(r.content, features="lxml")
    print(len(bs.select(".left > .sons")))
    for x in bs.select(".left > .sons"):
        title = x.select(".cont > p")[0].select("a > b")[0].get_text()
        author = x.select(".cont > p")[1].select("a")[1].get_text()
        print(author)
        # # 保存文本
        # try:
        #     with open("author.txt", 'a', encoding='utf-8') as fh:
        #         # 照片、姓名、朝代、作品数、简介、代表作
        #         fh.write(str(p) + '\t' + str(name) + '\t' + str(chaodai) + '\t' + str(numbers) + '\t' + str(intro) + '\t' + str(daibiaozuo) + '\n')
        #
        # except:
        #     print(index)
        #     print("ERROR")
        #     break
    # print("正在爬取第"+str(index)+"页")
    # time.sleep(15)
    index += 1

