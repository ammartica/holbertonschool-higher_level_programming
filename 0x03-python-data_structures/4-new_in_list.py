#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy = my_list.copy()
    if idx < 0:
        return cpy
    elif idx >= len(my_list):
        return cpy
    else:
        cpy[idx] = element
        return cpy
