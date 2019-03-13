#!/bin/bash   

while true
do
    echo Enter a term to search for, or press [CTRL + C] to stop:

    read queryterm

    curl -XGET "localhost:9200/_search?pretty" -H 'Content-Type: application/json' -d'
    {
        "query" : {
            "match" : { "text" : "'"$queryterm"'"}
        },
        "highlight" : {
            "fields" : {
                "text" : {}
            }
        }
    }
    '
    echo " "
done