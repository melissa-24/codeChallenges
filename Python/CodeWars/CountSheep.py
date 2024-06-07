# https://www.codewars.com/kata/5b077ebdaf15be5c7f000077

# If you can't sleep, just count sheep!!

# Task:
# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.

# loop through numbers starting at 1 to provided number and add a space and sheep... but possibly no space at the end of sheep...
# always valid and no negative is given

print('hello')

def count_sheep(n):
    result = ''
    i = 1
    while(i <= n):
        print(i)
        res = str(i) + " sheep..."
        result = result + res
        i = i+1
    return result

print(count_sheep(3))
