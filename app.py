print("""Czesc! Jestem programem ktory wysyla paczki.
Podaj element oraz wage elementu w kg aby okreslic ilosc calkowita do wyslania.
Wpisz liczbe mniejsza od 1 lub wieksza od 20 aby wyslac utworzone paczki.""")

print("-" * 40)

ilosc_wagi = 0
ilosc_paczek = 0
puste_kilogramy = 0
ilosc_elementow = 0
najwieksza_ilosc_pustych_elementow = 0
paczka = 0

while True:
    waga = int(input("Podaj wage elementu do wyslania: "))
    if waga < 1:
        puste_kilogramy = ilosc_paczek * 20 - ilosc_wagi
        najwieksza_ilosc_pustych_elementow = 20 - ilosc_wagi
        print(f"""Zakonczono dodawania paczek. Ilosc wyslanych paczek: {ilosc_paczek}
        puste kilogramy: {puste_kilogramy}
        ilosc elementow: {ilosc_elementow}
        najwiecej pustych elementow w paczce nr.: {najwieksza_ilosc_pustych_elementow}kg""")
        break
    if waga > 20:
        puste_kilogramy = ilosc_paczek * 20 - ilosc_wagi
        najwieksza_ilosc_pustych_elementow = 20 - ilosc_wagi
        print(f"""Zakonczono dodawania paczek. Ilosc wyslanych paczek: {ilosc_paczek}
    puste kilogramy: {puste_kilogramy}
    ilosc elementow: {ilosc_elementow}
    najwiecej pustych elementow w paczce nr.: {najwieksza_ilosc_pustych_elementow}kg""")
        break
    if waga < 20:
        ilosc_wagi += waga
        ilosc_elementow += 1
        najwieksza_ilosc_pustych_elementow = 20 - ilosc_wagi
        print(f"Podana waga: {waga}")
    if waga == 20:
        ilosc_paczek += 1
        ilosc_elementow += 1
        najwieksza_ilosc_pustych_elementow = 20 - ilosc_wagi
        waga = 0
        ilosc_wagi = 0
        print(f"Ilosc utworzonych paczek: {ilosc_paczek}")
    if ilosc_wagi == 20:
        ilosc_paczek += 1
        najwieksza_ilosc_pustych_elementow = 20 - ilosc_wagi
        waga = 0
        ilosc_wagi = 0
        print(f"Ilosc utworzonych paczek: {ilosc_paczek}")
