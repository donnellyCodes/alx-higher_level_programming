#!/usr/bin/python3
def remove_char_at(str, n):
    # to check whether n is valid
    if n < 0 or n >= len(str):
        return str
    # creating a new string
    new_str = str[:n] + str[n+1:]
    return new_str
