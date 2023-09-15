#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # creating the new dictionary
    new_dictionary = {}
    # iterates through original dictionary
    for key, value in a_dictionary.items():
        new_dictionary[key] = value * 2
    return new_dictionary
