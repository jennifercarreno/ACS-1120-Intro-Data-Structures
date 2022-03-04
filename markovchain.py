
from dictogram import Dictogram
from tokens import tokenize
from random import choice, random
from cleanup import cleanup

class Markov_chain():
    
    def __init__(self, words) -> None:
        # list of tokens, iterates through the list of tokens and creates a list of words that appear after
        self.chain = {}
        self.hist = Dictogram()
        
        # words = tokens from source
        for i in range(len(words)-2):

            # creates a pair of words, word[i] = word, wor[i+2] = next word
            pair = (words[i], words[i+1])
            self.hist.add_count(pair)
            
            # if its not already in the chain, create a dictogram for it. pair -> key of a dictogram
            if pair not in self.chain.keys():
                self.chain[pair] = Dictogram()
            # already exists in chain -> adds next word
            self.chain[pair].add_count(words[i+2])
                

    def walk(self, length=15) -> str:
        #  generates random word, random word lives in dictionary, then get the list of values and chose a random one and string them together
        words = []
        pairs = []
        
        start = self.hist.sample() #generates random word
        
        current_pair = start

        while len(pairs) <= length and current_pair:
            
            pairs.append(current_pair) 
            new_word = self.choose_next_word(current_pair) #returns next randomly generated word
            new_pair = (current_pair[len(current_pair)-1], new_word) #sets the new word to the current one, keeps moving
            # print(current_pair, new_word, new_pair)
            current_pair = new_pair
            
        
        for pair in pairs:
            if pair is not pairs[len(pairs)-1]:
                words.append(pair[1])
        
        
        sentence = ''
        for word in words:
            sentence += word + ' '
        
        return sentence
    
    def choose_next_word(self, pair):
        # checks if the word is in chain
        if pair not in self.chain.keys():
            return None
        # if it is, choices is the list of words, value, key = pair, value = choicea
        choices = self.chain[pair]
        return choices.sample() # returns randomly generated word
            

if __name__ == '__main__':
    
    corpus = open("clean_corpus.txt", "r").read()
    source = tokenize(corpus)    
    markov = Markov_chain(source)
    sentence = markov.walk()
    
    print(sentence)
