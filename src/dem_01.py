"""
Challenge #1:
Write a function that retrieves the last n elements from a list.
Examples:
- last([1, 2, 3, 4, 5], 1) ➞ [5]
- last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]
- last([1, 2, 3, 4, 5], 7) ➞ "invalid"
- last([1, 2, 3, 4, 5], 0) ➞ []
Notes:
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.
"""


#a is list, n is the nth element
def last(a, n):
    # Your code here
    # if n is longer than the length of the list, it should return invalid
    # if n is zero, return an empty list

    #how would we do this if we just needed to return the first n elements?
    # we'd want to grab everything starting from index 0 up to N
    # then grab subslice where that starts at
    # the beginning of our input list has length n

    #pythons slicing syntax
    #a[0:n] get first n elements 0 is where we start, n is where we end
    #a[] get last n elements
    #we want to start slicing from len(a) - n and then take everything
    #from there to the end of the list
    #a[len(a) -n:] we dont have to put a number after : because that means we want all the way to the end of list
    if n > len(a):
        return "invalid"

    last_n = a[len(a) - n:]
    return last_n


print(last([4, 3, 9, 9, 7, 6], 3))
print(last([1, 2, 3, 4, 5], 7))
print(last([1, 2, 3, 4, 5], 0))
print(last([1, 2, 3, 4, 5], 1))