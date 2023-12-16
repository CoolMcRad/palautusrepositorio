from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_parempi_tekoaly import KPSParempiTekoaly
from kps_tekoaly import KPSTekoaly

class Peli:

    def luo_peli(self, tyyppi):
        if tyyppi == 'a':
            return KPSPelaajaVsPelaaja()
        if tyyppi == 'b':
            return KPSTekoaly()
        if tyyppi == 'c':
            return KPSParempiTekoaly()

        return None

    def tulosta_ohje(self):
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )
