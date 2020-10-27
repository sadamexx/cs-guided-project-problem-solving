
"""
Challenge #6:
Return the number (count) of vowels in the given string.
We will consider `a, e, i, o, u as vowels for this challenge (but not y).
The input string will only consist of lower case letters and/or spaces.
"""
def get_count(input_str):
    # Your code here
    #count number of vowels
    #keep a counter of how many vowels
    #how do we know it is a vowel?
    #keep a list or string of all the vowels
    # use in
    vowels = "aeiou"
    counter = 0
    for letter in input_str:
        if letter in vowels:
            counter += 1
    return counter


print(get_count("yeah"))
print(get_count("si"))
print(get_count("seee"))
print(get_count("why"))
