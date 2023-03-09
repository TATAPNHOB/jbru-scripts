import json
import os
fold = "TheWheelNumberTarget"
os.mkdir(fold)
with open(fold + 'Tech.jet','r',encoding='utf-8') as f:
    content = json.load(f)
content = content["content"]
for item in content:
    os.mkdir(fold + "/" + item["id"])
    with open('en/' + fold + '/' + item["id"] + '/data.jet','r',encoding='utf-8') as f:
        data = json.load(f)
    fields = data["fields"]
    if (item["intro"] != None):
        if fields[0]["n"] != "HasIntroAudio":
            print('something is wrong')
        fields[0]["v"] = "true"
        fields[1]["s"] = item["intro"]
    if (item["followup"] != None):
        if fields[4]["n"] != "HasFollowupAudio":
            print('something is wrong')
        fields[4]["v"] = "true"
        fields[5]["s"] = item["followup"]
    if (item["outro"] != None):
        if fields[6]["n"] != "HasOutroAudio":
            print('something is wrong')
        fields[6]["v"] = "true"
        fields[7]["s"] = item["outro"]
    fields[3]["s"] = item["prompt"]
    m = open(fold + "/" + item["id"] + "/data.jet","w",encoding="utf-8")
    m.write(json.dumps({"fields":fields},ensure_ascii=False,indent=1))
    m.close()
