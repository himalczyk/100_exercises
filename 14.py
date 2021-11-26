d = {"a": 1, "b": 2, "c": 3}
deleting = d.items()
filtered_d = dict((key, value) for key, value in d.items() if value <= 1)
print(filtered_d)