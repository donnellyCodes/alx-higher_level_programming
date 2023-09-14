#!/usr/bin/python3
def uniq_add(my_list=[]):
    """ The fuction below iterates over each element in input list
    append adds function not available in unique_list"""
    unique_list = []
    for i in my_list:
        if i not in unique_list:
            unique_list.append(i)
    return sum(unique_list)
