#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    Sum = 0
    if (len(sys.argv) > 1):
        for i in range(len(sys.argv) - 1):
            Sum += int(sys.argv[i + 1])
    print("{:d}".format(Sum))
