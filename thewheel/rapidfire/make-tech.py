import json
answers = []
first = True
answermode = False
t_o = {"id":"","prompt":"","intro":None,"outro":None,"followup":None}
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
        else:
            answermode = False
            content += [t]
            answers = []
            t = t_o.copy()
            t["id"] = s[1]
    elif answermode or s[0] == 'answers':
        answermode = True
        if s[2] != "" and s[2] != '<отсутствует>':
            answer = {"text":s[2],"value":s[4]}
        answers += [answer]
    elif s[0] == 'followup':
        t["followup"] = s[2]
    elif s[0] == 'prompt':
        t["prompt"] = s[2]
    elif s[0] == 'intro':
        t["intro"] = s[2]
    elif s[0] == 'outro':
        t["outro"] = s[2]
content += [t]
n = open('TheWheelRapidFireTech.jet','w',encoding='utf-8')
n.write(json.dumps({"content":content},ensure_ascii=False,indent=1))
n.close()
