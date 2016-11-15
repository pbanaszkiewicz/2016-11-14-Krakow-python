kolumna1 = []
kolumna2 = []

for linia in open('reference.csv'):
    dane = linia.split(',')
    kolumna1.append(float(dane[0]))
    kolumna2.append(float(dane[1]))

liczba_linii = len(kolumna1)

plik = open('wynik.csv', 'w')
plik.write(str(liczba_linii) + "\n")

for indeks in range(liczba_linii):
    linia = '{:.3e};{:.3f}\n'.format(kolumna1[indeks], kolumna2[indeks])
    plik.write(linia)

plik.close()


###################
# w funkcji
# wywołanie:
#   podmiana_formatu(1) dla plików reference1.csv i wynik1.csv
def podmiana_formatu(i):
    kolumna1 = []
    kolumna2 = []

    for linia in open('reference{}.csv'.format(i)):
        dane = linia.split(',')
        kolumna1.append(float(dane[0]))
        kolumna2.append(float(dane[1]))

    liczba_linii = len(kolumna1)

    plik = open('wynik{}.csv'.format(i))
    plik.write(str(liczba_linii) + "\n")

    for indeks in range(liczba_linii):
        linia = '{:.3e};{:.3f}\n'.format(kolumna1[indeks], kolumna2[indeks])
        plik.write(linia)

    plik.close()

