import requests
from bs4 import BeautifulSoup
import xlrd
import xlwt
import time
index = 2
while index <= 252:

    r = requests.get("https://www.gushimi.org/shiren/index_"+str(index)+".html")
    bs = BeautifulSoup(r.content, features="lxml")
    for x in bs.select(".news_box"):
        p = x.select(".news_pic > a > img")[0]["src"]
        name = x.select(".news_title > a")[0].get_text()
        s = x.select(".news_summy")[0].get_text()
        chaodai = s.split(" ")[0][3:]
        numbers = s.split(" ")[1][4:-1]
        intro = x.select(".news_text > p")[0].get_text()[5:]
        works = x.select(".news_text > p")[1].select("a")
        try:
            daibiaozuo = works[0].get_text() + "、" + works[1].get_text() + "、" + works[2].get_text()
        except:
            try:
                daibiaozuo = works[0].get_text()
            except:
                daibiaozuo = ""
        # 保存文本
        try:
            with open("author.txt", 'a', encoding='utf-8') as fh:
                # 照片、姓名、朝代、作品数、简介、代表作
                fh.write(str(p) + '\t' + str(name) + '\t' + str(chaodai) + '\t' + str(numbers) + '\t' + str(intro) + '\t' + str(daibiaozuo) + '\n')

        except:
            print(index)
            print("ERROR")
            break
    print("正在爬取第"+str(index)+"页")
    time.sleep(15)
    index += 1

