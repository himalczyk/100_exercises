import re

def count_words_from_file(filepath):

    with open(filepath, 'r+') as file:
        content = file.readlines()
        stringed = ''.join(content)
        splitted = re.split('\s+|,', stringed)
        # splitted_one = content[0].split(",")

    return len(splitted)

print(count_words_from_file('words2.txt'))

#different solution

def count_words(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
    text = text.replace(",", " ")
    string_list = text.split(" ")
    return len(string_list)
 
print(count_words("words2.txt"))