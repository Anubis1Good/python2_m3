import json
from pprint import pprint

with open('f.json','r',encoding='utf-8') as file:
    data = json.load(file)
    pprint(data)

with open('f2.json','w',encoding='utf-8') as file:
    json.dump({'Привет':'Мир'},file, ensure_ascii=False)

with open('f2.json','r',encoding="utf-8") as file:
    pprint(json.load(file))