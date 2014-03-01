"""
Quicksort algorithm
Using list comprehensions
"""


def quicksort(lst):
    """
    Implementation of the quicksort algorithm
    """
    if len(lst) <= 1:
        return lst
    pivot, rest = lst[0], lst[1:]
    lte = [lte for lte in rest if lte <= pivot]
    gt = [gt for gt in rest if gt > pivot]
    return quicksort(lte) + [pivot] + quicksort(gt)

assert quicksort(range(10)) == range(10)
assert quicksort(range(10)[::-1]) == range(10)
assert quicksort([1, 4, 2, 5, 3]) == sorted([1, 4, 2, 5, 3])
