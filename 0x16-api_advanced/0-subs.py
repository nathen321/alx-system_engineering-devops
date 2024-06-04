#!/usr/bin/python3
"""Module for task 0"""
import json
import requests


def number_of_subscribers(subreddit):
    """Read reddit API and return number subscribers """
    cl_id = '3WrsYgFIARz1D-hUyTDBMg'
    sk = 'MB5wiAqzpkow7aZsKsK1lQvlo6W3SQ'
    auth = requests.auth.HTTPBasicAuth(cl_id, sk)
    data = {'grant_type': 'password',
            'username': 'TrainingFly4822',
            'password': 'C@l1gula'}

    headers = {'User-Agent': 'MyBot/1.0.1'}
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)
    TOKEN = res.json()['access_token']
    headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}
    sub_info = requests.get("https://oauth.reddit.com/r/{}/about.json"
                            .format(subreddit), headers=headers)
    print(sub_info.status_code)
    if sub_info.status_code >= 300:
        return 0

    return sub_info.json().get("data").get("subscribers")
