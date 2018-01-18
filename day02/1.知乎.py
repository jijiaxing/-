from bs4 import BeautifulSoup
#-*-coding:utf-8-*-
import requests

def zhihuLogin():
    # 构建一个session对象，可以保存cookie
    sess = requests.Session()

    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}

    html = sess.get("https://www.zhihu.com/#signin",headers=headers)
    # 调用lxml解析哭
    bs = BeautifulSoup(html,"lxml")

    # 获取之前get页面里的_xsrf,跨域攻击
    # 跨于攻击伪造网站信任的用户请求,盗取用户信息，欺骗服务器
    # 所以网站会通过设置一个隐藏字段来存放MD5字符串，这个字服来验证cookie和session的一种方式
    _xsrf= bs.find("input",attrs={"name":"_xsrf"}).get("value")
    print _xsrf

zhihuLogin()