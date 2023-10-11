#!/usr/bin/python3
""" function that queries the reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit """
import requests


def top_ten(subreddit):
    """ get top ten posts from subreddit

    Args:
    subreddit (str): subreddit name"
    """
    url = 'https://www.reddit.com/r/{}/.json'.format(subreddit)
    headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0)\
                    Gecko/20100101 Chrome/80.0'
            }
    response = requests.get(url,
                            headers=headers,
                            params={'limit': 10})

    if response.status_code != 200:
        print('None')
        return
    top_posts = response.json().get('data')
    for sub in top_posts.get('children'):
        print(sub.get('data').get('title'))
