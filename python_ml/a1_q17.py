#Write a program in python that converts a given string to title case (first letter of each word capitalized).

string = "good morning"

print("The original string is : " + str(string))
res=string[0].upper() + string[1:]
print("The string after uppercasing initial character : " + str(res))