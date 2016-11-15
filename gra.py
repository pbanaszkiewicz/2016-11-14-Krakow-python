import random


def losowa_liczba(low=1, high=100):
    return random.randint(low, high)


def wczytaj_odpowiedz(prompt):
    return int(input(prompt))


def sprawdz_liczbe(dol, gora, zgadniecie, liczba, licznik):
    if not dol <= zgadniecie <= gora:
        print("To nie jest poprawna liczba!")
        return False

    if zgadniecie < liczba:
        print("Niestety! Sprobuj wieksza liczbe")
        return False

    elif zgadniecie > liczba:
        print("Niestety! Sprobuj mniejsza liczbe")
        return False

    else:
        print("Brawo! Udalo Ci sie za {}. razem".format(licznik))
        return True


def gra(liczba, dol, gora):
    print("Zgadnij liczbe z zakresu {} - {}".format(dol, gora))
    licznik = 0
    udalo_sie = False
    while licznik < 7 and not udalo_sie:
        zgadniecie = wczytaj_odpowiedz(">>> ")
        udalo_sie = sprawdz_liczbe(dol, gora, zgadniecie, liczba, licznik)
        licznik += 1
    if not udalo_sie:
        print("Niestety! Nie masz juz wiecej szans")


dol = 1
gora = 100
liczba = losowa_liczba(dol, gora)
gra(liczba, dol, gora)

