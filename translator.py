d = dict(weather = "clima", earth = "terra", rain = "chuva")

word = input("Enter word: ")
translate = ''

if d[word]:
    translate = d[word]
    
print(translate)

#other solution

def vocabulary(word):
    return d[word]
word = input("Enter word: ")
print(vocabulary(word))
