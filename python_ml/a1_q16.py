#Write a program in python that counts the frequency of each character in a string.
def count_characters(input_string):
    # Initialize an empty dictionary to store character frequencies
    char_frequency = {}

    # Count frequency of each character in the input string
    for char in input_string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    return char_frequency


# Input string
input_string = input("Enter a string: ")

# Count frequency of each character
frequency_dict = count_characters(input_string)

# Print the character frequencies
print("\nCharacter frequencies:")
for char, freq in frequency_dict.items():
    print(f"'{char}' : {freq}")



