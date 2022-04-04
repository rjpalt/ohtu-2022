class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edtila = 0

    def miinus(self, arvo):
        self.edtila = self.tulos
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.edtila = self.tulos
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.edtila = self.tulos
        self.tulos = 0

    def kumoa(self):
        self.tulos = self.edtila

    def aseta_arvo(self, arvo):
        self.tulos = arvo
