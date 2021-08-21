#encoding:utf-8
import sys
import os
from you_get import common as you_get
print("Welcome to Pixiv Images Downloads!\nIt is come from Leo!")
where = input("输入你要爬取的Pixiv的下载地址")
year = input("输入你要爬取的Pixiv日榜年:")
month = input("输入你要爬取的Pixiv日榜月:")
day = input("输入你要爬取的Pixiv日榜日:")

if year == '0' :
    print("错误，退出执行中")
    exit()
elif month == '0' :
    url = 'https://pic.tjsky.net/pixiv/pic/' + year + '/'
    os.mkdir(where + year + '/')
    directory = where + year + '/'
elif day == '0' :
    url = 'https://pic.tjsky.net/pixiv/pic/' + year + '/' + month + '/'
    os.mkdir(where + year + '/' + month + '/')
    directory = where + year + '/' + month + '/'
else:
    url = 'https://pic.tjsky.net/pixiv/pic/' + year + '/' + month + '/' + day +'_daily/'
    os.mkdir(where + year + '/' + month + '/'+ day +'_daily/')
    directory = where + year + '/' + month + '/'+ day +'_daily/'
sys.argv = ['you-get','-o',directory,url]
you_get.main()
