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
        Query = None
        types = None
        if a['properties'][b]['type'] == "rich_text":
            types = "rich_text"
            Query = a['properties'][b]['rich_text'][0]['plain_text']

        elif a['properties'][b]['type'] == "select":
            types = "select"
            if a['properties'][b]['select'] == None:
                Query = "선택된 데이터가 없음"
            else:
                Query = a['properties'][b]['select']['name']

        elif a['properties'][b]['type'] == "checkbox":
            types = "checkcbox"
            Query = a['properties'][b]['checkbox']

        elif a['properties'][b]['type'] == "multi_select":
            types = "multi_select"
            multi_select_data = []
            if len(a['properties'][b]['multi_select']) != 0:
                for c in a['properties'][b]['multi_select']:
                    multi_select_data.append(c['name'])
                Query = multi_select_data
            else:
                Query = "선택된 데이터가 없음"

        elif a['properties'][b]['type'] == "text":
            types = "text"
            Query = a['properties'][b]['text']['content']
        
        elif a['properties'][b]['type'] == "number":
            types = "number"
            Query = a['properties'][b]['number']
        
        elif a['properties'][b]['type'] == "title":
            types = "title"
            Query = a['properties'][b]['title'][0]['plain_text']
        else:
            print("지원하지 않는 형식 : {0}".format(a['properties'][b]['type']))
            #??
        print(f'{b} | {types} | {Query}')
    print("--------------")
