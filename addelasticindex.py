import json

filecount = 0
count = 1
for filecount in range(11):
    filestring = str(filecount)
    inputfile = open('rawtweets/twitter_data' + filestring  + '.txt', 'r')
    outputfile = open('elasticreadytweets/elastictwitter_data' + filestring + '.txt', 'w')



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
    filecount += 1