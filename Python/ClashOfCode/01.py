# https://www.codingame.com/clashofcode/clash/report/3786488e4a1cc727646b6d3c49d6b512ca48716

# I am playing a game that is a lot like 2048, but it doesn't tell me my score, so I don't know how well I am doing!

# All I have to do to calculate the score is add up the values of all of the squares. Empty squares, represented by periods, are worth 0 points. The rest are tricky, though, because each square is equal to two to the power to what is shown as a hexadecimal number.

# That means that 1 is represented as 0 (2^0 = 1) and the classic 2048 is represented as b (2^11 = 2048).


# Input
# Line 1: An integer n for the width and height of the board.
# Next n lines: n space-separated squares that are either periods or a hexadecimal digit (0-9a-f).
# Output
# Line 1: The current score of my board.
# Constraints
# 1 ≤ n ≤ 10
# Example
# Input
# 4
# . . . .
# . . 0 .
# . 0 . 1
# . 1 . .

import sys
import math
import re

a = 0
n = int(input())
for i in range(n):
    for s in input().split():
        # check if s is a digit/integer
        if s.isdigit():
            a += pow(2, int(s))
        # if not an integer using regex check and convert hex to int
        elif re.findall("[a-f]", s):
            a += pow(2, int(s,16))
        
print(a)