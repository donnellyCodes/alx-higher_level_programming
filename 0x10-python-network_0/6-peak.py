#!/usr/bin/python3
"""
Defines peak finding algorithm
"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    i = list_of_integers
    if (not i):
        return None
    if (len(i) <= 2):
        return max(i)
    peak = None
    if (i[0] >= i[1]):
        peak = i[0]
    if (i[-1] >= i[-2]):
        peak = i[-1]
    if (peak):
        return peak

    j = 1
    while (j < len(i) - 1):
        if (i[j] >= i[j + 1] and i[j] >= i[j - 1]):
            return i[j]
        else:
            j += 1
    return peak
