import json
answers = []
first = True
answermode = False
t_o = {"id":"","prompt":"","intro":None,"followup":None,"outro":None}
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
            content += [t]
            t = t_o.copy()
            t["id"] = s[1]
    elif s[0] == 'prompt':
        t["prompt"] = s[2]
    elif s[0] == 'intro':
        t["intro"] = s[2]
    elif s[0] == 'outro':
        t["outro"] = s[2]
    elif s[0] == 'followup':
        t["followup"] = s[2]
content += [t]
n = open('TheWheelTypingListTech.jet','w',encoding='utf-8')
n.write(json.dumps({"content":content},ensure_ascii=False,indent=1))
n.close()
