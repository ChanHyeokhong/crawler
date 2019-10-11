import json
from elasticsearch import Elasticsearch,helpers
import csv
es = Elasticsearch()


def el(x):
    with open(x, "r", encoding="UTF8") as f:
        reader = csv.DictReader(f)
        helpers.bulk(es, reader, index="npr", doc_type="np_data")

"""
es.indices.create(
    index='npr',
    body={
        "settings": {
            "index": {
                "analysis": {
                    "analyzer": {
                        "my_analyzer": {
                            "type": "custom",
                            "tokenizer": "nori_tokenizer"
                        }
                    }
                }
            }
        }
    }
)
with open("efefe.json", encoding='utf-8') as json_file:
    json_data = json.loads(json_file.read())


body = ""
for i in json_data:
    body = body + json.dumps({"index": {"_index": "npr", "_type": "np_data"}}) + '\n'
    body = body + json.dumps(i, ensure_ascii=False) + '\n'

helpers.bulk(body)

with open("eif.json", encoding='utf-8') as json_file:
    json_data = json.loads(json_file.read())


body = ""
for i in json_data:
    print(i)z
    es.index(index='npr',doc_type='npdata',body=i)
    #body = body + json.dumps({"index": {"_index": "npr", "_type": "npdata"}}) + '\n'
    #body = body + json.dumps(i, ensure_ascii=False) + '\n'
#es.bulk(body)

#es.indices.delete(index="dictionary", ignore=[400, 404])
"""