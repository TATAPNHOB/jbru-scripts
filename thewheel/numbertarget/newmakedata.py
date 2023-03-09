import json
import os
import copy

fold = 'TheWheelNumberTarget'
mus_ext = '.ogg'
txt_ext = '.jet'
prompts = os.listdir(fold)

with open(fold + 'Tech' + txt_ext,encoding='utf-8') as f:
    content = json.load(f)["content"]
##fields
fields_sample = {
    "HasIntroAudio":{
        "t":"B",
        "v":"false",
        "n":"HasIntroAudio"
        },
    "IntroAudio":{
        "t":"A",
        "v":"intro",
        "n":"IntroAudio"
        },
    "HasPromptAudio":{
        "t":"B",
        "v":"false",
        "n":"HasPromptAudio"
        },
    "PromptAudio":{
        "t":"A",
        "v":"prompt",
        "n":"PromptAudio"
        },
    "HasOutroAudio":{
        "t":"B",
        "v":"false",
        "n":"HasOutroAudio"
        },
    "OutroAudio":{
        "t":"A",
        "v":"outro",
        "n":"OutroAudio"
        },
    "HasFollowupAudio":{
        "t":"B",
        "v":"false",
        "n":"HasFollowupAudio"
        },
    "FollowupAudio":{
        "t":"A",
        "v":"followup",
        "n":"FollowupAudio"
        }
    }
types = ["intro","prompt","outro","followup"]

## NEXT PART SHOULD NOT BE MODIFIED

for prompt in prompts:
    files = os.listdir(fold + '/' + prompt)
    c = {}
    for cont in content:
        if cont["id"] == prompt:
            c = cont
            break
    fields = copy.deepcopy(fields_sample)
    for file in files:
        file = file.replace(mus_ext,'')
        if file not in types:
            if file == 'data.jet':
                os.remove(fold + '/' + prompt + '/' + file)
            else:
                print(file)
                print(prompt)
                raise Exception
        else:
            fields["Has" + file.capitalize() + "Audio"]["v"] = "true"
            fields[file.capitalize() + "Audio"]["s"] = c[file]
    fields = list(fields.values())
    n = open(fold + '/' + prompt + '/data' + txt_ext,'w',encoding='utf-8')
    n.write(json.dumps({"fields":fields},ensure_ascii=False,indent=2))
    n.close()
