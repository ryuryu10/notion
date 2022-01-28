from Tools import loader
import requests
import json

token = 'secret_U72PU588nbSbJtLJXKPQQpF6RHsUk8tvEXpjpLwe6w4'

databaseId = 'dcdab6b0d0f9475587c617589169b4b4'

headers = {"Authorization" : "Bearer " + loader.load_config('token'),
           "Notion-Version" : "2021-05-13"
           }


def readDatabase(databaseId, headers):
    readUrl = f"https://api.notion.com/v1/databases/{loader.load_config('database')}"

    res = requests.request("GET", readUrl, headers=headers)
    print(res.status_code)
    print(res.text)


readDatabase(databaseId, headers)