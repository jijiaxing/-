# -*- coding:utf-8 -*-
import urllib
import urllib2

def loadPage(url,filename):
    print '正在下载'+filename
    headers = {'User-Agent':"Mozilla/5.0"}
    request = urllib2.Request(url,headers=headers)
    return urllib2.urlopen(request).read()


def writePage(html,filename):

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