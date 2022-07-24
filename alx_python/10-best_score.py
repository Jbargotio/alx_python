#!/usr/bin/python3

def best_score(a_dictionary):
    num = 0
    if a_dictionary == None:
        return None
    else:
        for key,value in a_dictionary.items():
            if value > num:
                num = value
        return(list(a_dictionary.keys())[list(a_dictionary.values()).index(num)])       
