#Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius




print("Choose an option:")
print("1. Convert from Celsius to Fahrenheit")
print("2. Convert from Fahrenheit to Celsius")
choice = input("Enter your choice (1 or 2): ")

if choice == '1':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit}°F")
elif choice == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius}°C")


