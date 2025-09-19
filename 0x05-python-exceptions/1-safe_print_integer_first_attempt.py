#!/usr/bin/python3


def safe_print_integer(value):
    
    valueInt = False
    try:
        if value / 1:
            valueInt = True
            print("{:d}".format(value))
    except TypeError:
        valueInt = False
        pass
    
    return valueInt