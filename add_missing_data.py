checklist = ["Portugal", "Germany", "Spain"]

with open('countries_missing.txt', 'r') as missing_file:
    data = missing_file.readlines()
    data = [i.strip("\n") for i in data if "\n" in i]
    for country in checklist:
        data.append(country)
    data_sorted = sorted(data)
    
with open('countries_missing_added.txt', 'w') as add_file:
    for country in data_sorted:
        add_file.write(country+ "\n")