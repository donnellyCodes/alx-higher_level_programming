#!/usr/bin/python3
"""
function to print a peak in a list of unsorted integers
"""
def find_peak(list_of_integers):
    i = list_of_integers
    if i == []:
        return None
    total = len(i)
    if total == 1:
        return i[0]
    elif total == 2:
        return max(i)
    middle = int(total / 2)
    peak = i[middle]
    if peak > i[middle - 1] and peak > i[middle + 1]:
        return peak
    elif peak < i[middle - 1]:
        return find_peak(i[:middle])
    else:
        return find_peak(i[middle + 1:])
