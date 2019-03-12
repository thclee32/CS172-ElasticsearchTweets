import json

file = open('data.txt', 'r')

tweets = []
for line in file:
    tweets.append(json.loads(line))

json.dump('data1.json', tweets)