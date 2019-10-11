#-*- coding: utf-8 -*-
import pandas as pd
from datetime import datetime
from es_setting import el
time = datetime.today()
ntime=str(time.year)+","+str(time.month)+","+str(time.day)
def panda(moum):
    data = pd.DataFrame(moum)
    data.columns = ['source','title','article_body','collect_time','link','good','nice','sad','angry','wanted','recommand','press']
    data.head()
    re='뉴스결과'+ntime+".csv"
    data.to_csv(re, encoding='utf-8',index=False)
    el(re)
