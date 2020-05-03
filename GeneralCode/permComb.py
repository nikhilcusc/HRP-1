import itertools
from itertools import permutations, combinations

l = [i for i in range(1,4)]
print(l)
'''
perm = permutations(l)
for i in perm:
    print(i)
'''
print('\n Permutations with 3')
perm2 = permutations(l,3)
rows=[]
for i in perm2:
    print(i)
    rows.append(list(i))
print('\n Permutations of rows : ')
perm22 = permutations(rows,3)
for i in perm22:
    print(list(i))
'''
print('\n Combinations with 3')
comb = combinations(l,3)
for i in comb:
    print(i)
'''