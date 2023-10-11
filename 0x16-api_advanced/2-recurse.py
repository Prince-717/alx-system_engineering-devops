#!/usr/bin/python3
""" python scripts to list containing the titles
of all hot articles for a given subreddit """
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """ get a list of the titles of all hot posts

    Args:
        subreddit (str): subreddit title
        hot_list (list, optional): list of hot posts. default to []
        after (str, optional): later in the listing. defaults to ""

    Returns:
        list: list of all hot posts
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if type(subreddit) is not str or subreddit is None:
        return None

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0)\
                    Gecko/20100101 Chrome/80.0'
            }

    params = {
        'after': after, 'count': count, 'limit': 100
        }

    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    hot_posts = response.json().get('data', {})
    after = hot_posts.get('after', None)
    count += hot_posts.get('dist', None)
    for i in hot_posts.get('children', None):
        hot_list.append(i.get('data').get('title'))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
