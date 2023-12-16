from kivi_sakset_paperi import KiviSaksetPaperi

class KPSPelaajaVsPelaaja(KiviSaksetPaperi):
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = input("Toisen pelaajan siirto: ")
        return tokan_siirto
