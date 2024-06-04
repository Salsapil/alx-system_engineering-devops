#!/usr/bin/python3
"""3. Count it!"""
import requests
from collections import Counter


def count_words(subreddit, word_list, after=None, word_count=None):
    """
    Recursively queries the Reddit API and counts the occurrences of keywords
    in the titles of hot posts for a given subreddit.
    """

    if word_count is None:
        word_count = Counter()
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {'User-Agent': 'CustomUserAgent/0.1'}

    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()

    posts = data['data']['children']
    if not posts:
        return word_count if word_count else None
