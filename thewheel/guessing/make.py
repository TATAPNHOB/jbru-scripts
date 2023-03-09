import json
alts = []
clues = []
first = True
cluemode = False
t_o = {"altSpellings":[],"answer":"","category":"","clues":[],"followup":"","id":"","isValid":"","prompt":"","reveal":"","us":False,"x":False}
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
            if (s[8] == '1'):
                t["x"] = True
            first = False
        else:
            t["altSpellings"] = alts
            t["clues"] = clues
            content += [t]
            t = t_o.copy()
            t["id"] = s[1]
            if (s[8] == '1'):
                t["x"] = True
            clues = []
            cluemode = False
    elif cluemode or s[0] == 'clues':
        cluemode = True
        if s[2] != '' and s[2] != '<отсутствует>':
            q = {"clue":s[2]}
            if s[4] != '' and s[4] != '<отсутствует>':
                q["clueComment"] = s[4]
            clues += [q]
    elif s[0] == 'category' and s[2] != '<отсутствует>':
        t["category"] = s[2]
    elif s[0] == 'prompt' and s[2] != '<отсутствует>':
        t["prompt"] = s[2]
    elif s[0] == 'followup' and s[2] != '<отсутствует>':
        t["followup"] = s[2]
    elif s[0] == 'reveal' and s[2] != '<отсутствует>':
        t["reveal"] = s[2]
    elif s[0] == 'answer' and s[2] != '<отсутствует>':
        t["answer"] = s[2]
        alts = s[9].split('|')
        if alts[0] == "":
            alts = []
        t["altSpellings"] = alts
t["clues"] = clues
content += [t]
n = open('TheWheelGuessing.jet','w',encoding='utf-8')
n.write(json.dumps({"content":content},ensure_ascii=False,indent=2))
n.close()
