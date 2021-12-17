from datetime import date

age = input("What is your year of birth?")
todays_date = date.today()

print(f"We think you are {int(todays_date.year) - int(age)}")