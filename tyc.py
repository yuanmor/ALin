import json

with open("天眼查.txt",'r',encoding="utf-8") as f:
    lines = f.readline()

CName_List = []
lines = json.loads(lines)
for i in lines:
    CName_List.append(i['name'])
for CName in CName_List:
    print(CName)
