from traceback import print_tb
from Tools import loader, notion
import requests
import json

print("head title\n") 
data = notion.Requests("query")
print(data['results'][0]['properties'])