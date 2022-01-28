import loader
import requests
import json

headers = {"Authorization" : "Bearer " + loader.load_config('token'),
           "Notion-Version" : "2021-05-13"
           }

def Requests(type):
    pass

def readDatabase(databaseId, headers):
    readUrl = f"https://api.notion.com/v1/databases/{loader.load_config('database')}"

    res = requests.request("GET", readUrl, headers=headers)
    print(res.status_code)
    print(res.text)


#readDatabase(loader.load_config('database'), headers)

url = "https://api.notion.com/v1/pages/cf8b4bec8cc1485fa125f4966872784e"
response = requests.request("GET", url, headers=headers)

print(response.text)