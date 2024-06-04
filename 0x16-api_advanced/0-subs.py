#!/usr/bin/python3
""" script to obtain subscribers
    count from a subreddit
"""
from requests import get


def number_of_subscribers(subreddit):
    """ function to get subscriber count"""
    if subreddit and type(subreddit) is str:
        subscribers = 0
        url = 'http://reddit.com/r/{}/about.json'.format(subreddit)
        headers = {'user-agent': 'Google Chrome Version 125.0.6422.141'}
        req = get(url, headers=headers)
        if req.status_code == 200:
            data = req.json()
            subscribers = data.get('data', {}).get('subscribers', 0)
        return subscribers
