import tweepy

client = tweepy.Client(
    bearer_token="NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN"
)

response = client.search_recent_tweets(
    query="ال lang:ar",
    max_results=10
)

for tweet in response.data:
    print(tweet.text)
