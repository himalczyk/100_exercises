d = dict(weather = "clima", earth = "terra", rain = "chuva")

word = input("Enter word: ")

def vocabulary(word):
    try:
        return d[word]
    except KeyError:
        print("That word doesn't exist!")
        
print(vocabulary(word))
    