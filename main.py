from Tools import notion

Column_Name = []
Row_Data = []

print("head title\n") 
data = notion.Requests("query")
for a in data['results'][0]['properties']:
    Column_Name.append(a)
for a in data['results']:
    Row_Data.append(a)
for a in Row_Data:
    for b in Column_Name:
        if a['properties'][b]['type'] == "rich_text":
            print('{0} : {1}'.format(b, a['properties'][b]['rich_text'][0]['plain_text']))
        elif a['properties'][b]['type'] == "select":
            print('{0} : {1}'.format(b, a['properties'][b]['select']['name']))
        elif a['properties'][b]['type'] == "checkbox":
            print('{0} : {1}'.format(b, a['properties'][b]['checkbox']))
        elif a['properties'][b]['type'] == "number":
            print('{0} : {1}'.format(b, a['properties'][b]['multi_select'][0]['name']))
        elif a['properties'][b]['type'] == "text":
            print('{0} : {1}'.format(b, a['properties'][b]['text']['content']))
        
        else:
            print('{0} : 텍스트를 지원하지 않음.'.format(b))
    print("--------------")
