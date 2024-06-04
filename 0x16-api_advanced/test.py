#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

from requests import get
import requests


def number_of_subscribers(subreddit):
    url = ("https://api.reddit.com/r/{}/about.json".format(subreddit))
    headers = {'User-Agent': 'CustomClient/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    
    response = response.status_code
    print(response)

number_of_subscribers("pro")


