def f(x):
    return 2*x-1

def wb(xy):
    if xy < 0:
        return -xy
    else:
        return xy

a = -1
b = 4
e = 0.0000000000000001

if f(a)*f(b) <= 0:
    while wb(a-b) > e:
        s = (a+b)/2
        print(s)
        if f(a) * f(s) <= 0:
            b = s
        else:
            a = s

# metody numeryczne