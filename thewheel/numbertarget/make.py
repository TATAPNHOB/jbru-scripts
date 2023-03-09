import json
answers = []
first = True
answermode = False
t_o = {"category":"","id":"","isValid":"","prompt":"","unit":"","us":False,"x":False}
content = []
with open('base.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
for line in lines:
    line = line.replace('\n','')
    s = line.split(chr(9))
    if s[0] == 'id':
        if first:
            first = False
        else:
            content += [t]
        t = t_o.copy()
        t["id"] = s[1]
        if s[6] == '1':
            t["x"] = True
    elif s[0] == 'category':
        t["category"] = s[2]
    elif s[0] == 'prompt':
        t["prompt"] = s[2]
    elif s[0] == 'unit':
        t["unit"] = s[2]
    elif s[0] == 'value':
        t["value"] = s[2]
content += [t]
n = open('TheWheelNumberTarget.jet','w',encoding='utf-8')
n.write(json.dumps({"content":content},ensure_ascii=False,indent=1))
n.close()
