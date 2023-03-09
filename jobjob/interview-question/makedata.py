import json
import os
os.mkdir("ApplyYourselfInterviewQuestion")
with open('ApplyYourselfInterviewQuestion.jet','r',encoding='utf-8') as f:
    content = json.load(f)
content = content["content"]
for item in content:
    os.mkdir("ApplyYourselfInterviewQuestion/" + item["id"])
    with open('en/ApplyYourselfInterviewQuestion/' + item["id"] + '/data.jet','r',encoding='utf-8') as f:
        data = json.load(f)
    fields = data["fields"]
    question = item["question"]
    if (item["round"] == "three"):
        fields[4]["s"] = item["round3Header"]
        fields[5]["v"] = item["round3Header"]
        

    
    fields[1]["s"] = question
    fields[2]["v"] = question

    m = open("ApplyYourselfInterviewQuestion/" + item["id"] + "/data.jet","w",encoding="utf-8")
    m.write(json.dumps({"fields":fields},ensure_ascii=False,indent=1))
    m.close()
