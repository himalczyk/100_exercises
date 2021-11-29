def string_splitter(word: str):
    
    the_list_of_words = word.split(" ")
    
    return len(the_list_of_words)

print(string_splitter("A random sentence"))