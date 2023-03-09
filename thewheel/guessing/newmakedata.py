import json
import os
import copy
import re

fold = 'TheWheelGuessing'
mus_ext = '.ogg'
txt_ext = '.jet'
prompts = os.listdir(fold)

with open(fold + txt_ext,encoding='utf-8') as f:
    content = json.load(f)["content"]

with open(fold + 'Tech' + txt_ext,encoding='utf-8') as f:
    content_tech = json.load(f)["content"]
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
    "HasRevealAudio":{
        "t":"B",
        "v":"false",
        "n":"HasRevealAudio"
        },
    "RevealAudio":{
        "t":"A",
        "v":"reveal",
        "n":"RevealAudio"
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
clue_sample = {
    "HasClueAudio":{
        "t":"B",
        "v":"false",
        "n":"HasClueAudio"
        },
    "ClueAudio":{
        "t":"A",
        "v":"clues_X_clue",
        "n":"ClueAudio"
        },
    "HasClueCommentAudio":{
        "t":"B",
        "v":"false",
        "n":"HasClueAudio"
        },
    "ClueCommentAudio":{
        "t":"A",
        "v":"clues_X_clueComment",
        "n":"ClueAudio"
        }
    }
types = ["intro","prompt","outro","followup","reveal"]

## NEXT PART SHOULD NOT BE MODIFIED (jk lol)

for prompt in prompts:
    files = os.listdir(fold + '/' + prompt)
    c = {}
    for cont in content:
        if cont["id"] == prompt:
            c = cont
            break
    c_tech = {}
    for cont_tech in content_tech:
        if cont_tech["id"] == prompt:
            c_tech = cont_tech
            break
    answers = c["clues"]
    fields = copy.deepcopy(fields_sample)
    for file in files:
        file = file.replace(mus_ext,'')
        if file not in types:
            if file == 'data.jet':
                os.remove(fold + '/' + prompt + '/' + file)
            elif (re.match(r'clues_\d_clue',file) != None or re.match(r'clues_\d\d_clue',file) != None):
                ## в массив ответов перенесем хинт. его нужно будет отразить в дате
                a = 1
            else:
                print(file)
                print(prompt)
                raise Exception
        else:
            fields["Has" + file.capitalize() + "Audio"]["v"] = "true"
            try:
                fields[file.capitalize() + "Audio"]["s"] = c[file]
            except KeyError:
                try:
                    fields[file.capitalize() + "Audio"]["s"] = c_tech[file]
                except KeyError:
                    raise Exception ##holy shit if that raises i don't know what to do anymore
    i = 0
    print(prompt,answers)
    for answer in answers:
        clue = copy.deepcopy(clue_sample)
        clue["HasClueAudio"]["n"] += str(i)
        clue["HasClueAudio"]["v"] = "true"
        clue["ClueAudio"]["n"] += str(i)
        clue["ClueAudio"]["v"] = "clues_" + str(i) + "_clue"
        clue["ClueAudio"]["s"] = answer["clue"]
        clue["HasClueCommentAudio"]["n"] += str(i)
        clue["ClueCommentAudio"]["v"] = "clues_" + str(i) + "_cluesComment"
        if ("clueComment" in answer.keys()):
            clue["HasClueCommentAudio"]["v"] = "true"
            clue["ClueCommentAudio"]["s"] = answer["clueComment"]
            clue["ClueAudio"]["s"] = answer["clueComment"]
        clue["HasClueAudio" + str(i)] = clue["HasClueAudio"]
        clue["ClueAudio" + str(i)] = clue["ClueAudio"]
        clue["HasClueCommentAudio" + str(i)] = clue["HasClueCommentAudio"]
        clue["ClueCommentAudio" + str(i)] = clue["ClueCommentAudio"]
        clue.pop("HasClueAudio")
        clue.pop("ClueAudio")
        clue.pop("HasClueCommentAudio")
        clue.pop("ClueCommentAudio")
        fields.update(clue)
        i += 1
    fields = list(fields.values())
    n = open(fold + '/' + prompt + '/data' + txt_ext,'w',encoding='utf-8')
    n.write(json.dumps({"fields":fields},ensure_ascii=False,indent=2))
    n.close()
