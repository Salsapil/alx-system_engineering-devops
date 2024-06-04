#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """
    number_of_subscribers.
    if invalid, the function returns 0.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {'User-Agent': 'CustomUserAgent/0.1'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code != 200:
            return 0

        data = response.json()
        return data['data']['subscribers']

    except (requests.RequestException, ValueError, KeyError):
        return 0
