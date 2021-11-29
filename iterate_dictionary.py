
 
d = {"a":list(range(1, 11)), "b":list(range(11, 21)), "c":list(range(21, 31))}
print(f"b has value {d['b']}\nc has value {d['c']}\na has value {d['a']}")

#also can be done with

for key, value in d.items():
    print(key, "has value", value)