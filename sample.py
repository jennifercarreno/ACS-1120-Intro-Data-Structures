from json.tool import main
import random
import Code.histogram as histogram

# chooses a random word from the list of words in the histogram
def sample(source_text):
    file = open(source_text, 'r')
    text = file.read()
    words = text.split()

    sum = len(words)
    dart = random.randint(0,sum)

    count = 0 

    for word in words:
        # print((f"Before: {count}"))
        count += words.count(word)

        if (dart - count) > 0:
            count = count
            # print(f"After: {count}")
            # print(f"NON-WORD: {word}, COUNT: {count}")
        else: 
            print(f"DART: {dart},WORD: {word}, WORD COUNT: {words.count(word)} SUM: {sum}")
            return word


# returns the amount of times the dart lands on each word
def sample_test(source_text):
    
    repeats = {}
    words = []
    for i in range(10000):
        words.append(sample(source_text))
        repeats[words[i]]= words.count(words[i])

   
    return(print(f"{repeats}"))

if __name__ == "__main__":
    # histogram_dict = histogram.histogram("sample.txt")
    sample("clean_corpus.txt")
    
    # sample_test("sample.txt")

  