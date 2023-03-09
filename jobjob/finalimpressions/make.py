import json
with open("base.txt",'r',encoding='utf-8') as f:
    lines = f.readlines()
content = []
for line in lines:
    line = line.replace('\n','')
    s = line.split(chr(9))
    t = {"firstPrompt":s[2],"id":s[0],"isValid":"","secondPrompt":s[4],"x":False}
    content += [t]
w = open('ApplyYourselfFinalImpression.jet','w',encoding='utf-8')
w.write(json.dumps({"content":content},ensure_ascii=False,indent=1))
w.close()
