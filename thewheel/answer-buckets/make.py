import json
first = True
unfin = False
answers = []
payload = []
answermode = False
t_o = {"keywords":[],"sequential":[],"answers":[]}
with open('base.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
for line in lines:
    line = line.replace('\n','')
    s = line.split(chr(9))
    if s[0] == 'keywords':
        answermode = False
        if first:
            first = False
        else:
            if not (answers == []):
                t["answers"] = answers
                payload += [t]
        t = t_o.copy()
        answers = []
        if s[2] != '---':
            t["keywords"] = s[2].split('|')
    elif s[0] == 'sequential':
        if s[2] != '---':
            t["sequential"] = s[2].split('|')
    elif s[0] == 'answers' or answermode:
        answermode = True
        if s[2] != '' and s[2] != '<отсутствует>':
            answers += [s[2]]
if not (answers == []):
        
    t["answers"] = answers
    payload += [t]
n = open('answerbuckets.json','w',encoding='utf-8')
n.write(json.dumps({"payload":payload},ensure_ascii=False,indent=1))
n.close()
