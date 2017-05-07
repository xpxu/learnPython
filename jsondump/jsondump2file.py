import json
with open("test.json") as infile:
    j = json.load(infile)

j["Account"]["Containers"].append({"name": "mnop", "created_at": "100000.12345"})

with open("test.json", "w") as outfile:
    json.dump(j, outfile, indent=4, separators=(',', ': '))
