cala_waga = 0
paczki = 0
pusta_waga = 0
ilosc_elementow = 0
ilosc_wagi = 0
waga_wszystkich_paczek = 0
lista_wagi_elementow = []
lista_pusta_waga = []

print("-" * 40)

print("Wpisz liczbe paczek do wyslania ")
ilosc_paczek = int(input())

while True:
    waga = int(input("Podaj wage elementu do wyslania: "))
    if waga < 1:
        if ilosc_wagi > 0:
            pusta_waga = 20 - ilosc_wagi
            lista_pusta_waga.append(pusta_waga)
            paczki += 1
        print("-" * 40)
        print(f"Zakonczono dodawania paczek. Ilosc wyslanych paczek: {paczki}")
        print(f"wyslane kilogramy: {waga_wszystkich_paczek}")
        print(f"ilosc elementow: {ilosc_elementow}")
        print(f"lista wagi wpisanych elementow: {lista_wagi_elementow}")
        if lista_pusta_waga:
            pusta_paczka = lista_pusta_waga.index(max(lista_pusta_waga)) + 1
            max_pusta_waga = max(lista_pusta_waga)
            print(f"najwiecej pustych kilogramow w paczce nr: {pusta_paczka}, zmarnowano {max_pusta_waga} kg")
        break
    if waga > 20:
        if ilosc_wagi > 0:
            pusta_waga = 20 - ilosc_wagi
            lista_pusta_waga.append(pusta_waga)
            paczki += 1
        print("-" * 40)
        print(f"Zakonczono dodawania paczek. Ilosc wyslanych paczek: {paczki}")
        print(f"wyslane kilogramy: {waga_wszystkich_paczek}")
        print(f"ilosc elementow: {ilosc_elementow}")
        print(f"lista wagi wpisanych elementow: {lista_wagi_elementow}")
        if lista_pusta_waga:
            pusta_paczka = lista_pusta_waga.index(max(lista_pusta_waga)) + 1
            max_pusta_waga = max(lista_pusta_waga)
            print(f"najwiecej pustych kilogramow w paczce nr: {pusta_paczka}, zmarnowano {max_pusta_waga} kg")
        break
    if ilosc_wagi + waga > 20:
        pusta_waga = 20 - ilosc_wagi
        lista_pusta_waga.append(pusta_waga)
        paczki += 1
        ilosc_wagi = 0
        print(f"Zaczeto nowa paczke. Ilosc stworzonych paczek: {paczki}")

    waga_wszystkich_paczek += waga
    ilosc_wagi += waga
    ilosc_elementow += 1
    lista_wagi_elementow.append(waga)
    print(f"Podana waga: {waga}")

    if ilosc_wagi == 20:
        lista_pusta_waga.append(0)
        paczki += 1
        ilosc_wagi = 0
        print(f"Paczka gotowa. Ilosc stworzonych paczek: {paczki}")

    if paczki == ilosc_paczek:
        print(f"Zakonczono dodawania paczek. Ilosc wyslanych paczek: {paczki}")
        print(f"wyslane kilogramy: {waga_wszystkich_paczek}")
        print(f"ilosc elementow: {ilosc_elementow}")
        print(f"lista wagi wpisanych elementow: {lista_wagi_elementow}")
        if lista_pusta_waga:
            pusta_paczka = lista_pusta_waga.index(max(lista_pusta_waga)) + 1
            max_pusta_waga = max(lista_pusta_waga)
            print(f"najwiecej pustych kilogramow w paczce nr: {pusta_paczka}, zmarnowano {max_pusta_waga} kg")
        break
