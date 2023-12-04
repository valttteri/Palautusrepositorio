KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        self.kapasiteetti = kapasiteetti

        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Väärä kasvatuskoko")  # heitin vaan jotain :D
        self.kasvatuskoko = kasvatuskoko

        self.lukujono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lukumaara = 0

    def kuuluu(self, luku:int):
        return luku in self.lukujono

    def lisaa(self, luku:int):
        if not self.kuuluu(luku):
            self.lukujono[self.alkioiden_lukumaara] = luku
            self.alkioiden_lukumaara += 1

            # kasvatetaan listan kapasiteettia tarvittaessa
            self.kasvata_listan_kapasiteettia()
            return True

        return False
    
    def kasvata_listan_kapasiteettia(self):
        if self.alkioiden_lukumaara % len(self.lukujono) == 0:
            taulukko_old = self.lukujono
            self.kopioi_lista(self.lukujono, taulukko_old)
            self.lukujono = self._luo_lista(self.alkioiden_lukumaara + self.kasvatuskoko)
            self.kopioi_lista(taulukko_old, self.lukujono)


    def poista(self, poistettava_luku:int):
        if self.kuuluu(poistettava_luku):
            luvun_indeksi = self.lukujono.index(poistettava_luku)
            self.lukujono[luvun_indeksi] = 0

            for j in range(luvun_indeksi, self.alkioiden_lukumaara - 1):
                self.lukujono[j] = self.lukujono[j + 1]

            self.alkioiden_lukumaara -= 1
            return True

        return False

    def kopioi_lista(self, lukujono_1, lukujono_2):
        for i in range(0, len(lukujono_1)):
            lukujono_2[i] = lukujono_1[i]

    def mahtavuus(self):
        return self.alkioiden_lukumaara

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lukumaara)

        for i in range(0, len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu

    @staticmethod
    def yhdiste(lukujono_1, lukujono_2):
        joukko = IntJoukko()
        a_taulu = lukujono_1.to_int_list()
        b_taulu = lukujono_2.to_int_list()

        for i in range(0, len(a_taulu)):
            joukko.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            joukko.lisaa(b_taulu[i])

        return joukko

    @staticmethod
    def leikkaus(lukujono_1, lukujono_2):
        joukko = IntJoukko()
        a_taulu = lukujono_1.to_int_list()
        b_taulu = lukujono_2.to_int_list()

        for luku in a_taulu:
            if luku in b_taulu:
                    joukko.lisaa(luku)

        return joukko

    @staticmethod
    def erotus(a, b):
        joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for luku in a_taulu:
            joukko.lisaa(luku)

        for luku in b_taulu:
            joukko.poista(luku)

        return joukko

    def __str__(self):
        merkkijono = "{"
        if self.alkioiden_lukumaara == 0:
            return merkkijono+"}"
        
        for i in range(self.alkioiden_lukumaara):
            merkkijono += f"{str(self.lukujono[i])}, "
        return merkkijono[:-2]+"}"
