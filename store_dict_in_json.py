import json

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

# not an optimal solution, use json library
# with open('company1.json', 'w') as json_file:
#     json_file.write(str(d))
    
# different solution
    
with open("company2.json", "w") as file:
    json.dump(d, file, indent=4) #object, to file, 4 white spaces to indent the different levels of the dictionary items