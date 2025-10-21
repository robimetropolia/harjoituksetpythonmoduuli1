import random

# 1. Arpakuutioiden silmälukujen summa
def heita_nopat():
    n = int(input("Anna arpakuutioiden määrä: "))
    summa = 0
    for i in range(n):
        heitto = random.randint(1, 6)
        summa += heitto
    print(f"Noppien silmälukujen summa on {summa}")


# 2. Viisi suurinta syötettyä lukua
def viisi_suurinta():
    luvut = []
    while True:
        syote = input("Anna luku (tyhjä lopettaa): ")
        if syote == "":
            break
        luvut.append(float(syote))
    luvut.sort(reverse=True)
    print("Viisi suurinta lukua ovat:")
    for luku in luvut[:5]:
        print(luku)


# 3. Alkuluvun tarkistus
def tarkista_alkuluku():
    luku = int(input("Anna kokonaisluku: "))
    if luku < 2:
        print("Luku ei ole alkuluku.")
    else:
        on_alkuluku = True
        for i in range(2, int(luku ** 0.5) + 1):
            if luku % i == 0:
                on_alkuluku = False
                break
        if on_alkuluku:
            print(f"Luku {luku} on alkuluku.")
        else:
            print(f"Luku {luku} ei ole alkuluku.")


# 4. Kaupunkien nimet
def kaupungit_listaan():
    kaupungit = []
    for i in range(5):
        nimi = input(f"Anna {i+1}. kaupungin nimi: ")
        kaupungit.append(nimi)
    print("\nKaupungit:")
    for kaupunki in kaupungit:
        print(kaupunki)


# Päävalikko
def main():
    while True:
        print("\nValitse tehtävä:")
        print("1 = Arpakuutiot")
        print("2 = Viisi suurinta lukua")
        print("3 = Alkuluku")
        print("4 = Kaupungit")
        print("0 = Lopeta")
        valinta = input("Valintasi: ")

        if valinta == "1":
            heita_nopat()
        elif valinta == "2":
            viisi_suurinta()
        elif valinta == "3":
            tarkista_alkuluku()
        elif valinta == "4":
            kaupungit_listaan()
        elif valinta == "0":
            print("Ohjelma lopetetaan.")
            break
        else:
            print("Virheellinen valinta, yritä uudelleen.")

main()

