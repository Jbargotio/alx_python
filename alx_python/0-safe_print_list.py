#!/usr/bin/python
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        while i < x:
            print(my_list[i], end = "")
            i += 1        
        return i        
    except IndexError:
        print()
        return i
