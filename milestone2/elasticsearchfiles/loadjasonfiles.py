import requests, json, os
from elasticsearch import Elasticsearch
import pprint

if __name__ == '__main__':

    directory='D:/courses/Fall2020/cs518-WebProgramming/dissertation/'
    res = requests.get('http://localhost:9200')
    # pprint.pprint(res.content)
    es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])

    i=1
    failed=0
    for foldname in os.listdir(directory):
        for filename in os.listdir(directory+foldname):
            if filename.endswith(".json"):


                try:
                    docket_content = json.load(open(directory+foldname+"/"+filename))
                    es.index(index="etdsearch", doc_type="documents", id=i, body=docket_content)
                    i = i + 1
                except Exception:
                    print("Error reading file:",filename)
                    failed=failed+1

    print("Successfully loaded jason files:",i)
    print("Failed jason files:",failed)
