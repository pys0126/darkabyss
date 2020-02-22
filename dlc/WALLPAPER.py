'''
    手机壁纸爬取网址：https://mobile.alphacoders.com/by-device/524/Redmi-Note-7-Wallpapers?page=1
    电脑壁纸爬取网址：https://wall.alphacoders.com/featured.php?lang=Chinese
'''

from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re
import os
import time

#手机壁纸爬虫
def Phoneimg():
    page = input("\t-----输入抓取起始页（末页343）：")
    page1 = input("\t-----输入抓取页数：")
    print("\t---%-本脚本由PYS编写-%---")
    print("\t-----欢迎访问我的网站：https://darkabyss.top -----")
    print('\t===按Ctrl+C结束运行===\n')
    time.sleep(1)
    os1 = input("\t-----是否创建文件,创建了填N（Y/N）：")

    if page == "1":
        print("\t-----创建文件中...-----")
        time.sleep(1)
        os.mkdir("C:\\Users\\Administrator\\Downloads\\phoneimg\\")
        print("\t-----文件创建成功-----")
        print("\t-----下载好的壁纸可在C盘\\Users\\Administrator\\Downloads\\的phoneimg文件夹下查看-----")
    else:
        if os1 == "y" or os1 == "Y":
            print("\t-----创建文件中...-----")
            time.sleep(1)
            os.mkdir("C:\\Users\\Administrator\\Downloads\\phoneimg\\")
            print("\t-----文件创建成功-----")
            print("\t-----下载好的壁纸可在C盘\\Users\\Administrator\\Downloads\\的phoneimg文件夹下查看-----")
        else:
            pass

    p = 0
    y = 0
    print("\t-----开始爬取-----")

    for w in range(int(page1)):
        p += 1
        htm = urlopen("https://mobile.alphacoders.com/by-device/524/Redmi-Note-7-Wallpapers?page=" + str(int(page)+p-1)).read().decode("utf-8")
        html = BeautifulSoup(htm,"lxml")
        all_a1 = html.find_all("div",{"class":"thumb-element"})
        print("\t-----开始下载图片-----\n")
        for i in all_a1:
            y += 1
            all_url = i["id"]
            pipei =  re.compile(r'\d+')
            pipei_allurl = pipei.findall(all_url)
            s = 0
            print("\t=")
            for b in all_url:
                s += 1
                if s == 2:
                    break
                else:
                    pass
                print("\t==")
                all_img = urlopen("https://mobile.alphacoders.com/wallpapers/view/" + pipei_allurl[0]).read().decode("utf-8")
                text_html = BeautifulSoup(all_img,"lxml")
                all_a2 = text_html.find_all("div",{"class":"center"})
                print("\t======")
                for l in all_a2:
                    all_img = l.find_all("img",{"class":"img-full-size"})
                    for m in all_img:
                        img = m["src"]
                        img_down = requests.get(img)
                        img_name = "C:\\Users\\Administrator\\Downloads\\img\\" + pipei_allurl[0] + ".jpg"
                        with open(img_name,"wb") as f:
                            f.write(img_down.content)
            print("\t=================")
            print("\t-----已下载第" + str(y) + "张图片-----")
        print("\t-----已完成第" + str(int(page)+p-1) + "页的爬取-----\n")

#电脑壁纸爬虫
def PCimg():
    print('/////-✨-本脚本由PYS创建-✨-/////')
    print("===欢迎访问我的网站：https://darkabyss.top===")
    print('===按Ctrl+C结束运行===')

    z = 0
    page = int(input('===输入抓取起始页：'))
    T_of_F = input('===是否创建文件,创建了填N(Y/N)：')
    time.sleep(1)

    if page == 1:
        print('===创建文件中===')
        time.sleep(1)
        os.makedirs('C:\\Users\\Administrator\\Downloads\\PCimg\\')
        print('===创建成功===')
        print("===下载好的壁纸可在C盘\\Users\\Administrator\\Downloads\\的PCimg文件夹下查看===")
    else:
        if T_of_F == 'y' or T_of_F == 'Y':
            print('===创建''PCimg''文件===')
            time.sleep(1)
            os.makedirs('C:\\Users\\Administrator\\Downloads\\PCimg\\')
            print('===创建成功===')
            print("===下载好的壁纸可在C盘\\Users\\Administrator\\Downloads\\的PCimg文件夹下查看===")
        else:
            pass

    for ss in range(int(input('===输入抓取页数：'))):
        page += 1
        htm = urlopen("https://wall.alphacoders.com/featured.php?lang=Chinese&page=" + str(page)).read().decode("utf-8")
        html = BeautifulSoup(htm,features="html.parser")
        all_a1 = html.find_all("div",{"class":"boxgrid"})
        print('\n')
        print('===开始下载图片===')
        print('\n')

        for i in all_a1:
            all_href = i.find_all("a")
            print('/')
            for l in all_href:
                all_url = l["href"]
                print('//')
                html1 = "https://wall.alphacoders.com/" + all_url
                print('///')
                html2 = urlopen(html1).read().decode("utf-8")
                print('////')
                text_html = BeautifulSoup(html2,features="html.parser")
                print('/////')
                all_a2 = text_html.find_all("picture")
                print('//////')

                for x in all_a2:
                    all_img = x.find_all("img")
                    print('///////')
                    for s in all_img:
                        z += 1
                        img_url = s['src']
                        img_file = 'C:\\Users\\Administrator\\Downloads\\PCimg\\' + str(page*30+z-30) + '.png'
                        print('////////')
                        r = requests.get(img_url)
                        print('/////////')
                        with open(img_file,'wb') as f:
                            f.write(r.content)
                        print('===已下载第' + str(z) + '张图片')
        print('===已完成第' + str(page-1) + '页===\n')

#开始...
while True:
    string = print("\t*****欢迎使用自动下载壁纸脚本*****\n")
    input_str = input("\t*****输入'PC'下载电脑壁纸，输入'PH'下载手机壁纸*****\n\t*****在此输入(PC/PH)：")    
    if input_str == "pc" or input_str == "PC":
        PCimg()
        PCtrue = input("\t*****继续请按Y，退出请按N：")
        if PCtrue == "y" or PCtrue == "Y":
            pass
        else:
            break
    elif input_str == "ph" or input_str == "PH":
        Phoneimg()
        PHtrue = input("\t*****继续请按Y，退出请按N：")
        if PHtrue == "y" or PCtrue == "Y":
            pass
        else:
            break
    else:
        print("\t*****输入错误请重新输入或者按Ctrl+C退出本脚本*****\n")
        continue




