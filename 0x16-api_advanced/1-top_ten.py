#!/usr/bin/python3
"""Module for task 0"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API"""
    top = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'
                       .format(subreddit),
                       headers={"User-Agent": "linux:/ludaw/0.1"},
                       allow_redirects=False)
    if top.status_code >= 300:
        print('None')
    else:
        for child in top.json().get("data").get("children"):
            print(child.get("data").get("title"))
