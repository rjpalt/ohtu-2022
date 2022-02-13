class IntJoukko:

    # Konstruktori
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        

        #Tarkasta kapasiteetti
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Virheellinen arvo kapasiteetilla.")

        self.kapasiteetti = kapasiteetti
    
        # Tarkasta kasvatuskoko
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Virheellinen arvo parametrille kasvatuskoko.")

        self.kasvatuskoko = kasvatuskoko

        self.ljono = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0


    # Kuuluuko luku joukkoon
    def kuuluu(self, etsittavaLuku):

        if etsittavaLuku in self.ljono:
            return True
        else:
            return False


    def lisaa_alkio(self):
        self.alkioiden_lkm += 1 


    def vahenna_alkio(self):
        self.alkioiden_lkm -= 1


    # Lisaa luku
    def lisaa(self, lisattavaLuku):

        if self.alkioiden_lkm == 0:
            self.ljono[0] = lisattavaLuku
            self.lisaa_alkio()
            return True

        if not self.kuuluu(lisattavaLuku):
            self.ljono[self.alkioiden_lkm] = lisattavaLuku
            self.lisaa_alkio()

            if self.alkioiden_lkm % len(self.ljono) == 0:
                self.korvaa_taulukko_uudella()

            return True

        return False


    # Metodi luvun poistamiseksi lukujoukosta
    def poista(self, poistettavaLuku):

        if poistettavaLuku in self.ljono:
            self.ljono.remove(poistettavaLuku)
            self.vahenna_alkio()
            return True
        else:
            return False



    # Uusi metodi, joka korvaa ohjelman käyttämän taulukon
    def korvaa_taulukko_uudella(self):

        taulukko_old = self.ljono.copy()

        self.ljono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)

        for alkio in taulukko_old:
            self.ljono.append(alkio)



    def mahtavuus(self):

        return self.alkioiden_lkm

        

    def to_int_list(self):

        return [alkio for alkio in self.ljono if alkio != 0]



    @staticmethod
    def yhdiste(taulu_a, taulu_b):
        uusiJoukko = IntJoukko()
        
        for alkio in taulu_a.to_int_list() + taulu_b.to_int_list():
            uusiJoukko.lisaa(alkio)

        return uusiJoukko


    @staticmethod
    def leikkaus(taulu_a, taulu_b):

        yhteistenLukujenJoukko = IntJoukko()

        for alkio in taulu_a.to_int_list():
            if alkio in taulu_b.to_int_list():
                yhteistenLukujenJoukko.lisaa(alkio)

        return yhteistenLukujenJoukko


    @staticmethod
    def erotus(taulu_a, taulu_b):

        uniikkienLukujenJoukko = IntJoukko()

        for alkio in sorted([alkio for alkio in taulu_a.to_int_list() if alkio not in taulu_b.to_int_list()]):
            uniikkienLukujenJoukko.lisaa(alkio)

        return uniikkienLukujenJoukko



    def __str__(self):

        return  '{' + ', '.join([str(alkio) for alkio in self.ljono if alkio != 0]) + '}'
