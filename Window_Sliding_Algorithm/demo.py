from itertools import pairwise

lst = [1,2,3,4,5]
print("Original list - ", lst)
print("Successive overlapping pairs - ", list(pairwise(lst)))