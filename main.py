#-*- coding: utf-8 -*-
from press import press
from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime
import re
from Parser import parse
from sql_save import save
from to_csv import panda
from face import face
base_url="https://news.naver.com"

def collecting():
    data = urlopen(base_url).read()
    soup = BeautifulSoup(data, "html.parser")
    dd = datetime.today()
    collect_time=str(dd.year)+","+str(dd.month)+","+str(dd.day)
    patter='[^\w\s]'
    co = []
    ll=[]
    for i in soup.find_all('div',{'class':'hdline_flick_item'}):#헤드라인 사진포함된 것 추출
        a = i.find('a')
        ll.append(base_url+a.get('href'))

    for i in soup.find_all('dd'):#대표기사들 추출
        b = i.find('a')
        ll.append(b.get('href'))

    for k in soup.find_all('div', 'hdline_article_tit'):#헤드라인 추출
        c=k.find('a')
        ll.append(base_url+c.get('href'))

    for data in soup.find_all('div','mtype_list_wide'):#나머지 기사 추출
        try:
            for a in data.find_all('a'):
                link=a.get('href')  # for getting link
                ll.append(link)

        except OSError:
            break

    for i in soup.find_all('ul',{'class':'section_list_ranking'}):#가장많이본 뉴스 추출
        for j in i.find_all('a'):
            link=j.get('href')
            ll.append(base_url+link)

    for i in ll:
        cs=[]
        article_body, title = parse(i)
        press_1 = press(i)
        good, nice, sad, angry, wanted, recommand = face(i)
        dic={
            'title':title,
            'press':press_1,
            'good':good,
            'nice':nice,
            'sad':sad,
            'angry':angry,
            'wanted':wanted,
            'recommand':recommand
        }
        cs.append('naver_news')
        cs.append(title)
        cs.append(article_body)
        cs.append(collect_time)
        cs.append(i)
        cs.append(good)
        cs.append(nice)
        cs.append(sad)
        cs.append(angry)
        cs.append(wanted)
        cs.append(recommand)
        cs.append(press_1)
        
        try:
            save('naver_news', title, article_body, collect_time, i, good, nice, sad, angry, wanted, recommand, press_1)
        except:#헤드라인 뉴스와 분야별 순위에 같이 포함되면 기본키 중복으로 삽입 거절당하기 때문에 그것을 방지하기 위한 예외처리
            pass

        co.append(cs)
    panda(co)
