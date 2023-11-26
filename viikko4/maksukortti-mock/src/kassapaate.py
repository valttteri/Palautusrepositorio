HINTA = 5


class Kassapaate:
    def __init__(self):
        self.myytyja_lounaita = 0

    def lataa(self, kortti, summa):
        if summa >= 0:
            kortti.lataa(summa)
        else:
            print("Negatiivinen arvo ei kelpaa")

    def osta_lounas(self, kortti):
        if kortti.saldo >= HINTA:
            kortti.osta(HINTA)
            self.myytyja_lounaita = self.myytyja_lounaita + 1
        else:
            print("Kortilla ei ole tarpeeksi saldoa")
