#-*-coding:utf-8-*-
# HTTPPasswordMgrWithDefaultRealm()：来保存私密代理的用户密码
# ProxyBasicAuthHandler()：来处理代理的身份验证。
#如果我们有客户端的用户名和密码，我们可以通过下面的方法去访问爬取

import urllib
import urllib2

user = 'test'
passwd = '123456'

webserver = 'http://192.168.199.107'

passwdmgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

passwdmgr.add_password(None,webserver,user,passwd)

#构建一个HTTP基础用户名/密码验证的HTTPBasicAuthHandler处理器对象，参数是创建的密码管理对象

# 基础验证处理器
httpauth_handler = urllib2.HTTPBasicAuthHandler(passwdmgr)

opener = urllib2.build_opener(httpauth_handler)#可以有多个处理器

# 可以选择通过install_opener()方法定义opener为全局opener

urllib2.install_opener(opener)

request = urllib2.Request('http://192.168.199.107')
response = urllib2.urlopen(request)
print(response.read())

















