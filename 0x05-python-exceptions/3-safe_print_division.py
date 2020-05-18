#!/usr/bin/python3
def safe_print_division(a, b):
    divide = 0
    try:
        divide = a / b
    except:
        pass
    finally:
        if divide:
            print("Inside result: {}".format(divide))
            return (divide)
        else:
            print("Inside result: None")
            return (None)
