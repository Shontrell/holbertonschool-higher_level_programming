#!/usr/bin/python3
def uppercase(str):
    lin = len(str)
    for i in range(0, lin):
        c = ord(str[i])
        if c >= 97 and c <= 122:
            c = c - 32
        print("{:c}".format(c), end="")
    print()
