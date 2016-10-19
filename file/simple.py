import json

output = '{"age": 20, "score": 88, "name": "Bob"}'
with open('xp.log', 'a') as outfile:
    # json.dump(output, outfile)
    outfile.write(output + '\n\n')
