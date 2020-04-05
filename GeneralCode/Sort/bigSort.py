'''
Consider an array of numeric strings where each string is a positive number with anywhere from  to  digits. Sort the array's elements in non-decreasing, or ascending order of their integer values and print each element of the sorted array on a new line.
'''

def bigSorting(unsorted):
    
    unsorted.sort(key = lambda x: (len(x), x))
    return unsorted