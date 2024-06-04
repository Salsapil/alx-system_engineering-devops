#!/usr/bin/python3
"""1. Top Ten"""
import requests


def top_ten(subreddit):
    """
    top ten 10 hot posts
    if in valid, prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {'User-Agent': 'CustomUserAgent/0.1'}

    params = {'limit': 10}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json()

    posts = data['data']['children']
    for post in posts:
        print(post['data']['title'])
