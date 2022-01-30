from urllib import request
from . import loader
import requests
import json

_SAVEDATA = True

headers = {
    "Authorization" : "Bearer " + loader.load_config('token'),
    "Accept": "application/json",
    "Notion-Version" : "2021-08-16"
    }
payload = {"page_size": 100}

def Requests(type):
    if type == "query":
        readUrl = f"https://api.notion.com/v1/databases/{loader.load_config('database')}/query"
        res = requests.request("POST", readUrl, json=payload, headers=headers)
    elif type == "database":
        readUrl = f"https://api.notion.com/v1/databases/{loader.load_config('database')}"
        res = requests.request("GET", readUrl, headers=headers)
    elif type == "pages":
        readUrl = f"https://api.notion.com/v1/pages/{loader.load_config('database')}"  
        res = requests.request("GET", readUrl, headers=headers)
    else:
        pass
    
    if _SAVEDATA == True:
        with open('./dump.json', 'w', encoding='utf8') as f:
            json.dump(res.json(), f, ensure_ascii=False)
    json_data = res.json()
    return json_data
