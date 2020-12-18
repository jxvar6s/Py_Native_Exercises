#!/usr/bin/env python3.9

# JulianV
# Dec 8, 2020.
# Display a floating number raounded to 2 decimal places.

def main():
    number = user_input()
    round_float(number)

def user_input():
    number = float(input("Enter your integer number: "))
    return number

def round_float(number):
    print("Your number has been rounded to 2 demcimal places as", '%.2f' % number)


if __name__ == "__main__":
    main()