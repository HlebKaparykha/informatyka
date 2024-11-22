def f(x):
    return x*x+1

a = 0
b = 2
e = 100000

calka = 0
szer = (b-a)/e

for i in range(e):
    wys = f(a+i*szer)
    calka += szer * wys

print(calka)