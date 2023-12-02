KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.lukujono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        for i in range(0, self.alkioiden_lkm):
            if n == self.lukujono[i]:
                return True

    def lisaa(self, n):

        if self.alkioiden_lkm == 0:
            self.lukujono[0] = n
            self.alkioiden_lkm +=  1
            return True

        if not self.kuuluu(n):
            self.lukujono[self.alkioiden_lkm] = n
            self.alkioiden_lkm +=  1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm == len(self.lukujono):
                taulukko_old = self.lukujono
                self.lukujono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
                for i in range(0, self.mahtavuus()):
                    self.lukujono[i] = taulukko_old[i]
            return True

        return False

    def poista(self, n):
        aloita_korvaus = False

        if self.kuuluu(n):
            for i in range(0, self.alkioiden_lkm - 1):
                if n == self.lukujono[i]:
                    aloita_korvaus = True
                if aloita_korvaus:
                    self.lukujono[i] = self.lukujono[i + 1]

            self.alkioiden_lkm -= 1
            return True
        return False

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(0, self.alkioiden_lkm):
            taulu[i] = self.lukujono[i]

        return taulu
    
    def hae_index(self, i):
        return self.lukujono[i]

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()

        for i in range(0, a.mahtavuus()):
            x.lisaa(a.hae_index(i))

        for i in range(0, b.mahtavuus()):
            x.lisaa(b.hae_index(i))

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()

        for i in range(0, a.mahtavuus()):
            for j in range(0, b.mahtavuus()):
                if a.hae_index(i) == b.hae_index(j):
                    y.lisaa(b.hae_index(j))

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()

        for i in range(0, a.mahtavuus()):
            z.lisaa(a.hae_index(i))

        for i in range(0, b.mahtavuus()):
            z.poista(b.hae_index(i))

        return z

    def __str__(self):
        merkkijono = "{"
        for i in range(0, self.alkioiden_lkm):
            merkkijono += str(self.lukujono[i])
            if i != self.alkioiden_lkm-1:
                merkkijono += ", "
        merkkijono += "}"
        return merkkijono
