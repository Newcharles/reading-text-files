# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content():
    file = open("./story.txt", "r")
    read_file = file.read()
    global list_data 
    list_data = read_file.rsplit()
    # print(list_data)

def count_words():
    read_file_content()
    word = input("Enter the word you want to count: ")
    splitted_word = word.rsplit()
    result = {}
    for words in splitted_word:
        word_count = list_data.count(words)
        result[words] = word_count
    print(result)

count_words()
