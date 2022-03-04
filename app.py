"""Main script, uses other modules to generate sentences."""
import imp
from flask import Flask
import histogram, sample
from tokens import tokenize
from markovchain import Markov_chain


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
    return sentence



if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
