#!/usr/bin/env python3.9

# JulianV
# Dec 10, 2020.
# flow control

def main():
    is_raining()

def is_raining():
    answer = input("Is it raining? ")
    if answer == 'y' or answer == 'Y':
        response = input("Do you have an umbrella? ")
        if response == 'y' or answer == 'Y':
            print("Go outside.")
        else:
            print("Wait for a while...")
    else:
        print("Go outside...")


if __name__ == "__main__":
    main()