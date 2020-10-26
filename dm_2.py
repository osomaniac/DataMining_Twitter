import keys
import json
import tweepy as t
from wordcloud import WordCloud

## passes authentication to twitter
auth = t.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

## these settings tell us if we are going over twitter's limit
api = t.API(auth,wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

'''
tweets = api.search(q="vote", count=1)
for tweet in tweets:
    print(tweet.user.screen_name, ":", tweet.text)

print()

tweets = api.search(q="#collegefootball", count=2)
for tweet in tweets:
    print(tweet.user.screen_name, ":", tweet.text)
'''

'''
#Places with trending topics
trends_available = api.trends_available()
print(len(trends_available))
print(trends_available[:3]) ## woeid = where on earth id, 1 = worldwide
'''
'''
wolrd_trends = api.trends_place(id=1)
#print(wolrd_trends)

outfile = open('world_trends.json', 'w')
json.dump(wolrd_trends, outfile, indent=5)

trends = wolrd_trends[0]['trends'] #null value for tweet_volume means the trend did not get over 10k tweets
#print(trends)

# only keep those trends with tweet_volumber over 10k
trends = [t for t in trends if t['tweet_volume']]
#print(trends)

# sort by tweet_volume
from operator import itemgetter
trends.sort(key=itemgetter("tweet_volume"), reverse=True)

# print the name for the top 5 topics
for t in trends[:5]:
    print(t['name'])

'''

# Find trending topics for New Yok and create wordcloud for it
new_york_trends = api.trends_place(id=2459115)
ny_trends = new_york_trends[0]['trends']
ny_trends = [t for t in ny_trends if t['tweet_volume']]
from operator import itemgetter
ny_trends.sort(key=itemgetter("tweet_volume"), reverse=True)

ny_dict = {}
for t in ny_trends:
    ny_dict[t['name']] = t['tweet_volume'] 

wc = WordCloud(colormap='prism',width=1600, height=900, prefer_horizontal=0.5, min_font_size=10,background_color='white')
wc = wc.generate_from_frequencies(ny_dict) ## or you can use -> wc = wc.fit_words(ny_dict)
wc = wc.to_file('NYCTwitterTrends.png')
