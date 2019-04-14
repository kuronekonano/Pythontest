import requests
from bs4 import BeautifulSoup
import bs4
def getHTMLText(url):
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    # print(r.url)
    # print(r.text)
    return r.text
def fillUnivList(ulist,html):
    soup=BeautifulSoup(html,'html.parser')
    # for it in soup.find_all('table'):
    #     print(it)
    #     print('='*30)
    for tr in soup.find_all('table')[12].children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr.find_all('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string,tds[4].string,tds[5].string,tds[6].string])
            # for it in tr.find_all('td'):
            #     print(it)
            #     print('*'*50)
def printUnivList(ulist):
    tplt="{0:^6}\t{1:<20}\t{2:{7}<32}\t{3:>10}\t{4:>10}\t{5:>10}\t{6:>10}\t"
    print(tplt.format('排名','昵称','签名','分数','AC数','提交数','AC率',chr(12288)))
    for i in ulist[1::]:
        try:
            print("{0:^6}\t{1:<20}\t{2:{7}<35}{3:>10}\t{4:>10}\t{5:>10}\t{6:>10}\t".format(i[0], i[1], i[2][:25:], i[3], i[4],i[5],i[6],chr(12288)))
        except:
            break
uinfo=[]
html=getHTMLText('http://acm.hrbust.edu.cn/index.php?m=Ranklist&a=showRatingrank&page_id=1&name=')
fillUnivList(uinfo,html)
printUnivList(uinfo)