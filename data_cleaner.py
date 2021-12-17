with open('countries_raw.txt', 'r') as to_clean_file:
    data = to_clean_file.readlines()

data = [i.strip("\n") for i in data if "\n" in i]
data = [i for i in data if i !=""]
data = [i for i in data if i !="Top of Page"]
data = [i for i in data if len(i) != 1]
print(data)

with open("countries_clean.txt", "w") as clean_file:
    for i in data:
        clean_file.write(i+"\n")
