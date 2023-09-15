#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # create a list to store keys to be deleted
    key_delete = []
    for key, v in a_dictionary.items():
        if v == value:
            key_delete.append(key)
    # deleting from dictionary
    for key in key_delete:
        del a_dictionary[key]
    return a_dictionary
