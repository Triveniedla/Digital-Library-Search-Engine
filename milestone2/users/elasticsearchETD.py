from elasticsearch import Elasticsearch
import pprint
import requests


class elasticsearchETD:
    def __init__(self):

        try:
            res = requests.get('http://localhost:9200')
            es = Elasticsearch(HOST="http://localhost", PORT=9200)
            self.es = Elasticsearch()
            self.connection="Successful"
        except:
            self.connection="Notsuccessful"

    def singlequery(self,whattosearch):

        body = {
        "from":0,
        "size":5000,
        "query": {
                 "match":{
                 "title": whattosearch["searchtext"]}
                 }}

        res = self.es.search(index="etdsearch", body=body)


        totalquerycount = len(res["hits"]["hits"])
        if totalquerycount==0:
            msg = 0
            output = ["None found"]
        else:
            msg = 1
            output = []
            for arg in res["hits"]["hits"]:
                output.append(arg['_source'])

        return output,msg


def elasticsearchfun(whattosearch):
    esobject = elasticsearchETD()

    if esobject.connection=="Notsuccessful":

        msg = 0
        output = ["cannot reach ElasticSearch on http://localhost:9200"]

    else:
        msg = 1
        output,msg = esobject.singlequery(whattosearch)

    return output,msg
