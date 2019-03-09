

inputfile = open('twitter_data3.txt', 'r')

outputfile = open('data1.txt', 'w')

'''
for line in inputfile:
    for word in line.split():
        if word == "\n":
            outputfile.write("\n" + ",")
        outputfile.write(word)
'''

outputfile.write("[" + "\n")

for line in inputfile:
    if line != "\n":
        outputfile.write(line + ", \n")
    #if line != "\n":
    #   outputfile.write(",")

outputfile.write("]")

inputfile.close()
outputfile.close()