# -*- coding: utf-8 -*-
import tweepy

CONSUMER_KEY = 'Z1r4Yw95FWE1XYax8yRFzQ'
CONSUMER_SECRET = 'jWC5YGfeUZkhjUEN65ZgDQBnWeewJ4niewfpQOekQQ'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth_url = auth.get_authorization_url()
print 'Please authorize: ' + auth_url
verifier = raw_input('PIN: ').strip()
auth.get_access_token(verifier)
print "ACCESS_KEY = '%s'" % auth.access_token.key
print "ACCESS_SECRET = '%s'" % auth.access_token.secret