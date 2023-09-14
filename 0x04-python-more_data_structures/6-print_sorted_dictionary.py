#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # this function only sorts first level keys in a dictionary
    for key in sorted(a_dictionary):
        print(key, ':', a_dictionary[key])
