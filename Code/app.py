"""Main script, uses other modules to generate sentences."""
from curses import flash
from flask import Flask, render_template, redirect
from Code.tokens import tokenize
from Code.markovchain import Markov_chain
from flask import request
import Code.twitter as twitter


app = Flask(__name__)


@app.before_first_request
def before_first_request():
    """Runs only once at Flask startup"""
    # TODO: Initialize your histogram, hash table, or markov chain here.
    # histogram.histogram("clean_corpus.txt")


@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    corpus = open("clean_corpus.txt", "r").read()
    source = tokenize(corpus)    
    markov = Markov_chain(source)
    sentence = markov.walk()
    return render_template('index.html', sentence = sentence)

@app.route('/tweet', methods=['POST'])
def tweet():
    status = request.form['sentence']
    twitter.tweet(status)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
