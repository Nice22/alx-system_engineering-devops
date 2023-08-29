#!/usr/bin/python3
"""Contains the count_words function"""
import requests

def count_words(subreddit, word_list, found_dict=None, after=None):
    if found_dict is None:
        found_dict = {}
    '''Prints counts of given words found in hot posts of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        found_list (obj): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
    '''

    user_agent = {'User-agent': 'test45'}
    posts = requests.get(f'http://www.reddit.com/r/{subreddit}/hot.json?after={after}', headers=user_agent)

    if after is None:
        word_list = [word.lower() for word in word_list]

    if posts.status_code == 200:
        posts_data = posts.json()['data']
        aft = posts_data['after']
        posts = posts_data['children']

        for post in posts:
            title = post['data']['title'].lower()
            for word in title.split():
                if word in word_list:
                    if word in found_dict:
                        found_dict[word] += 1
                    else:
                        found_dict[word] = 1

        if aft is not None:
            count_words(subreddit, word_list, found_dict, aft)
        else:
            sorted_results = sorted(found_dict.items(), key=lambda item: (-item[1], item[0]))
            for key, value in sorted_results:
                print('{}: {}'.format(key, value))
    else:
        print("Invalid subreddit or unable to fetch data.")

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], sys.argv[2:])

        return
