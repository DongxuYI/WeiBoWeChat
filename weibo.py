'''
抓取并保存 正文、图片、发布时间、点赞数、评论数、转发数
抓取的微博id：
洋葱故事会   https://m.weibo.cn/u/1806732505
'''

# -*-coding:utf8-*-
# 需要的模块
import os
import urllib
import urllib.request
import time
import json
import xlwt

# 定义要爬取的微博大V的微博ID
# 2409114274 黑龙江省图书馆
# 2608219435 哈尔滨市图书馆
# 6128752536 齐齐哈尔图书馆
# 鸡西市图书馆
# 6329499161 鹤岗市图书馆
# 双鸭山市图书馆
# 3800463069 大庆市图书馆
# 伊春市图书馆
# 佳木斯市图书馆
# 七台河图书馆
# 6233305361 牡丹江市图书馆
# 1707407605 绥化市北林区图书馆
# 1373517133 吉林省图书馆
# 2727738163 长春市图书馆
# 1080087592 吉林省吉林市图书馆
# 5087890014 四平市图书馆
# 辽源市图书馆
# 6225156153 通化市图书馆
# 白山市图书馆
# 松原市图书馆
# 白城市图书馆
# 3504018477 辽宁省图书馆
# 3349135200 沈阳市图书馆
# 2043274575 大连图书馆
# 2786857105 鞍山市图书馆
# 1944439460 抚顺市图书馆
# 1745228087 本溪市图书馆
# 丹东市图书馆
# 6260486243 锦州市图书馆
# 1400563524 营口图书馆
# 阜新市图书馆
# 5977347236 辽阳市图书馆
# 5678809695 盘锦市图书馆
# 6146856129 铁岭市图书馆
# 2475474210 辽宁省朝阳市图书馆
# 葫芦岛市图书馆

ids = [
    "2409114274",
    "2608219435",
    "6128752536",
    "6329499161",
    "3800463069",
    "6233305361",
    "1707407605",
    "1373517133",
    "2727738163",
    "1080087592",
    "5087890014",
    "6225156153",
    "3504018477",
    "3349135200",
    "2043274575",
    "2786857105",
    "1944439460",
    "1745228087",
    "6260486243",
    "1400563524",
    "5977347236",
    "5678809695",
    "6146856129",
    "2475474210"
]

id = '6128752536'

# 设置代理IP

proxy_addr = "122.241.72.199:808"


# 定义页面打开函数
def use_proxy(url, proxy_addr):
    req = urllib.request.Request(url)
    req.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
    proxy = urllib.request.ProxyHandler({'http': proxy_addr})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
    return data


# 获取微博主页的containerid，爬取微博内容时需要此id
def get_containerid(url):
    data = use_proxy(url, proxy_addr)
    content = json.loads(data).get('data')
    for data in content.get('tabsInfo').get('tabs'):
        if (data.get('tab_type') == 'weibo'):
            containerid = data.get('containerid')
    return containerid


# 获取微博大V账号的用户基本信息，如：微博昵称、微博地址、微博头像、关注人数、粉丝数、性别、等级等
def get_userInfo(id):
    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=' + id
    data = use_proxy(url, proxy_addr)
    content = json.loads(data).get('data')
    profile_image_url = content.get('userInfo').get('profile_image_url')
    description = content.get('userInfo').get('description')
    profile_url = content.get('userInfo').get('profile_url')
    verified = content.get('userInfo').get('verified')
    guanzhu = content.get('userInfo').get('follow_count')
    name = content.get('userInfo').get('screen_name')
    fensi = content.get('userInfo').get('followers_count')
    gender = content.get('userInfo').get('gender')
    urank = content.get('userInfo').get('urank')
    print("微博昵称：" + name + "\n" + "微博主页地址：" + profile_url + "\n" + "微博头像地址：" + profile_image_url + "\n" + "是否认证：" + str(
        verified) + "\n" + "微博说明：" + description + "\n" + "关注人数：" + str(guanzhu) + "\n" + "粉丝数：" + str(
        fensi) + "\n" + "性别：" + gender + "\n" + "微博等级：" + str(urank) + "\n")
    return name


# 保存图片
def savepic(pic_urls, created_at, page, num, filename):
    pic_num = len(pic_urls)
    srcpath = 'weibo_img/' + filename + '/'
    if not os.path.exists(srcpath):
        os.makedirs(srcpath)
    picpath = str(created_at) + 'page' + str(page) + 'num' + str(num) + 'pic'
    for i in range(len(pic_urls)):
        picpathi = picpath + str(i)
        path = srcpath + picpathi + ".jpg"
        urllib.request.urlretrieve(pic_urls[i], path)


# 获取微博内容信息,并保存到文本中，内容包括：每条微博的内容、微博详情页面地址、点赞数、评论数、转发数等
def get_weibo(id, file, filename):
    i = 1
    while True:
        url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=' + id
        weibo_url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=' + id + '&containerid=' + get_containerid(
            url) + '&page=' + str(i)
        try:
            data = use_proxy(weibo_url, proxy_addr)
            content = json.loads(data).get('data')
            cards = content.get('cards')
            if (len(cards) > 0):
                for j in range(len(cards)):
                    print("-----正在爬取第" + str(i) + "页，第" + str(j) + "条微博------")
                    card_type = cards[j].get('card_type')
                    if (card_type == 9):
                        mblog = cards[j].get('mblog')
                        attitudes_count = mblog.get('attitudes_count')  # 点赞数
                        comments_count = mblog.get('comments_count')  # 评论数
                        created_at = mblog.get('created_at')  # 发布时间
                        reposts_count = mblog.get('reposts_count')  # 转发数
                        if mblog.get('retweeted_status'):  # 是否原创
                            retweet = "原创"
                        else:
                            retweet = "转发"

                        scheme = cards[j].get('scheme')  # 微博地址
                        text = mblog.get('text')  # 微博内容
                        pictures = mblog.get('pics')  # 正文配图，返回list
                        pic_urls = []  # 存储图片url地址
                        if pictures:
                            for picture in pictures:
                                pic_url = picture.get('large').get('url')
                                pic_urls.append(pic_url)
                        # print(pic_urls)

                        # 保存文本
                        with open(file, 'a', encoding='utf-8') as fh:
                            if len(str(created_at)) < 6:
                                created_at = str(created_at)
                            # 页数、条数、微博地址、发布时间、微博内容、点赞数、评论数、转发数、图片链接
                            fh.write(str(i) + '\t' + str(j) + '\t' + str(scheme) + '\t' + str(
                                created_at) + '\t' + text + '\t' + str(attitudes_count) + '\t' + str(
                                comments_count) + '\t' + str(reposts_count) + '\t' + str(pic_urls) + '\t' + retweet + '\n')

                        # 保存图片
                        savepic(pic_urls, created_at, i, j, filename)
                i += 1
                '''休眠1s以免给服务器造成严重负担'''
                time.sleep(1)
            else:
                break
        except Exception as e:
            print(e)
            pass


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


if __name__ == "__main__":
    name = get_userInfo(id)
    txtname = str(name) + id + ".txt"
    xlsname = str(name) + id + ".xls"

    if os.path.exists(txtname):
        os.remove(txtname)

    get_weibo(id, txtname, name)

    if os.path.exists(xlsname):
        os.remove(xlsname)
    txt_xls(txtname, xlsname)

print('finish')
