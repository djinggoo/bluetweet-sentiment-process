from apps.run import db


class AccountTweet(db.Model):
    """this is model / or entity for account tweet"""
    id = db.Column(db.String(), primary_key=True)
    account_id = db.Column(db.Integer)
    twitter_id = db.Column(db.Integer)
    tweet = db.Column(db.String())
    tweet_created_at = db.Column(db.Date)
    created_at = db.Column(db.Date)

    def __init__(self, id, account_id, twitter_id, tweet, tweet_created_at, created_at):
        self.id = id
        self.account_id = account_id
        self.twitter_id = twitter_id
        self.tweet = tweet
        self.tweet_created_at = tweet_created_at
        self.created_at = created_at