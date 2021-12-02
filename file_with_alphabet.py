import string
    
with open('file_with_alphabet.txt', 'w+') as file:
    for letter in string.ascii_lowercase:
        file.write(letter + "\n")
    