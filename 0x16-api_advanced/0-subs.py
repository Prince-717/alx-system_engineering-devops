#!/usr/bin/python3
"""
Python script to use Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """ subreddit number of subscribers

    Args:
        subreddit (str): name of subreddit

    Returns:
        int: nbr of subs on success, 0 on failure
    """
    headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0)\
                    Gecko/20100101 Chrome/80.0'
            }
    response = requests.get('https://www.reddit.com/r/{}/about.json'
                            .format(subreddit),
                            headers=headers,
                            allow_redirects=False)

    if response.status_code != 200:
        return (0)

    response = response.json()
    count = response.get('data', {})
    return (count.get('subscribers', 0))
