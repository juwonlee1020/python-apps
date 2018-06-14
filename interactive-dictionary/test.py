import json
data = json.load(open("data.json"))
for d in data.keys():
    if not (d[0].islower()):
        print(d)