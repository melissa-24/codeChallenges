# Write a function named sumDigits which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits

def sum_digits(number):
    print(number)
    a = []
    num = str(number)
    print(num)
    neg = False
    for i in num:
        if i == '-':
            neg = True
        elif neg == True:
            b = int(i)
            a.append(b)
            neg = False
        else:
            b = int(i)
            a.append(b)
    print(a)
    sum = 0
    for i in a:
        sum += i
        print(sum)
    return sum


sum_digits(10)
sum_digits(-35)