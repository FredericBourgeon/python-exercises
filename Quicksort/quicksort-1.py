"""
Quicksort algorithm
Simple algorithm
"""


def quicksort(lst):
    """
    Implementation of the quicksort algorithm
    """
    if len(lst) <= 1:
        return lst
    pivot, rest = lst[0], lst[1:]
    lte = []
    gt = []
    for i in rest:
        if i <= pivot:
            lte.append(i)
        else:
            gt.append(i)
    return quicksort(lte) + [pivot] + quicksort(gt)

assert quicksort(range(10)) == range(10)
assert quicksort(range(10)[::-1]) == range(10)
assert quicksort([1, 4, 2, 5, 3]) == sorted([1, 4, 2, 5, 3])
