"""
Challenge #9:
Given a string, write a function that returns the "middle" character of the
word.
If the word has an odd length, return the single middle character. If the word
has an even length, return the middle two characters.
Examples:
- get_middle("test") -> "es"
- get_middle("testing") -> "t"
- get_middle("middle") -> "dd"
- get_middle("A") -> "A"
"""

def is_even(n):
    return n % 2 == 0

def get_middle(input_str):
    # Your code here
    #how do we determine if the length is even or odd?
    if is_even(len(input_str)):
        # figure out how to get the middle char(s)
        # return the two chars for even
        midpoint = len(input_str) // 2
        both = input_str[midpoint - 1:midpoint + 1]
        return both
    else:
        #calculate the midpoint index by dividing by two
        # we can't use decimal, so we need to floor it
        # return the single char for odd
        midpoint = len(input_str) // 2
        return input_str[midpoint]


print(get_middle("test"))
print(get_middle("testing"))
print(get_middle("middle"))
print(get_middle("A"))
