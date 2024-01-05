#!/usr/bin/python3
"""find peak"""

def find_peak(list_of_integers):
    """finding peak to list of unsorted integers"""
    a = list_of_integers
    l = len(a)
    if l == 0:
        return
    b = l // 2
    if (b == l - 1 or a[b] >= a[b + 1]) and (b == 0 or a[b] >= a[b - 1]):
        return a[b]
    if b != l - 1 and a[b + 1] > a[b]:
        return find_peak(a[b + 1:])
    return find_peak(a[:b])
