import json
answers = []
first = True
answermode = False
t_o = {"answers":[],"category":"","id":"","isValid":"","prompt":"","sort":"ascending","subtype":"","unit":"","us":False,"x":False}
content = []
with open('base.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
for line in lines:
    line = line.replace('\n','')
    s = line.split(chr(9))
    if s[0] == 'id':
        if first:
            t = t_o.copy()
            t["id"] = s[1]
            first = False
            if s[7] == '1':
                t["x"] = True
        else:
            answermode = False
            t["answers"] = answers
            content += [t]
            answers = []
            t = t_o.copy()
            t["id"] = s[1]
            if s[7] == '1':
                t["x"] = True
    elif answermode or s[0] == 'answers':
        answermode = True
        if s[2] != "" and s[2] != '<отсутствует>':
            answer = {"text":s[2],"value":s[4]}
        answers += [answer]
    elif s[0] == 'category':
        t["category"] = s[2]
    elif s[0] == 'prompt':
        t["prompt"] = s[2]
    elif s[0] == 'unit':
        t["unit"] = s[2]
    elif s[0] == 'sort':
        t["sort"] = s[1]
    elif s[0] == 'subtype':
        t["subtype"] = s[1]
t["answers"] = answers
content += [t]
n = open('TheWheelRapidFire.jet','w',encoding='utf-8')
n.write(json.dumps({"content":content},ensure_ascii=False,indent=1))
n.close()
