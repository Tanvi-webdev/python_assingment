#Write a python program that removes all punctuation from a given string.

import string

test_str = " what is your name ? and from where? you came  ;"
print("The original string is : " + test_str)
for punctuation in string.punctuation:
    test_str = test_str.replace(punctuation, '')

print("The string after punctuation filter : " + test_str)