def factorial(n,show=False):
    from math import factorial
    c = n
    f = factorial(n)
    retun = []
    print('{}! = '.format(n), end='')
    if c > 1:
        while c > 0:
            retun.append(str(f' {c} '))
            if c > 1:
                retun.append(' x ')
            elif c == 0:
                retun.append(str(f'= {f}'))
            c -= 1
        for ci in retun:
            return ci
print(factorial(10))
