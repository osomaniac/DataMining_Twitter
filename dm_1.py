import keys
import tweepy as t

## passes authentication to twitter
auth = t.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

## these settings tell us if we are going over twitter's limit
api = t.API(auth,wait_on_rate_limit = True, wait_on_rate_limit_notify = True)


user = api.get_user('prattprattpratt')
'''
print(user.name)
print(user.description)
print(user.status.text)
print(user.followers_count)
print(user.geo_enabled)

print(user) ## gives a TON of info
me = api.me
print(me.name)
'''


followers = []
## cursor invokes a specified method to make sure you aren't surpassing twitter's rate limits
cursor = t.Cursor(api.followers, screen_name= 'prattprattpratt')
'''
for account in cursor.items(10):
    followers.append(account.screen_name)
print(followers)

friends = []
cursor = t.Cursor(api.friends, screen_name= 'prattprattpratt')
for friend in cursor.items(10):
    friends.append(friend.screen_name)
print(friends)

'''
## Get a user's recent tweets using user_timeline
christ_tweets = api.user_timeline(screen_name = 'prattprattpratt', count = 5) 

'''
for tweet in christ_tweets:
    print(f'{tweet.user.screen_name}: {tweet.text}\n') 
'''

mytweets = api.home_timeline()

for tweet in mytweets:
    print(f'{tweet.user.screen_name}: {tweet.text}\n') 


