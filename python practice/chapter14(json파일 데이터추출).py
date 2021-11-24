import json
s = set()
with open('cctv.json','r')as file:
    reader = file.read()
    dic_list = json.loads(reader)

    for i in range(len(dic_list)):
        a = dic_list[i].get('설치목적구분')
        s.add(a)
    print(s)

