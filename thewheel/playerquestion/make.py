import json
with open('base.txt',encoding='utf-8') as f:
    lines = f.readlines()
content = []
for line in lines:
    content += [{"text":line.replace('\n','').split(chr(9))[1]}]
n = open('TheWheelPlayerQuestion.jet','w',encoding='utf-8')
n.write(json.dumps({"content":content},ensure_ascii=False,indent=2))
n.close()
