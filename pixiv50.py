#encoding:utf-8
import sys
from you_get import common as you_get
print("Welcome to Pixiv Images Downloads!\nIt is come from Leo!")

year = input("输入你要爬取的Pixiv日榜年:")
month = input("输入你要爬取的Pixiv日榜月:")
day = input("输入你要爬取的Pixiv日榜日:")

if year == '0' :
    print("错误，退出执行中")
    exit()
elif month == '0' :
    url = 'https://pic.tjsky.net/pixiv/pic/' + year + '/'
    directory = r'/root/pixiv/' + year + '/'
elif day == '0' :
    url = 'https://pic.tjsky.net/pixiv/pic/' + year + '/' + month + '/'
    directory = r'/root/pixiv/' + year + '/' + month + '/'
else:
    url = 'https://pic.tjsky.net/pixiv/pic/' + year + '/' + month + '/' + day +'_daily/'
    directory = r'/root/pixiv/' + year + '/' + month + '/'+ day +'_daily/'

sys.argv = ['you-get','-o',directory,url]
you_get.main()
