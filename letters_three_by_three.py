import string

with open("three_letters_alphabet.txt", "w") as file:
    for letter1, letter2, letter3 in zip(string.ascii_letters[0::3], string.ascii_letters[1::3], string.ascii_letters[2::3]):
        file.write(letter1 + letter2 + letter3 + "\n")
        
        
#different solution to cover errors

import string
 
letters = string.ascii_lowercase + " "
 
slice1 = letters[0::3]
slice2 = letters[1::3]
slice3 = letters[2::3]
 
with open("letters_three_by_three.txt", "w") as file:
    for s1, s2, s3 in zip(slice1, slice2, slice3):
        file.write(s1 + s2 + s3 + "\n")