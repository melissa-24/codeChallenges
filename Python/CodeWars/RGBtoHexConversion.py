# https://www.codewars.com/kata/513e08acc600c94f01000001

# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

# Examples (input --> output):
# 255, 255, 255 --> "FFFFFF"
# 255, 255, 300 --> "FFFFFF"
# 0, 0, 0       --> "000000"
# 148, 0, 211   --> "9400D3"

# HEX = 0-9 and A-F
# RGB = 000-255
# figure out what each rgb range = hex
# 16 HEX choices = 255 numbers
# RGB 148 = HEX 94
# RGB 211 = HEX D3
# number/16 = x + y*16
# R/16 = 148/16 = 9.25 =>  x = 9 => y = (.25*16 = 4)

# Find a way to take each of the 3 numbers provided, and create the x and y hex values


# take RGB value and divide by 16
def divBy16(num):
    if num < 0:
        num = 0
    elif num > 255:
        num = 255
    num = num/16
    return num

# Change the numbers greater than 9 to a-f
def greaterThan9(num):
    if 10 <= num <= 15:
        return chr(ord('A') + num - 10)
    else:
        return str(num)

# Take the divided number and get x and y
def split(val):
    num = divBy16(val)
    toString = str(num)
    xString, yString = toString.split('.')
    x = int(xString)
    x = greaterThan9(x)
    y = float('0.' + yString)
    y = y * 16
    y = int(y)
    y = greaterThan9(y)
    return x + y

def makeHex(a,b,c):
    hex01 = split(a)
    hex02 = split(b)
    hex03 = split(c)
    theHexCode = hex01+hex02+hex03

    return theHexCode


print('returned hex code', makeHex(255,255,255))
print('returned hex code', makeHex(148, 0, 211))
print('returned hex code', makeHex(-20, 275, 125)) # 00FF7D
