from sqlite3 import Row
from traceback import print_tb
from typing import Collection
from Tools import loader, notion
import requests
import json

Column_Name = []
Row_Data = []

print("head title\n") 
data = notion.Requests("query")
for a in data['results'][0]['properties']:
    Column_Name.append(a)
'''for b in Column_Name:
    if data['results'][0]['properties'][b]['type'] == "rich_text":
        print(data['results'][0]['properties'][b]['rich_text'][0]['text']['content'])'''

for a in data['results']:
    Row_Data.append(a)