def horner(liczba, system):
    liczba_dziesietna = 0
    potega = 0
    litery_szesnastkowe = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    liczba = liczba[::-1]

    for cyfra in liczba:
        if '0' <= cyfra <= '9':
            cyfra = int(cyfra)
        elif 'A' <= cyfra.upper() <= 'F':
            cyfra = litery_szesnastkowe[cyfra.upper()]

        liczba_dziesietna += cyfra * (system ** potega)
        potega += 1

    return liczba_dziesietna


liczby8 = []
with open("liczby2.txt") as plik:
    for linia in plik:
        liczby8.append(linia.strip())
print(liczby8)
liczby10 = []
with open("liczby2.txt") as plik:
    for linia in plik:
        liczby10.append(linia.strip())
print(liczby10)

minimum = int(liczby8[0])
maks =int(liczby8[0])

for i in range(1, len(liczby8)):
    if minimum > int(liczby8[i]):
        minimum = int(liczby8[i])
    if maks < int(liczby8[i]):
        maks = int(liczby8[i])
print(minimum, maks)
pierwszy = int(liczby8[0])
ilosc = 1
maksymalnailosc = 1
pierwszyMaks = pierwszy
for i in range(len(liczby8)-1):
    if int(liczby8[i])<=int(liczby8[i+1]):
        ilosc += 1
        if ilosc > maksymalnailosc:
            maksymalnailosc = ilosc
            pierwszyMaks = pierwszy
    else:
        pierwszy = int(liczby8[i+1])
        ilosc = 1
print(maksymalnailosc, pierwszyMaks)

licznik = 0
licznik2 = 0
for i in range(len(liczby8)):
    if horner(liczby8[i], 8) == liczby10[i]:
        licznik += 1
    if horner(liczby8[i], 8) > liczby10[i]:
        licznik2 += 1
print(licznik, licznik2)