import csv
import json

csvfile = open('뉴스결과.csv2019,10,1','r')

jsonfile = open(file='eif.json',mode='w',encoding="utf-8")
print(csvfile)
fieldNames = ('source','title','article_body','collect_time','link','good','nice','sad','angry','wanted','recommand','press')
reader = csv.DictReader(csvfile, fieldnames=fieldNames)
data = list(reader)
json.dump(data,jsonfile,ensure_ascii = False,indent=4)