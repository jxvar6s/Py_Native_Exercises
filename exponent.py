#!/usr/bin/env python3.9

# JulianV
# Dec 4, 2020.
# Make a exponent function.

def main():
    base, exp = user_input()
    exponent(base, exp)

def exponent(base, exp):
    _base, _exp = str(base), str(exp)
    print(f"\n\t{_base} raise to the power of {_exp} is {base**exp} i.e.({(_base +'*')*exp} = {base**exp})\n")

def user_input():
    base = int(input("\nEnter your base number: "))
    exp = int(input("Enter your exponential number: "))
    return base, exp


if __name__ == "__main__":
    main()