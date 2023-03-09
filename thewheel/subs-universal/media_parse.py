with open('media.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
audio = []
audionums = []
for line in lines:
    line = line.replace('\n','')
    data = line.split('|')
    for i in range(int(data[2])):
        audio += [data[3+i*4]]
        audionums += [data[5+i*4]]
with open('start.txt','r',encoding='utf-8') as f:
    startlines = f.read().split('^')
with open('base.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
for line in lines:
    line = line.replace('\n','')
    line = line.replace('\\"','')
    line = line.replace('"','\\"')
    line = line.replace("\\'",'')
    line = line.replace("'","\\'")
    s = line.split(chr(9))
    if (s[4] == '[Unsubtitled]'):
        s[2] += ' [Unsubtitled]'
    startlines[int(audionums[audio.index(s[0])])-1] = s[2]
text = ''
for startl in startlines:
    text += '^' + startl

n = open('parsedstart.txt','w',encoding='utf-8')
n.write(text)
n.close()
