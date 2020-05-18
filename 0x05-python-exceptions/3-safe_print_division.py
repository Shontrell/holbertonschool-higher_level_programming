#!/usr/bin/python3
def safe_print_division(a, b):
    divide = 0
    try:
        divide = a / b
    finally:
        if divide:
            print("Inside result: {:f}".format(divide))
            return (divide)
        else:
            print("Inside result: None")
            return (None)
