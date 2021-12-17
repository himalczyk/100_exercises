# 1. Password contains at least one number
# 2. Contains one uppercase letter
# 3. It is at least 5 chars long
# Display message "Password is not fine" if the user didn't create a correct password

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
        

#one loop solution

# while True:
#     psw = input("Enter new password: ")
#     if any(i.isdigit() for i in psw) and any(i.isupper() for i in psw) and len(psw) >= 5:
#         print("Password is fine")
#         break
#     else:
#         print("Password is not fine")

#advanced password checker other solution

# while True:
#     notes = []
#     psw = input("Enter password: ")
#     if not any(i.isdigit() for i in psw):
#         notes.append("You need at least one number")
#     if not any(i.isupper() for i in psw):
#         notes.append("You need at least one uppercase letter")
#     if len(psw) < 5:
#         notes.append("You need at least 5 characters")
#     if len(notes) == 0:
#         print("Password is fine")
#         break
#     else:
#         print("Please check the following: ")
#         for note in notes:
#             print(note)