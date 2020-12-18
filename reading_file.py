#!/usr/bin/env python3.9

# JulianV
# Dec 17, 2020.
# Reading line from a given file 
# and display on line 5 from the text file.

def main():
    file_name = input("Enter file name: ")
    lista = reading_file(file_name)
    displaying_line(lista)

def reading_file(file_obj):
    with open(file_obj) as f:
        lines = f.readlines()
    return lines

def displaying_line(list_of_lines):
    print(f"This is line 4 -> {list_of_lines[3].strip()} <-")


if __name__ == "__main__":
    main()