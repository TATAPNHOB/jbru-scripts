import json
with open("base.txt",'r',encoding='utf-8') as f:
    lines = f.readlines()
content = []
for line in lines:
    line = line.replace('\n','')
    s = line.split(chr(9))
##    if (s[3].find("1") != -1):
##        x = True
##    else:
##        x = False
##  x = False
    t = {"text":s[1]}
    content += [t]
w = open('TheWheelAnswer.jet','w',encoding='utf-8')
w.write(json.dumps({"content":content},ensure_ascii=False))
w.close()
