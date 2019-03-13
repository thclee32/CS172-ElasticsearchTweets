#!/bin/bash   

while true
do
    echo Enter a term to search for, or press [CTRL + C] to stop:

    read queryterm

    curl -XGET "localhost:9200/tweetindex/tweet/_search?q=text:$queryterm&pretty"
    echo " "
done