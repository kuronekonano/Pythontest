import datetime
import socket
import threading
import urllib.request

import pymysql
from bs4 import BeautifulSoup
import re
from urllib import request
import time
from lxml import etree

lock = threading.Lock()
lock_num = threading.Lock()
NUM = 0


class Spider(object):
    def __init__(self):
        self.send_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
            'Referer': 'https://movie.douban.com/explore'
        }
        self.hotMovieUrl_list = []
        self.movieDetailInfo_list = []
        global lock
        global lock_num
        self.Num = 0
        self.starttime = datetime.datetime.now()
        self.endtime = datetime.datetime.now()

    # 爬取豆瓣Top250名【第一层】
    def getHotMovieUrlList(self, page_1):
        movie = []
        for i in range(int(page_1)):
            url = "https://movie.douban.com/top250?start=" + str(i * 25) + "&filter="
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
            page = request.Request(url, headers=headers)
            page_info = request.urlopen(page).read().decode('utf-8')
            soup = BeautifulSoup(page_info, 'html.parser')
            titles = soup.select('#content > div > div.article > ol > li > div > div.info > div.hd > a ')
            for title in titles:
                musicurl = re.findall('<a class="" href="[^"]+', str(title))[0].strip('<a class="" hre').strip('f="')
                print(musicurl)
                movie.append(musicurl)
        return movie

    # 爬取豆瓣Top250详细信息【第二层】
    def getMovieDetailInfo(self, movie_url,c):
        movieDetailInfo_dict = {}  # 存储电影详细信息的字典
        resp = urllib.request.urlopen(movie_url)
        html_data = resp.read().decode('utf-8')
        # 构建xpath
        html = etree.HTML(html_data)
        movie_year = html.xpath('//*[@id="content"]/h1/span[2]/text()')[0].strip('(').strip(')')  # 年份
        movieDetailInfo_dict['movie_year'] = movie_year
        movie_name = html.xpath('//*[@id="content"]/h1/span[1]/text()')[0].split(' ')[0]  # 电影名
        movieDetailInfo_dict['movie_name'] = movie_name
        # 导演
        if (c[1]==1):
            movie_director_list = html.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')
            director = ""
            for directors in movie_director_list:
                director += str(directors) + "/"
                movie_director = director.strip('/')
                movieDetailInfo_dict['movie_director'] = movie_director
        else:
             movieDetailInfo_dict['movie_director'] = "Null"
        # 编剧
        if (c[2]==1):
            movie_writer_list = html.xpath('//*[@id="info"]/span[2]/span[2]/a/text()')
            writer = ""
            for writers in movie_writer_list:
                writer += str(writers) + "/"
            movie_writer = writer.strip('/')
            movieDetailInfo_dict['movie_writer'] = movie_writer
        else:
            movieDetailInfo_dict['movie_writer'] = 'NULL'
        # 演员
        movie_actor_list = html.xpath('//*[@id="info"]/span[3]/span[2]/a/text()')
        actor = ""
        for actors in movie_actor_list:
            actor += str(actors) + "/"
        movie_actor = actor.strip('/')
        movieDetailInfo_dict['movie_actor'] = movie_actor
        # 类型
        if(c[3]==1):
            movie_type_list = html.xpath('//*[@id="info"]/span[@property="v:genre"]/text()')
            type = ""
            for types in movie_type_list:
                type += str(types) + "/"
            movie_type = type.strip('/')
            movieDetailInfo_dict['movie_type'] = movie_type
        else:
            movieDetailInfo_dict['movie_type'] = 'NULL'
        # 别名
        movieDetailInfo_dict['movie_anotherName'] = ""
        # 语言
        movieDetailInfo_dict['movie_language'] = ""
        # 国家/地区
        movieDetailInfo_dict['movie_country'] = ""
        movie_attrs = html.xpath('//*[@id="info"]/span[@class="pl"]')
        for attr in movie_attrs:
            if attr.text == '制片国家/地区:':
                movie_country = attr.tail.strip()
                movieDetailInfo_dict['movie_country'] = movie_country
            if attr.text == '语言:':
                movie_language = attr.tail.strip()
                movieDetailInfo_dict['movie_language'] = movie_language
            if attr.text == '又名:':
                movie_anotherName = attr.tail.strip()
                movieDetailInfo_dict['movie_anotherName'] = movie_anotherName

        movie_date = html.xpath('//*[@id="info"]/span[@property="v:initialReleaseDate"]/@content')[0]
        # 上映日期
        movieDetailInfo_dict['movie_date'] = movie_date
        # 片长
        try:
            movie_time = html.xpath('//*[@id="info"]/span[@property="v:runtime"]/text()')[0]
        except:
            movie_time = "无片长信息"
        movieDetailInfo_dict['movie_time'] = movie_time
        # IMDB链接
        movieDetailInfo_dict['movie_IMDB'] = ""
        movie_IMDB = html.xpath('//*[@id="info"]/a[@rel="nofollow" and @target="_blank"]/text()')
        if len(movie_IMDB) != 0:
            movieDetailInfo_dict['movie_IMDB'] = movie_IMDB[0]
        #grade
        movie_grade = html.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')[0]
        # 评分
        if(c[4]==1):
            movieDetailInfo_dict['movie_grade'] = movie_grade
        else:
            movieDetailInfo_dict['movie_grade'] ='NULL'

        movie_commentsNum = html.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/div/div[2]/a/span/text()')[0]
        # 评价人数
        movieDetailInfo_dict['movie_commentsNum'] = movie_commentsNum
        # 电影详情页面URL地址
        movie_pageUrl = movie_url
        movieDetailInfo_dict['movie_pageUrl'] = movie_pageUrl

        # 短评
        movieDetailInfo_dict['movie_comment'] = self.get_comments(movie_url + 'comments?status=F')
        # 论坛
        movieDetailInfo_dict['movie_discussion'] = self.get_discussion(movie_url + 'discussion/')
        # 爬取结果是字典，表示单部电影的所有详细信息
        return movieDetailInfo_dict

    # 第一条短评
    def get_comments(self,comments_url):
        resp = urllib.request.urlopen(comments_url)
        html_data = resp.read().decode('utf-8')
        # 构建xpath
        html = etree.HTML(html_data)
        return html.xpath('//*[@id="comments"]/div[1]/div[2]/p/span/text()')[0]

    # 论坛第一条题目
    def get_discussion(self,discussion_url):
        resp = urllib.request.urlopen(discussion_url)
        html_data = resp.read().decode('utf-8')
        # 构建xpath
        html = etree.HTML(html_data)
        try:
            return html.xpath('//*[@id="posts-table"]//tr[2]/td[1]/a/text()')[0].strip('\n').strip()
        except:
            return  "论坛内容为空"

    # 爬取豆瓣电影Top250简介【第三层】
    def getMovieDetailInfo_list(self, movie_urls,b,y,conn1):
        # conn = pymysql.connect(host='localhost', user='root', password='colin123', db='base', port=3306, charset='utf8')
        for url in movie_urls:
            time.sleep(1)
            movieDetailInfo = self.getMovieDetailInfo(url,b)  # 【第二层】爬取详细信息
            # movie_info = self.saveDatabase(movieDetailInfo, conn)
            lock_num.acquire()
            global NUM
            NUM = NUM + 1
            self.Num=NUM
            lock_num.release()
            num = NUM
            # 从这里开始构建返回到客户端的信息
            movie_msg = '爬取的第' + str(num) + '条电影信息\n'
            movie_msg += '*****************************************\n'
            movie_msg += '【上映年份】' + movieDetailInfo['movie_year'] + '\n【片名】' + movieDetailInfo['movie_name'] + '\n【导演】' + \
                         movieDetailInfo['movie_director'] + '\n【编剧】' + movieDetailInfo['movie_writer'] + '\n【主演】' + movieDetailInfo[
                             'movie_actor'] + '\n【类型】' + movieDetailInfo['movie_type'] + '\n【制片国家地区】' + movieDetailInfo[
                             'movie_country'] + '\n【语言】' + movieDetailInfo['movie_language'] + '\n【上映日期】' + movieDetailInfo[
                              'movie_date'] + '\n【片长】' + movieDetailInfo['movie_time'] + '\n【又名】' + movieDetailInfo[
                             'movie_anotherName'] + '\n【IMDB链接】' + movieDetailInfo['movie_IMDB'] + '\n【评分】' + movieDetailInfo[
                             'movie_grade'] + '\n【评价人数】' + movieDetailInfo['movie_commentsNum'] + '\n【页面网址】' + movieDetailInfo[
                             'movie_pageUrl'] + '\n【短评】' + movieDetailInfo['movie_comment'] + '\n【论坛讨论】' + movieDetailInfo[
                             'movie_discussion'] + '\n'
            movie_msg += '*****************************************\n'
            print(movie_msg)
            y.AppendText(movie_msg)
        if num >= int(b[5]) * 25:
            self.endtime = datetime.datetime.now()  # 结束时间
            conn1.sendall((str((self.endtime - self.starttime).seconds) ).encode())


    def startSpiderInfo(self,a,x):  # 此处是被服务器端启动的爬虫线程
        global NUM
        NUM=0
        self.q = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.q.bind(('localhost', 12306))
        self.q.listen(5)
        conn, addr = self.q.accept()
        self.starttime = datetime.datetime.now()  # 起始时间
        urls = self.getHotMovieUrlList(a[5])  # 首先爬取电影列表【第一层】
        print(urls)  # 返回要爬取详细信息的电影URL列表，是以字典形式存储
        for i in range(int(a[0])):  # a[0]是线程数
            time.sleep(1)
            leng = len(urls)
            music_urls = urls[i * leng // int(a[0]):(i + 1) * leng // int(a[0])]  # 切片操作，为每个线程平均分配要爬的电影url
            # 创建并启动线程，调用获取电影详细信息【第二层】
            threading.Thread(target=self.getMovieDetailInfo_list, args=(music_urls,a,x,conn,)).start()



    def saveDatabase(self, movie_info, conn):
        lock.acquire()
        cur = conn.cursor()
        try:
            sql_judge = 'select movie_name from movies where movie_name="%s"' % (movie_info['movie_name'])
            cur.execute(sql_judge)
            conn.commit()
            judge_name = cur.fetchone()
            if judge_name == None:
                sql = 'insert into movies values(null ,"%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")' % (
                    movie_info['movie_year'], movie_info['movie_name'], movie_info['movie_director'],
                    movie_info['movie_writer'], movie_info['movie_actor'], movie_info['movie_type'],
                    movie_info['movie_country'], movie_info['movie_language'], movie_info['movie_anotherName'],
                    movie_info['movie_date'], movie_info['movie_time'], movie_info['movie_IMDB'],
                    movie_info['movie_grade'],
                    movie_info['movie_commentsNum'], movie_info['movie_pageUrl'], movie_info['movie_comment'],
                    movie_info['movie_discussion'])
                cur.execute(sql)
                conn.commit()
                print("保存成功！！！")
        except:
            try:
                sql_judge = 'select movie_name from movies where movie_name="%s"' % (movie_info['movie_name'])
                cur.execute(sql_judge)
                conn.commit()
                judge_name = cur.fetchone()
                if judge_name == None:
                    sql = 'insert into movies values(null ,"%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")' % (
                        movie_info['movie_year'], movie_info['movie_name'], movie_info['movie_director'],
                        movie_info['movie_writer'], movie_info['movie_actor'], movie_info['movie_type'],
                        movie_info['movie_country'], movie_info['movie_language'], movie_info['movie_anotherName'],
                        movie_info['movie_date'], movie_info['movie_time'], movie_info['movie_IMDB'],
                        movie_info['movie_grade'],
                        movie_info['movie_commentsNum'], movie_info['movie_pageUrl'], "评论存在emoji或未知编码字符",
                        movie_info['movie_discussion'])
                    cur.execute(sql)
                    conn.commit()
                    print("保存成功！！！")
            except:
                print("保存失败！！！")
        lock.release()
        cur.close()
        return movie_info


if __name__ == '__main__':
    Spider().startSpiderInfo()