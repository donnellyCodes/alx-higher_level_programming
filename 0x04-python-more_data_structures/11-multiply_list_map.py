#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    # lambda function is used to multiply each element by the input number
    return list(map(lambda x: x * number, my_list))
