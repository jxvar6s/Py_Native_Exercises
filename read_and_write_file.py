#!/usr/bin/env python3.9

# JulianV
# Dec 10, 2020.
# reading and writing ito a file.

def main():
    test_file = input("Enter file name: ")
    text_lines = open_file(test_file)
    write_file('new_lines.txt', text_lines)

def open_file(test_file):
    with open(test_file, 'r') as f:
        textlines = f.readlines()
    return textlines

def write_file(final_file, lines):
    counter = 1
    with open(final_file, 'w') as f:
        for line in lines:
            if counter == 5:
                counter += 1
                continue
            else:
                f.write(line)
            counter += 1
# count = 0
# with open("test.txt", "r") as fp:
#     lines = fp.readlines()
#     count = len(lines)
# with open("newFile.txt", "w") as fp:
#     for line in lines:
     
#         if (count == 3):
#             count -= 1
#             print(count)
#             continue
#         else:
#             print(count)
#             fp.write(line)
#         count-=1


#if __name__ == "__main__":
 #   main()