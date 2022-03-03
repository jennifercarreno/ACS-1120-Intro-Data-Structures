from cgitb import text
from flask import request
import requests
import urllib.parse

# TODO: 
# set api url
# loop through pages urls
# encode the urls


url = 'https://api.diffbot.com/v3/article?token=8d3acea2ef52e3efe3ea220f4b6284c3&url=http%3A%2F%2Fblog.diffbot.com%2Fdiffbots-new-product-api-teaches-robots-to-shop-online'

# x = requests.get(url).text
# print(x)

token = '8d3acea2ef52e3efe3ea220f4b6284c3'

def create_corpus():
    api_url = 'https://api.diffbot.com/v3/article?token=8d3acea2ef52e3efe3ea220f4b6284c3&url='
    corpus = open("corpus.txt", "a")
    pages = open("pages.txt", "r")

    for line in pages:
        line = urllib.parse.quote(pages.readline())
        new_url = api_url+line
        text = requests.get(new_url).text
        corpus.write(text+"\n")
    corpus.close()
    pages.close()


if __name__ == '__main__':
    create_corpus()
    