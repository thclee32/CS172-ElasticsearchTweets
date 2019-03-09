import json

file = open('data.txt')
data = json.loads(file.read())

for x in data:

    print(x["id"])
