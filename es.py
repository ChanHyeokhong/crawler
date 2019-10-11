#-*- coding: utf-8 -*-
from elasticsearch import helpers
import csv
import requests, json, os
from elasticsearch import Elasticsearch

es = Elasticsearch("localhost:9200")
j=0


"""
with open('eif.json','r',encoding='utf-8') as json_file:
    json_data = json.load(json_file)
    for doc in json_data:
        es.indices.delete(index='newses', ignore=[400, 404])
"""
"""
with open('eif.json','r',encoding='utf-8') as json_file:
    json_data = json.load(json_file)
    for doc in json_data:
        print(doc)
        action={
            'article_body' : doc['article_body'],
            'good': doc['good'],
            'sad': doc['sad'],
            'angry':doc['angry'],
            'wanted':doc['wanted'],
            'recommand':doc['recommand'],
            'press':doc['press']
        }
        j+=1
        es.index(index=doc['title'], doc_type=doc['link'], id=j,body=action)



a=input()
res=es.search(body={'query':{'match':{'article_body':a}}})
for r in res['hits']['hits']:
    print(r['_score'],r['_source'])
"""