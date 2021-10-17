import requests, json, os
from elasticsearch import Elasticsearch
import pprint

if __name__ == '__main__':

    directory='../media/dissertation/jsonfiles/'
    res = requests.get('http://localhost:9200')
    pprint.pprint(res.content)
    es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])

    i=1
    failed=0
    for filename in os.listdir(directory):
        if filename.endswith(".json"):

            print(i,filename)
            try:
                docket_content = json.load(open(directory+"/"+filename))
                es.index(index="etdsearch", doc_type="documents", id=i, body=docket_content)
                i = i + 1
            except Exception:
                print("Error reading file:",filename)
                failed=failed+1

    print("Successfully loaded jason files:",i)
    print("Failed jason files:",failed)
