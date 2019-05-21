# -*- coding: UTF-8 -*-

'''
作者: 王兴春
用途：使用Python判断平年闰年
场景：Python系列——ArcGIS Desktop二次开发（Python版本）——Python基础学习
2019/05/21
'''
 
year = int(input("输入一个年份: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print(u"{0} 是闰年".format(year))   # 整百年能被400整除的是闰年
       else:
           print(u"{0} 不是闰年".format(year))
   else:
       print(u"{0} 是闰年".format(year))       # 非整百年能被4整除的为闰年
else:
   print(u"{0} 不是闰年".format(year))
