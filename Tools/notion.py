from asyncore import read
from cgitb import reset
from . import loader
import requests
import json

headers = {
    "Authorization" : "Bearer " + loader.load_config('token'),
    "Accept": "application/json",
    "Notion-Version" : "2021-08-16"
    }

def Requests(type,id):
    if db_query:
        pass
    
    readUrl = f"https://api.notion.com/v1/databases/{loader.load_config('database')}/query"
    res = requests.request("GET", readUrl, headers=headers)
    return res.text

def readDatabase(databaseId, headers):
    readUrl = f"https://api.notion.com/v1/databases/{loader.load_config('database')}"

    res = requests.request("GET", readUrl, headers=headers)
    print(res.status_code)
    print(res.text)


#readDatabase(loader.load_config('database'), headers)
'''url = "https://api.notion.com/v1/pages/cf8b4bec8cc1485fa125f4966872784e"
response = requests.request("GET", url, headers=headers)

print(response.text)'''