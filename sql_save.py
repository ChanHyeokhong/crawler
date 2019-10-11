#-*- coding: utf-8 -*-
import pymysql

def save(sources,title,article_body,collect_time,link,good,nice,sad,angry,wanted,recommand,press_1):
    conn = pymysql.connect(host='127.0.0.1',
                           port=3306,user='root',
                           password='cksgur123',
                           db='news',
                           charset='utf8')
    curs =conn.cursor()
    sql = 'insert into news.news_check (출처,제목,본문,수집날짜,link,좋아요,훈훈해요,슬퍼요,화나요,원해요,추천해요,신문국)' \
          ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

    curs.execute(sql, (sources,title,article_body,collect_time,link,good,nice,sad,angry,wanted,recommand,press_1))
    conn.commit()
    conn.close()
#gb..