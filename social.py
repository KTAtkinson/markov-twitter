import twitter

def tweet(chains):
    # Use Python os.environ to get at environmental variables
    # Note: you must run `source secrets.sh` before running this file
    # to make sure these environmental variables are set.
    api = twitter.Api(
        consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
        consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
        access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
        access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])
    user_creds = api.VerifyCredentials()
    statuses = api.GetUserTimeline(screen_name=user_creds.screen_name)
    print statuses[0].text, statuses[0].coordinates

    status = api.PostUpdate(make_text(chains) + ' #Hack13right', latitude=37.7886334,
                            longitude=-122.4136639)
