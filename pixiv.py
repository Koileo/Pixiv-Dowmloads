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
    i = 1
    j = 1
    while i <= 12:
        if(i<10):
            if(j<10):
                url = 'https://pic.tjsky.net/pixiv/pic/' + year + '/' + '0' + month + '/' + '0' + str(f) +'_daily/'
                os.makedirs('https://pic.tjsky.net/pixiv/pic/' + year + '/' + '0' + month + '/' + '0' + str(f) +'_daily/')
                directory = 'https://pic.tjsky.net/pixiv/pic/' + year + '/' + '0' +  month + '/' + '0' + str(f) +'_daily/'
                sys.argv = ['you-get','-o',directory,url]    
                you_get.main()
            elif(j>=10):
                url = 'https://pic.tjsky.net/pixiv/pic/' + year + '/' + '0' + month + '/' + str(f) +'_daily/'
                os.makedirs('https://pic.tjsky.net/pixiv/pic/' + year + '/' + '0' + month + '/' +  + str(f) +'_daily/')
                directory = 'https://pic.tjsky.net/pixiv/pic/' + year + '/' + '0' + month + '/' +  + str(f) +'_daily/'
                sys.argv = ['you-get','-o',directory,url]    
                you_get.main()
            j+=1
        if(i>=10):
            if(j<10):
                url = 'https://pic.tjsky.net/pixiv/pic/' + year + '/' + str(i) + '/' + '0' + str(j) +'_daily/'
                os.makedirs(where + year + '/'+ str(i) + '/' + '0' + str(j) +'_daily/')
                directory = where + year + '/'+ str(i) + '/' + '0' + str(j) +'_daily/'
                sys.argv = ['you-get','-o',directory,url]
                you_get.main()
            elif(j>=10):
                url = 'https://pic.tjsky.net/pixiv/pic/' + year + '/' + str(i) + '/' + str(j) +'_daily/'
                os.makedirs(where + year + '/'+ str(i) + '/' + str(j) +'_daily/')
                directory = where + year + '/'+ str(i) + '/' + str(j) +'_daily/'
                sys.argv = ['you-get','-o',directory,url]
                you_get.main()    
            j+=1
        i+=1
elif day == '0' :
    f=1
    while f<31:
        if(f<10):
            url = 'https://pic.tjsky.net/pixiv/pic/' + year + '/' + month + '/' + '0' + str(f) +'_daily/'
            os.makedirs('https://pic.tjsky.net/pixiv/pic/' + year + '/' + month + '/' + '0' + str(f) +'_daily/')
            directory = 'https://pic.tjsky.net/pixiv/pic/' + year + '/' + month + '/' + '0' + str(f) +'_daily/'
            sys.argv = ['you-get','-o',directory,url]    
            you_get.main()
        elif(f>=10):
            url = 'https://pic.tjsky.net/pixiv/pic/' + year + '/' + month + '/' + str(f) +'_daily/'
            os.makedirs('https://pic.tjsky.net/pixiv/pic/' + year + '/' + month + '/' +  + str(f) +'_daily/')
            directory = 'https://pic.tjsky.net/pixiv/pic/' + year + '/' + month + '/' +  + str(f) +'_daily/'
            sys.argv = ['you-get','-o',directory,url]    
            you_get.main()
        f+=1

else:
    url = 'https://pic.tjsky.net/pixiv/pic/' + year + '/' + month + '/' + day +'_daily/'
    os.makedirs(where + year + '/' + month + '/'+ day +'_daily/')
    directory = where + year + '/' + month + '/'+ day +'_daily/'
    sys.argv = ['you-get','-o',directory,url]
    you_get.main()
