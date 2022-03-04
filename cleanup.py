clean_chars = [] 
bad_chars = "-*_[].:»?!',;""@#$%^&*()1234567890"

def cleanup(f):
    old_file = open(f, "r")

# loops through each word in corpus
# Iterate through each character of the source text, and append it to a list of “clean” characters unless it is a character to be removed (you can use list membership operations to do this). 
# After iterating through all of the characters, return the joined list of “clean” characters.
# Iterate a list of characters to remove, check if they are found in the source text, and if so delete them. 
# Do the same for characters (or character sequences) to replace, except don’t remove them, but, you know, replace them.

    for line in old_file:
        for word in line:
            # makes list of clean characters
            if word not in bad_chars:
                clean_chars.extend(word.lower().split())
                
    return clean_chars

def test(f):
    old_file = open(f, "r")
    clean_file = open("clean_corpus.txt", "w")
    for line in old_file:
        for word in line:
            for char in word:
                if char not in bad_chars:
                    # print(char)

                    clean_file.write(char.lower())


if __name__ == '__main__':
    cleanup("corpus.txt")
    test("corpus.txt")
   