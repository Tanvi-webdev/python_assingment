#Write a program that asks the user for their birth year and calculates their age.

birth_year = int(input("What is your birth year : "))
current_year=int(input("Current year : "))
age = current_year - birth_year
print(f"Your age is {age}")