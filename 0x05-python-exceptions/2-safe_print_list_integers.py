#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    ni = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            i += 1
        except TypeError:
            i += 1
            ni += 1
            pass
        except ValueError:
            i += 1
            ni += 1
            pass
    print("")
    return (i - ni)
