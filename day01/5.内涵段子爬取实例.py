
#-*-coding:utf-8-*-
# 2中urllib.
import urllib2
import re
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")
class Spider:
    def __init__(self):
        self.page = 1
    #内涵段子爬虫类
    def loadPage(self,page):

        url = "http://www.neihan8.com/article/list_5_" + str(page)+'.html'

        user_agent = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT6.1; Trident/5.0'
        headers = {"User-Agent":user_agent}
        request = urllib2.Request(url,headers=headers)
        response = urllib2.urlopen(request)
        print type(response.read()) # 在python2中得到的数据格式是字节模式
        print type(response.read().decode('gbk')) # ======要注意===========
        print type(response.read().decode('gbk').encode('utf-8'))
        # < type 'str' >
        # < type 'unicode' >
        # < type 'str' >
        html = response.read().decode('gbk').encode('utf-8')  # 或者加gb2312
       # 找到所有段子内容包含<div class = "f18 mb20"></div>
       # re.s，如果没有则是只匹配一行有没有符合规则的字符串，如果没有则在下一行重新分配，如果加上则是将所有字符串将一个整体进行匹配

        pattern = re.compile(r'<div.*?class="f18 mb20">(.*?)</div>',re.S)
        item_list = pattern.findall(html)  # 列表需要遍历一下不能直接返回
        for i in item_list:
            self.printOnePage(i, self.page)
        # return item_list

    def printOnePage(self,item,page):

        print "****第%d页爬取完毕****"%page
        # for item in item_list:
        #
        #     print '======='
        item = item.replace("<p>", "").replace("</p>", "").replace("<br />", "")
        self.writeToFile(item)


    def writeToFile(self,text):

        with open('./duanzi.txt','ab') as f:

            f.write(text)

    def dowork(self):

        while True:
            try:
                item_list = self.loadPage(self.page)
            except urllib2.URLError, e:
                print e.reason
                continue

            self.page += 1  # 此页处理完毕，处理下一页
            print self.page

            print "输入 quit 退出"
            command = raw_input()
            if (command == "quit"):

                break


if __name__ == '__main__':
    spider = Spider()
    spider.dowork()


