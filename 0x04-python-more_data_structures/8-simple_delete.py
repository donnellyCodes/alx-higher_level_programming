#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """ This function modiefies the original dictionary
    by deletinga key """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
