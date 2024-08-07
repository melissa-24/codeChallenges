# For example:
# 13:00 = one o'clock 
# 13:09 = nine minutes past one 
# 13:15 = quarter past one 
# 13:29 = twenty nine minutes past one
# 13:30 = half past one 
# 13:31 = twenty nine minutes to two
# 13:45 = quarter to two 
# 00:48 = twelve minutes to one
# 00:08 = eight minutes past midnight
# 12:00 = twelve o'clock
# 00:00 = midnight

# Note: If minutes == 0, use 'o'clock'. If minutes <= 30, use 'past', and for minutes > 30, use 'to'. 

ONES = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]  
TEENS = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]  
TENS = ["", "", "twenty", "thirty", "forty", "fifty"]  

# if hours == 0:
#             hourTime = 'midnight'
#         elif hours < 10:
#             hourTime = ONES[hours]
#         elif hours < 24:
#             # print('##1 less than 24', time, hours)
#             hours = hours - 12
#             # (print('##2 minus 12', time, hours))
#             if hours < 10:
#                 hourTime = ONES[hours]
#             else:
#                 hourTime = TEENS[hours // 10]
#             # print('##3 hour', hourTime)

def lessTen(n):
    # print(ONES[n])
    return ONES[n]
def lessTwenty(n):
    # print(TEENS[n - 10])
    return TEENS[n - 10]
def moreTwenty(n):
    # print(TENS[n // 10])
    return TENS[n // 10]
def hourConvert(n):
    if n < 10:
        # print(lessTen(n))
        return lessTen(n)
    elif n < 13:
        print(lessTwenty(n))
        return lessTwenty(n)
    elif n < 22:
        # print(lessTen(n-12))
        return lessTen(n-12)
    elif n < 24:
        # print(lessTwenty(n-12))
        return lessTwenty(n-12)


def readTime(time):
    mins = int(time[3:])
    hours = int(time[0:2])
    lastMins = int(time[4:])
    hTime = ''
    mTime = ''
    result = ''


    hTime = hourConvert(hours)
    print(hours, mins, hTime)
    
    if mins == 0:
        if hours == 0:
            result = 'midnight'
        else:
            result = hTime + " o'clock"
    elif mins == 30:
        if hours == 0:
            result = 'half past midnight'
        else:
            result = 'half past ' + hTime
    elif mins < 30:
        if mins < 10:
            mTime = lessTen(mins) + ' minuets past '
        elif mins < 20:
            mTime = lessTwenty(mins)
        else:
            if lastMins == 0:
                mTime = moreTwenty(mins) + ' minuets past '
            else:
                mTime = moreTwenty(mins) + ' ' + lessTen(lastMins) + ' minuets past '
        result = mTime + hTime
    elif mins > 30:
        mins = 60 - mins
        # lastMins = str(mins)
        # lastMins = int(lastMins[1])
        print('#1', mins, lastMins)
        if mins < 10:
            mTime = lessTen(mins) + ' minuets to '
        elif mins < 20:
            mTime = lessTwenty(mins) + ' minuets to '
        else:
            pass
        print('mTime', mTime)
        result = mTime + hTime
    print('result:', result)




readTime('13:00')
readTime('13:29')
readTime('15:10')
readTime('00:00')
readTime('17:50')
readTime('13:30')
readTime('09:08')
readTime('22:08')
readTime('23:58')
readTime('12:00')
readTime('00:30')
readTime('01:20')

