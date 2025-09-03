import math
import random

# 1. Tervehdys omalla nimellä
def tervehdys():
    nimi = input("Anna nimesi: ")
    print(f"Terve, {nimi}!")

# 2. Ympyrän pinta-ala
def ympyran_pinta_ala():
    sade = float(input("Anna ympyrän säde: "))
    ala = math.pi * sade**2
    print(f"Ympyrän pinta-ala on {ala:.2f}")

# 3. Suorakulmion piiri ja pinta-ala
def suorakulmio():
    kanta = float(input("Anna suorakulmion kanta: "))
    korkeus = float(input("Anna suorakulmion korkeus: "))
    piiri = 2 * (kanta + korkeus)
    ala = kanta * korkeus
    print(f"Suorakulmion piiri on {piiri:.2f}")
    print(f"Suorakulmion pinta-ala on {ala:.2f}")

# 4. Kolme kokonaislukua
def kolmelukua():
    a = int(input("Anna ensimmäinen kokonaisluku: "))
    b = int(input("Anna toinen kokonaisluku: "))
    c = int(input("Anna kolmas kokonaisluku: "))
    summa = a + b + c
    tulo = a * b * c
    keskiarvo = summa / 3
    print(f"Lukujen summa on {summa}")
    print(f"Lukujen tulo on {tulo}")
    print(f"Lukujen keskiarvo on {keskiarvo:.2f}")

# 5. Keskiaikaiset mitat
def keskiaikaiset_mitat():
    leiviskat = float(input("Anna leiviskät: "))
    naulat = float(input("Anna naulat: "))
    luodit = float(input("Anna luodit: "))

    # muunnetaan luodeiksi
    kokonaisluodit = leiviskat * 20 * 32 + naulat * 32 + luodit
    grammat = kokonaisluodit * 13.3
    kilogrammat = int(grammat // 1000)
    jäännösgrammat = grammat % 1000

    print("Massa nykymittojen mukaan:")
    print(f"{kilogrammat} kilogrammaa ja {jäännösgrammat:.2f} grammaa")

# 6. Numerolukon koodit
def numerolukko():
    # kolminumeroinen (0–9)
    koodi1 = "".join(str(random.randint(0, 9)) for _ in range(3))
    # nelinumeroinen (1–6)
    koodi2 = "".join(str(random.randint(1, 6)) for _ in range(4))
    print(f"Kolminumeroinen koodi: {koodi1}")
    print(f"Nelinumeroinen koodi: {koodi2}")

# --- Testaa ohjelmia ---
if __name__ == "__main__":
    print("Valitse ohjelma:")
    print("1 = Tervehdys")
    print("2 = Ympyrän pinta-ala")
    print("3 = Suorakulmio")
    print("4 = Kolme kokonaislukua")
    print("5 = Keskiaikaiset mitat")
    print("6 = Numerolukko")

    valinta = input("Anna valinta (1–6): ")

    if valinta == "1":
        tervehdys()
    elif valinta == "2":
        ympyran_pinta_ala()
    elif valinta == "3":
        suorakulmio()
    elif valinta == "4":
        kolmelukua()
    elif valinta == "5":
        keskiaikaiset_mitat()
    elif valinta == "6":
        numerolukko()
    else:
        print("Virheellinen valinta.")
