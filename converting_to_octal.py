#!/usr/bin/env python3.9

# JulianV
# Dec 8, 2020.
# Display a decimal number in octal.

def main():
    number = user_input()
    display_octal(number)

def user_input():
    number = int(input("Enter your integer number: "))
    return number

def display_octal(number):
    print(f"Your number {number} is represented in octal as -> {oct(number)}")
    print('%o,' % (number))


if __name__ == "__main__":
    main()