from string import ascii_lowercase

python = "python"
extracted_python = []

for letter in ascii_lowercase:
    with open('letter_per_file/' + letter + '.txt', 'r') as read_letter_file:
        letter = read_letter_file.readline()
        python_single_letter = [char for char in python]
        if letter in python_single_letter:
            extracted_python.append(letter)
        
print(extracted_python)