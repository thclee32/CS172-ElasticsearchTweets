# To run (EASY): 
Start Elasticsearch. (Whatever version you have)

Navigate to this directory (the one this README is in)

Run:
```
./elasticindex.sh
```
This scripts loads all 35087 tweets into Elasticsearch.

NOTE: This script does not terminate correctly when the index already exists.

## TWO WAYS TO GET RESULTS:
#### In your browser:
Open index.html. Make sure you have this Chrome extension installed and turned on: 

https://chrome.google.com/webstore/detail/moesif-orign-cors-changer/digfbfaphojjndkpccljibejjbppifbc?hl=en-US

If still nothing comes up, press F12 (at least on Chrome) to open the JavaScript terminal and see what kind of errors you're getting. If you're getting some sort of Cross-Origin Resource Sharing (CORS) error, maybe try a different extension. I had to try two before I got it to work. 

But hopefully once you have one of the CORS extensions installed, index.html should work. 
I've commented index.html extensively, so hopefully you guys can follow what I did. If you have questions just text me.


#### In the terminal:
```
./elasticquery.sh
```
This script will prompt you for a query term, and search for it in the tweet text.

It returns all information of all tweets that match your query, and highlights (snippet) the relevant text at the bottom of each tweet.


# To run (MANUALLY):
If you want to manually run the commands, instead of using the scripts:

To use:
Navigate to the elasticsearch folder. Run this command: 
```
./elasticsearch-5.1.1/bin/elasticsearch 
```

(or whatever version of elasticsearch you're using) to start Elasticsearch.

To verify that Elasticsearch is running, open another terminal and use:
```
curl.exe -XGET http://localhost:9200
```
(Elasticsearch uses localhost:9200 by default) 

If it is running, navigate to the Elasticsearch folder once more in the second terminal, and run:
```
curl.exe -XPOST 'http://localhost:9200/_bulk' --data-binary '@<filename>'
```
Replace <filename>.
The file has to be a modified version of the tweets json, which creates an index called "tweetindex", with objects "tweet".

It should echo the tweets that were added to the index.

Then a sample query looks like this:
```
curl.exe -XGET 'localhost:9200/tweetindex/tweet/1?pretty'
```
this returns the first tweet in the index.

```
curl.exe -XGET 'http://localhost:9200/tweetindex/tweet/_search?q=Riverside&pretty'
```
this returns all tweets that contain the string "Riverside" in any of the fields.

NOTE: all these commands are for Windows Powershell. MacOS Terminal and unix terminals may use different commands. Ex. curl.exe would just be curl.

FOR REFERENCE: To delete index, use:
```
curl -X DELETE 'localhost:9200/tweetindex'
```