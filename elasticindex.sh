#!/bin/bash          

cd elasticreadytweets

for file in *
do 
    curl -XPOST 'http://localhost:9200/_bulk' --data-binary @"$file"
done

echo "Successfully bulk loaded all tweets in Elasticsearch."