a = [1, 2, 3]
b = (4, 5, 6)

x = zip(a, b)

listed = list(x)

for item in listed:
    add = item[0] + item[1]
    print(add)
    
#other solution

for i,j in zip(a,b):
    print(i + j)