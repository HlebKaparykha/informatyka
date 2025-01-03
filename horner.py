# z dowolnego na 10
def konwertuj_na_dziesietny(liczba, system):
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


liczba_wejsciowa = input("Podaj liczbę: ")
system_wejsciowy = int(input("Podaj system liczbowy liczby wejściowej: "))

wynik = konwertuj_na_dziesietny(liczba_wejsciowa, system_wejsciowy)
print(f"Liczba {liczba_wejsciowa} w systemie {system_wejsciowy} to {wynik} w systemie dziesiętnym.")

# na dowolny

l = int(input("Liczba dziesietna: "))
o = 0
sys = int(input("Podaj system: "))
wynk = []
while l > 0:
    if l%sys<10:
        wynk.insert(0, l%sys)
    else:
        if l%sys == 10:
            wynk.insert(0, 'A')
        if l%sys == 11:
            wynk.insert(0, 'B')
        if l%sys == 12:
            wynk.insert(0, 'C')
        if l%sys == 13:
            wynk.insert(0, 'D')
        if l%sys == 14:
            wynk.insert(0, 'E')
        if l%sys == 15:
            wynk.insert(0, 'F')
    l = l // sys

print(wynk)
ldowsystm = ""
for i in wynk:
    ldowsystm = ldowsystm + str(i)

print(ldowsystm)