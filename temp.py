import requests

url = "https://api.notion.com/v1/databases/dcdab6b0d0f9475587c617589169b4b4/query"

payload = {"page_size": 100}
headers = {
    "Accept": "application/json",
    "Notion-Version": "2021-08-16",
    "Content-Type": "application/json",
    "Authorization": "Bearer secret_U72PU588nbSbJtLJXKPQQpF6RHsUk8tvEXpjpLwe6w4"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)