"""
Challenge #10:
Given a string of space separated integers, write a function that returns the
maximum and minimum integers.
Example:
- max_and_min("1 2 3 4 5") -> "5 1"
- max_and_min("1 2 -3 4 5") -> "5 -3"
- max_and_min("1 9 3 4 -5") -> "9 -5"
Notes:
- All inputs are valid integers.
- There will always be at least one number in the input string.
- The return string must be two numbers separated by a single space, and
the maximum number is first.
"""
def max_and_min(input_str):
    # Your code here
    #given string of numbers, figure out min and max
    # we have functions "max" and "min" which we can use
    # max and min only work on non negative numbers
    #what do we do with negative numbers? we cant use the string, we need numbers
    #convert string to a list of numbers
    #how? split on spaces,then use the int
    #once we have list of numbers, we can use max and min
    str_digits = input_str.split(" ")
    integers = []
    for n in str_digits:
        num = int(n)
        integers.append(num)
    large = max(integers)
    small = min(integers)
    # use f string to return
    return f"{large} {small}"


print(max_and_min("1 2 3 4 5"))
print(max_and_min("1 2 -3 4 5"))
print(max_and_min("1 9 3 4 -5"))