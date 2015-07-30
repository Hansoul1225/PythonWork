#-*_coding:utf8-*-
import requests
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class spider(object):
    def __init__(self):
        print u'��ʼ��ȡ���ݡ�����'

#getsource������ȡ��ҳԴ����
    def getsource(self,url):
        html = requests.get(url)
        return html.text

#changepage����������ͬҳ��������
    def changepage(self,url,total_page):
        now_page = int(re.search('pageNum=(\d+)',url,re.S).group(1))
        page_group = []
        for i in range(now_page,total_page+1):
            link = re.sub('pageNum=\d+','pageNum=%s'%i,url,re.S)
            page_group.append(link)
        return page_group
#geteveryclass����ץȡÿ���γ̿����Ϣ
    def geteveryclass(self,source):
        everyclass = re.findall('(<li deg="".*?</li>)',source,re.S)
        return everyclass
#getinfo������ÿ���γ̿�����ȡ��������Ҫ����Ϣ
    def getinfo(self,eachclass):
        info = {}
        info['title'] = re.search('target="_blank">(.*?)</a>',eachclass,re.S).group(1)
        info['content'] = re.search('</h2><p>(.*?)</p>',eachclass,re.S).group(1)
        timeandlevel = re.findall('<em>(.*?)</em>',eachclass,re.S)
        info['classtime'] = timeandlevel[0]
        info['classlevel'] = timeandlevel[1]
        info['learnnum'] = re.search('"learn-number">(.*?)</em>',eachclass,re.S).group(1)
        return info
#saveinfo������������info.txt�ļ���
    def saveinfo(self,classinfo):
        f = open('info.txt','a')
        for each in classinfo:
            f.writelines('title:' + each['title'] + '\n')
            f.writelines('content:' + each['content'] + '\n')
            f.writelines('classtime:' + each['classtime'] + '\n')
            f.writelines('classlevel:' + each['classlevel'] + '\n')
            f.writelines('learnnum:' + each['learnnum'] +'\n\n')
        f.close()

if __name__ == '__main__':

    classinfo = []
    url = 'http://www.jikexueyuan.com/course/?pageNum=1'
    spider = spider()
    all_links = spider.changepage(url,20)
    for link in all_links:
        print u'���ڴ���ҳ�棺' + link
        html = spider.getsource(link)
        everyclass = spider.geteveryclass(html)
        for each in everyclass:
            info = spider.getinfo(each)
            classinfo.append(info)
    spider.saveinfo(classinfo)


