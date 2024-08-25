#!/usr/bin/python3
"""
Queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.

"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit.
    
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"after": after},
    )

    if req.status_code == 200:
        after = req.json().get("data").get("after")
        for get_data in req.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            hot_list.append(title)
        if after:
            recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None