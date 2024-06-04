#!/usr/bin/python3
"""2. Recurse it!"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {'User-Agent': 'CustomUserAgent/0.1'}

    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return (None)

    data = response.json()

    posts = data['data']['children']
    if not posts:
        return (hot_list if hot_list else None)

    for post in posts:
        hot_list.append(post['data']['title'])

    after = data['data']['after']
    if not after:
        return (hot_list)

    return (recurse(subreddit, hot_list, after))
