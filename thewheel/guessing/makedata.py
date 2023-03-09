import json
import os
import re
import shutil
fold = "TheWheelGuessing"
shutil.rmtree(fold)
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
    if (item["reveal"] != None or item["reveal"] !=""):
        if fields[6]["n"] != "HasRevealAudio":
            print('something is wrong')
        fields[6]["v"] = "true"
        fields[7]["s"] = item["reveal"]
    if (item["outro"] != None):
        if fields[len(fields)-2]["n"] != "HasOutroAudio":
            print('something is wrong')
        fields[len(fields)-2]["v"] = "true"
        fields[len(fields)-1]["s"] = item["outro"]
    fields[3]["s"] = item["prompt"]
    for field in fields:
        if re.match(r"clues_\d_clue",field["v"]) != None:
            q = int(field["v"][6])
            if (field["v"].find("Comment") != -1):
                if "clueComment" in item["clues"][q].keys():
                    field["s"] = item["clues"][q]["clueComment"]
            else:
                field["s"] = item["clues"][q]["clue"]
    m = open(fold + "/" + item["id"] + "/data.jet","w",encoding="utf-8")
    m.write(json.dumps({"fields":fields},ensure_ascii=False,indent=1))
    m.close()
