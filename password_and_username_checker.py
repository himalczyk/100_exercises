def has_digit(value):
    for char in value:
        if char.isdigit():
            return True
    return False

def has_upper(value):
    for char in value:
        if char.isupper():
            return True
    return False

while True:
    while True:
        username = input("Enter username: \n")
        with open('users.txt', 'r') as check_user_f:
            users = check_user_f.read()
        if username in users:
            print('Username exists')
        else:
            break
    password = input("Please enter a password: \n")
    if not len(password) >= 5: 
        print("Password incorrect. Needs at least 5 characters long")
    elif not has_digit(password) and not has_upper(password):
        print('Password incorrect. Needs at least 1 digit and 1 upper char.')
    elif not has_digit(password):
        print("Password incorrect. Needs at least 1 digit.")
    elif not has_upper(password):
        print("Password incorrect. Needs at least 1 uppercase character.")
    elif len(password) >= 5 and has_digit(password) and has_upper(password):
        print("Password is correct")
        break