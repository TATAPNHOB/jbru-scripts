import json
with open("base.txt",'r',encoding='utf-8') as f:
    lines = f.readlines()
content = []
for line in lines:
    line = line.replace('\n','')
    s = line.split(chr(9))
    if (s[6].find("1") != -1):
        x = True
    else:
        x = False
    if (s[3].find("three") != -1):
        r3h = s[5]
    else:
        r3h = None
    t = {"id":s[0],"isValid":"","question":s[2],"round":s[3],"round3Header":r3h,"x":x}
    content += [t]
w = open('ApplyYourselfInterviewQuestion.jet','w',encoding='utf-8')
w.write(json.dumps({"content":content},ensure_ascii=False,indent=1))
w.close()

