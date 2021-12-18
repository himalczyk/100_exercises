checklist = ["Portugal", "Germany", "Munster", "Spain"]

with open('countries_clean.txt', 'r') as check_file:
    checkfile = check_file.read().split()
checked = [i for i in checklist if i not in checkfile] #compare items from list with countries and sort only the one that is not fitting
checklist.remove(''.join(checked))
print(checklist)
