#-*-coding:utf-8-*-
# cookielib模块：主要作用是提供用于存储cookie的对象
# HTTPCookieProcessor处理器：主要作用是处理这些cookie对象，并构建handler对象。

import urllib2
import cookielib
#CookieJar()对象保存cookie值
cookie = cookielib.CookieJar()

# 来创建cookie处理器对象，参数为cookiejar()对象
handle = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(handle)
# 以get方法访问页面，访问之后会自动保存cookie到cookiejar中
opener.open("http://www.baidu.com")

## 可以按标准格式将保存的Cookie打印出来
cookieStr = ''
for item in cookie:

    cookieStr = cookieStr+item.name+"="+item.value+";"

print cookieStr[:-1]