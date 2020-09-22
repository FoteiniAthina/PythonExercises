import datetime

name = input("Give me your name: ")
print("Your name is:  " + name)
age = int(input("Give me your age: "))
print("Your age is: " + str(age))

hundred_years_old = 100 - age

year_now = datetime.datetime.now()

print( name + ", you will be 100 years old in: " +str(year_now.year + hundred_years_old))
