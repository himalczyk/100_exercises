from string import ascii_lowercase

extracted_alphabet = []

for letter in ascii_lowercase:
    with open('letter_per_file/' + letter + '.txt', 'r') as read_letter_file:
        letter = read_letter_file.readline()
        extracted_alphabet.append(letter)
        
print(extracted_alphabet)