import json

inputfile = open('twitter_all.txt', 'r')
outputfile = open('elasticreadytweets.txt', 'w')


count = 1

#cnt = str(count)
#outputfile.write('''{"index":{"_index":"tweetindex", "_type":"tweet", "_id": "''' + cnt + '''"}}''')


for line in inputfile:
    cnt = str(count)
    if line != "\n":
        outputfile.write('''{"index":{"_index":"tweetindex", "_type":"tweet", "_id": "''' + cnt + '''"}}\n''')
        outputfile.write(line)
        count += 1
    

inputfile.close()
outputfile.close()