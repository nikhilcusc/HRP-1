# HackerRankProblems (HRP)
## This repo contains my solutions to Hacker Rank problems.

### NOTES:
1. Dictionary
    1. A dictionary maintains order of keys as they were input. So, if 4 came before 3 as a key in the input the dictonary would not sort it and put 3 before 4 in the keys. [Example](/UnNecCompliProblems/UNCP8.py)
    1. Initialize dictionary with contiguous values:
        > arrD = {i:0 for i in range(0,k)}

1. The distinction between lists and tuples is important: lists are (should be) homogeneous, aka contain a sequence of elements of the same type (think filenames). Tuples are heterogeneous, aka the position of elements has meaning and they are of different types.

1. Range will include the first argument and exclude the second argument. Example:
    >for _ in range(3,6):
    >   print(_)
    >3
    >4
    >5

    Same is true for list indexing. Example:
    > l= [1,3,6,9,22] -> l[2:4] -> [6, 9]
1. When solving problems dealing with 3 related numbers, check if problem is easy to solve looking at second or third number instead of first number. Examples: [finding triplets where the numbers are a factor of a common ratio r.](/ProbSol/countTriplets)
### TODO:
- [ ] In place reversing of doubly linked list.
- [ ] In place merging of sorted Linked list.
- [ ] range update query for multiplication in O(1) time.

1. To generate permutations and combinations include *import itertools*. 

1. Enumerate:
    > for i, v in enumerate(l):
    >...     print(i,v)
    >... 
    >0 4
    >1 3
    >2 5
    >3 7
    
    1. Finding all occurences of a values in a list:
    > occ = [i for i, v  in enumerate(arr) if v==val]
    
