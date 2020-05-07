#!/usr/bin/python3
def uniq_add(my_list=[]):
    x = 0
    a = set(my_list)
    a = list(a)
    for i in a:
        x += i
    return (x)
