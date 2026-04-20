from itertools import combinations
import numpy as np

### Zadanie 1
def alchemia(skladniki, wymagane, limit):
    liczba_poprawnych = 0
    najwiekszy_zbior = set()

    nazwy = list(skladniki.keys())
    for r in range(1, len(nazwy)+1):
        for kombinacja in combinations(nazwy, r):
            suma_toksycznosci = 0
            wlasciwosci_wywaru = set()

            for nazwa in kombinacja:
                toksycznosc, wlasciwosci = skladniki[nazwa]
                
                suma_toksycznosci += toksycznosc
                wlasciwosci_wywaru ^= wlasciwosci

            if suma_toksycznosci <= limit and wymagane.issubset(wlasciwosci_wywaru):
                liczba_poprawnych += 1
                najwiekszy_zbior = set(kombinacja)

    return liczba_poprawnych, najwiekszy_zbior

skladniki = {
    "Pajęcze Oko": (5, {"widzenie_w_ciemnosci", "zatrucie"}),
    "Jad Wiwerny": (15, {"sila", "zatrucie"}),
    "Łuska Smoka": (30, {"odpornosc_na_ogien", "sila"}), 
    "Kwiat Lotosu": (2, {"leczenie"}),
}

wymagane = {"widzenie_w_ciemnosci", "sila"}
limit = 25



wynik = alchemia(skladniki, wymagane, limit)
print(f"Wynik: {wynik}")

### Zadanie 2
def calka_monte_carlo(N):
    wartosci_x = np.random.uniform(0, 2, N)
    wartosci_y = np.random.uniform(0, 1, N)

    wartosci_fx = np.exp(-wartosci_x**2)
    liczba_trafien = np.sum(wartosci_y < wartosci_fx)

    wynik = 2.0 * (liczba_trafien / N)

    return wynik

print(calka_monte_carlo(10000))