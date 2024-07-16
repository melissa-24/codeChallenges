def sort_gift_code(code):
    # code = input string of upto 26 unique char
    # return alphabetized version of code
    # maybe just use sort()?
    print('what is input', code)
    #     code.sort() fails maybe loop through string into list then apply sort
    arr = []
    newArr = []
    newCode = ''
    for a in code:
        arr.append(a)
        print('a', a, 'arr', arr)
    newArr = sorted(arr)
    for a in newArr:
        newCode += a
    print('what is new input', newCode)

sort_gift_code('pqksuvy')

def updated(code):
    arr = []
    result = ''
    for a in code:
        arr.append(a)
    res = sorted(arr)
    for a in res:
        result += a

updated('pqksuvy')