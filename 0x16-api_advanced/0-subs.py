#!/usr/bin/python3
"""Module for task 0"""


def number_of_subscribers(subreddit):
    """Queries the Reddit API"""
    import requests

    sub = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "linux:/ludaw/0.1"},
                            allow_redirects=False)
    if sub.status_code >= 300:
        return 0

    return sub.json().get("data").get("subscribers")
