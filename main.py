from plistlib import load
from Tools import loader
from Tools import api
import requests
import json

print("head title\n") 
loaded_data = json.loads(api.Requests('databases',' '))
print(api.Requests('databases',' '))