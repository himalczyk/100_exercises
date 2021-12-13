from string import ascii_lowercase

for letter in ascii_lowercase:
    with open('letter_per_file/' + letter + '.txt', 'w') as letterfiles:
        letterfiles.writelines(letter)