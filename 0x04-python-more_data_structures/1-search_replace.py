#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """ my_list is the initial list
    search is the element to replace the list
    replace is the new element
    """
    return [replace if elem == search else elem for elem in my_list]
