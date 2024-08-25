#!/usr/bin/python3
"""
Function that queries the Reddit API, parses the title of
all hot articles, and prints a sorted count of given
keywords (case-insensitive, delimited by spaces).

"""
import requests


def count_words(subreddit, word_list, after=None, counter={}):
    """
       Prints the count of the given words present in the title of the
    subreddit's hottest articles.
        
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"after": after},
    )
    if counter == {}:
        for word in word_list:
            counter[word.lower()] = 0

    if req.status_code == 200:
        after = req.json().get("data").get("after")
        for get_data in req.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            for word in word_list:
                counter[word.lower()] += title.lower()\
                    .split().count(word.lower())
        if after:
            return count_words(subreddit, word_list, after, counter)
        for word in sorted(counter.items(), key=lambda x: x[1], reverse=True):
            if word[1] != 0:
                print(f"{word[0]}: {word[1]}")
    else:
        return None