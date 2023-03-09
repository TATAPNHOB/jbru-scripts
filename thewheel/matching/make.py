import json
answers = []
first = True
answermode = False
t_o = {"answers":[],"category":"","decoys":[],"headers":[],"id":"","isValid":"","prompt":"","promptHeader":"","us":False,"x":False}
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
            answer = {"match":s[2],"text":s[4]}
        answers += [answer]
    elif s[0] == 'category':
        t["category"] = s[2]
    elif s[0] == 'prompt':
        t["prompt"] = s[2]
    elif s[0] == 'promptHeader':
        t["promptHeader"] = s[2]
    elif s[0] == 'headers':
        t["headers"] = [{"match":s[2],"text":s[4]}]
t["answers"] = answers
content += [t]
n = open('TheWheelMatching.jet','w',encoding='utf-8')
n.write(json.dumps({"content":content},ensure_ascii=False,indent=1))
n.close()
