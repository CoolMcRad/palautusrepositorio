from peli import Peli

def main():
    while True:
        peli = Peli()
        peli.tulosta_ohje()

        peli_tyyppi = input()
        uusi_peli = peli.luo_peli(peli_tyyppi)

        if uusi_peli is None:
            break

        uusi_peli.pelaa()

if __name__ == "__main__":
    main()
