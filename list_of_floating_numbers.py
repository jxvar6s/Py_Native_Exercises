#!/usr/bin/env python3.9

# JulianV
# Dec 8, 2020.
# Fill a list of 5 float numbers.

def main():
    floating_list = fill_float_number_list()
    display_list(floating_list)

def user_input():
    number = float(input("Enter your number with decimals: "))
    return number

def fill_float_number_list():
    floating_numbers = []
    count = 1
    print('\n')
    while count < 6:
        number = user_input()
        floating_numbers.append(number)
        count += 1
    
    return floating_numbers

def display_list(lista):
    print('\n')
    print(" 5 float number list ".center(30,'#'))
    print(f"{lista}\n")


if __name__ == "__main__":
    main()