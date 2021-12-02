import string

with open('two_letters_alphabet.txt', 'w+') as file:
        for letter in string.ascii_letters:
                file.write(string.ascii_letters[0]+string.ascii_letters[1] + "\n")
                string.ascii_letters = string.ascii_letters[2:]
                index_exist = len(string.ascii_letters)
                if(index_exist == False):
                    break
                
#different "smarter" solution

with open("letters.txt", "w") as file:
    for letter1, letter2 in zip(string.ascii_letters[0::2], string.ascii_letters[1::2]):
        file.write(letter1 + letter2 + "\n")
