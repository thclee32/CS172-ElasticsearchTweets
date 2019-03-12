To use:
Navigate to the elasticsearch folder. Run this command: 
'''
./elasticsearch-5.1.1/bin/elasticsearch 
'''

(or whatever version of elasticsearch you're using) to start Elasticsearch.

To verify that Elasticsearch is running, open another terminal and use:
'''
curl.exe -XGET http://localhost:9200
'''
(Elasticsearch uses localhost:9200 by default) 

If it is running, navigate to the Elasticsearch folder once more in the second terminal, and run:
'''
curl.exe -XPOST 'http://localhost:9200/_bulk' --data-binary '@file.txt'
'''
File.txt is a modified version of the tweets json, which creates an index called "tweetindex", with objects "tweets".

It should echo the tweets that were added to the index.

Then a sample query looks like this:
'''
curl.exe -XGET 'localhost:9200/tweetindex/tweet/1?pretty'
'''
this returns the first tweet in the index.

'''
curl.exe -XGET 'http://localhost:9200/tweetindex/tweet/_search?q=Riverside'
'''
this returns all tweets that contain the string "Riverside" in any of the fields.