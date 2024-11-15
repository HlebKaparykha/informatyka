def wb(xy):
    if xy < 0:
        return -xy
    else:
        return xy

def pierwiastek(liczba):
    E = 0.00000000001
    a1 = 1
    a2 = liczba

    while wb(a1-a2)>E:

        a1 = (a1+a2)/2
        a2 = liczba/a1
        print(a1, a2)
    return a1

a = int(input("Podaj liczbę: "))
print(f"Pierwiastek z liczby {a} wynosi: {pierwiastek(a)}")