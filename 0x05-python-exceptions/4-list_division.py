#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    x = 0
    divide = 0
    newlist = []
    for x in range(list_length):
        try:
            divide = my_list_1[x] / my_list_2[x]
        except ZeroDivisionError:
            divide = 0
            print("division by 0")
        except TypeError:
            divide = 0
            print("wrong type")
        except IndexError:
            divide = 0
            print("out of range")
        finally:
            newlist.append(divide)
    return (newlist)
