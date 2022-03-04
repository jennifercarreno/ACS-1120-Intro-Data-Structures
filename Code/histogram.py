#  histogram function, takes in a text file
def histogram(source_text):
    # creates an empty dictionary
    histogram_dict = {}

    # splits by word and adds to an array
   
    file = open(source_text, 'r')
    text = file.read()
    words = text.split()
   
    
    # loops through each word 
    for i in range(len(words)):
        #counts how many times the word appears and adds it to the dictionary  
        histogram_dict[words[i]]= words.count(words[i])
        
    print(histogram_dict) 
    return histogram_dict

def histogram_tupple(source_text):
    # creates an empty dictionary
    histogram_tupple = []

    # splits by word and adds to an array
    with open(source_text,) as f:
       words = [word for line in f for word in line.split()]
    
    # loops through each word 
    for i in range(len(words)):
        #counts how many times the word appears and adds it to the dictionary  
        histogram_tupple.append((words[i], words.count(words[i])))
        
    print(histogram_tupple) 
    return histogram_tupple

# unique words function, takes in histogram
def unique_words(histogram):
    count = 0

    # loops through number of items 
    for x in histogram.items():
        count += 1

    print(count)
    return count

# frequency function 
def frequency(word, histogram):

    # for word in histogram, get the number of times the word appears
    for key,value in histogram.items():
        if key == word:
            frequency = histogram[word]

    return print(frequency)

if __name__ == "__main__":
    # histogram_tupple("clean_corpus.txt")
    histogram = histogram("clean_corpus.txt")
    # unique_words(histogram)
    # frequency('rory', histogram)