from kivi_sakset_paperi import KiviSaksetPaperi
from tekoaly import Tekoaly

class KPSTekoaly(KiviSaksetPaperi):
    def __init__(self):
        self.tekoaly = Tekoaly()

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        return tokan_siirto
