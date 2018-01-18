#-*-coding:utf-8-*-
#ProxyBasicAuthHandler(代理授权验证)
# HTTPPasswordMgrWithDefaultRealm()：来保存私密代理的用户密码
# ProxyBasicAuthHandler()：来处理代理的身份验证。

import urllib
import urllib2

# 私密代理授权的账户
user = 'mr_mao_hacker'
passwd = "sffqry9r"

# 私密代理ip
proxyserver = "61.158.163:16816"

# 构建一个密码管理器对象，用来保存需要处理的用户名和密码
passwdmgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

# 添加账户信息，第一个参数realm适于远程服务器相关的域信息，一般没人管它都是写None，后面三个参数分别是 代理服务器、用户名、密码
passwdmgr.add_password(None,proxyserver,user,passwd)
#ProxyBasicAuthHandler(代理授权验证)
# 构建一个代理基础用户名/密码验证的ProxyBasicAuthHandler处理器对象
#参数是密码管理器对象
#注意这里不再使用普通的ProxyHandler类了
proxyauth_handler = urllib2.ProxyBasicAuthHandler(passwdmgr)
# 通过 build_opener()方法使用这些代理Handler对象，创建自定义opener对象，参数包括构建的 proxy_handler 和 proxyauth_handler
opener = urllib2.build_opener(proxyauth_handler)

request = urllib2.Request('http://www.baidu.com')

response = opener.open(request)

print response.read()


















