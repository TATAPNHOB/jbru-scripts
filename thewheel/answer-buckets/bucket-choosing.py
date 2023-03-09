import json
import random
def getBucketForQuestion(question):
    question = question.replace("?","").lower()
    qwords = question.split(" ")
    qs = []
    for qword in qwords:
        if (qword != ""):
            qs += [qword]
    for bucket in buckets:
        for kws in bucket["keywords"]:
            kws = kws.lower()
            kwss = kws.split(" ")
            has_kws = questionHasKeywords(qs,kwss)
            try:
                k_i = qs.index(kws)
            except:
                k_i = -1
            if (has_kws):
                if (len(bucket["sequential"]) <= 0):
                    return bucket
                if (k_i < len(qs)-1):
                    next_w = qs[k_i + 1]
                    for seq in bucket["sequential"]:
                        if (next_w == seq):
                            return bucket
    return buckets[len(buckets)-1]

def questionHasKeywords(questionwords,keywordwords):
    try:
        first = questionwords.index(keywordwords[0])
    except:
        return False
    i1 = first + 1
    i2 = 1
    while (i2 < len(keywordwords)):
        if (i1 > len(questionwords)-1):
            return False
        if (keywordwords[i2] != questionwords[i1]):
            return False
        i1 += 1
        i2 += 1
    return True
with open('answerbuckets.json',encoding='utf-8') as f:
    buckets = json.load(f)["payload"]
query = input()
while (query != "STOP"):
    bucket = getBucketForQuestion(query)
    print(bucket["answers"][random.randint(0,len(bucket["answers"])-1)])
    if (bucket["keywords"] != []):
        print("Пул - " + bucket["keywords"][0],end=" ")
        if (bucket["sequential"] != []):
            print(bucket["sequential"][0])
        else:
            print()
    else:
        print('Пул - общий')
    query = input()
