def size_to_number(size):
# m = 38 
# Others increase or decrease by 2
# not allowed xm mx lx sx
    length = len(size)
    base = 38
    if size == 'm':
        print(38)
        return 38
    if length == 1:
        if size == 's':
            print(base - 2)
            return base - 2
        if size == 'l':
            print(base + 2)
            return base + 2
        else:
            return None
    if length > 1:
        if size[-1] == 'l' or size[-1] == 's':
            if 'x' in size:
                num = size.count('x')
                print(num)
                if num + 1 == length:
                    newBase = num * 2
                    print(newBase)
                    if 'l' in size:
                        print(base + newBase + 2)
                        return base + newBase + 2
                    if 's' in size:
                        print(base - newBase - 2)
                        return base - newBase - 2
    else:
        return None