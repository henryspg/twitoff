"""Retrieve Tweets, embeddings, and persist in the database."""
from os import getenv
import basilica
import tweepy
from .models import DB, Tweet, User
# from .models import *
# from .models import DB, User
from dotenv import load_dotenv


load_dotenv()


TWITTER_USERS = ['calebhicks', 'elonmusk', 'rrherr', 'SteveMartinToGo',
                 'alyankovic', 'nasa', 'sadserver', 'jkhowland', 'austen',
                 'common_squirrel', 'KenJennings', 'conanobrien',
                 'big_ben_clock', 'IAM_SHAKESPEARE', 'Jimmykimmel', 'BarackObama', 'StephenCurry30']

TWITTER_API_KEY = getenv('TWITTER_API_KEY')
TWITTER_API_KEY_SECRET = getenv('TWITTER_API_KEY_SECRET')
TWITTER_AUTH = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_KEY_SECRET)
TWITTER = tweepy.API(TWITTER_AUTH)
BASILICA = basilica.Connection(getenv('BASILICA_KEY'))


def add_or_update_user(username):
    """Add or update a user and their Tweets, error if not a Twitter user."""
    try:
        twitter_user = TWITTER.get_user(username)
        # how do I make a brand new user?  instantiate new user, and add to the DB
        # But 1st... see if the username already exists. if they dont exist, make a new user
        db_user = (User.query.get(twitter_user.id) or
                   User(id=twitter_user.id, name=username))
        DB.session.add(db_user)
        # Lets get the tweets - focusing on primary (not retweet/reply)
        tweets = twitter_user.timeline(
            count=200, exclude_replies=True, include_rts=False,
            tweet_mode='extended', since_id=db_user.newest_tweet_id
        )
        if tweets:
            db_user.newest_tweet_id = tweets[0].id
        print("about to loop through tweets and do stuff - twtr-py")
        for tweet in tweets:
            # print("the tweet is: ", tweet)
            embedding = BASILICA.embed_sentence(tweet.full_text,
                                                model='twitter')
            db_tweet = Tweet(id=tweet.id, text=tweet.full_text[:300],
                             embedding=embedding)
            db_user.tweets.append(db_tweet)
            DB.session.add(db_tweet)
    except Exception as e:
        print('Error processing {}: {}'.format(username, e))
        raise e
    else:
        DB.session.commit()


def insert_example_users():
    """Example data to play with."""
    print("1- just entered insert_example_users")
    add_or_update_user('austen')
    print("2- this is twitter.py austen")
    add_or_update_user('elonmusk')
    print("3- this is elon - twtr-py")
    add_or_update_user('jimmykimmel')
    print("4- this is Jimmykimmel - twtr-py")
      

 # Try to upload users in one go
def upload_users():
    """ upload at once"""
    for user in TWITTER_USERS:
        add_or_update_user(user)
        print(f"added_users {user}")
