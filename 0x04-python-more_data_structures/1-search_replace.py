#!/usr/bin/python3
def search_replace(my_list, search, replace):
    i = 0
    newlist = my_list.copy()
    for x in newlist:
        if x == search:
            newlist[i] = replace
        i += 1
    return (newlist)
