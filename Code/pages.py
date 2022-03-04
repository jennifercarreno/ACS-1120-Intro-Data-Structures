from cgitb import text
from flask import request
import requests


DIFFBOT_API_URL = 'http://api.diffbot.com/v3/article'
DIFFBOT_DEV_TOKEN = '8d3acea2ef52e3efe3ea220f4b6284c3'

def get_article(line):
    params = { 'token': DIFFBOT_DEV_TOKEN,
                'url':line,
                'discussion': 'false' }

    res = requests.get(DIFFBOT_API_URL, params)
    res_obj = res.json()['objects'][0]         

    return res_obj['text'] 


if __name__ == '__main__':
    import sys
    urls_file = open("pages.txt", "r")
    output_file = open('corpus.txt', 'w')

    corpus = ''

    for line in urls_file:
        url = line.strip() 
        article = get_article(url)
        corpus += article

    output_file.write(corpus)
    print('Corpus saved to {}'.format(output_file.name))