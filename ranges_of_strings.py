# my_range = []
# for item in range(1, 21):
#     my_range.append(str(item))
# print(my_range)

# can also be done with

my_range = range(1, 21)
print(list(map(str, my_range)))