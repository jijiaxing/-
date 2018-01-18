# -*- coding:utf-8 -*-
from lxml import etree
import urllib
import urllib2

import urllib
import urllib2

def loadPage(url,filename):

    print '正在下载'+filename
    headers = {'User-Agent':"Mozilla/5.0"}
    request = urllib2.Request(url,headers=headers)
    html = urllib2.urlopen(request).read()
    content = etree.HTML(html) #解析为HTML DOM模型
    # 所有匹配成功集合
    link_list = content.xpath("//div[@class='threadlist_lz clearfix']//a[@class='j_th_tit ']/@href")
    for link in link_list:

        fulllink  = link + "http://tieba.baidu.com"
        writeImage(fulllink)
def loadImage(link):

    request = urllib2.Request(link,headers=headers)
    response = urllib2.urlopen(request)
def writeImage(link):
    urllib2.Request(link,headers=headers)
    with open(filename,"w") as f:
        f.write(html)

def tiebaSpider(url,beginPage,endPage):
    for page in range(beginPage,endPage+1):
        pn = (page-1)*50
        filename = '第'+str(pn)+'页.html'
        fullurl = url + "$pn=" + str(pn)
        html = loadPage(fullurl,filename)
        writePage(html,filename)

if __name__ == '__main__':
    kw = raw_input('请输入爬取的贴吧名：')
    beginPage = int(raw_input('请输入开始页：'))
    endPage = int(raw_input('请输入结束页：'))

    url = 'https://tieba.baidu.com/f?'
    key = urllib.urlencode({"kw":kw})
    fullurl = url + key
    tiebaSpider(fullurl,beginPage,endPage)