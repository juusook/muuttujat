class Työntekijä:
    työntekijöiden_lkm = 0
    def __init__(self, etunimi, sukunimi):
        Työntekijä.työntekijöiden_lkm = Työntekijä.työntekijöiden_lkm + 1
        self.työntekijänumero = Työntekijä.työntekijöiden_lkm
        self.etunimi = etunimi
        self.sukunimi = sukunimi

    def tulosta_tiedot(self):
        print(f"{self.työntekijänumero}: {self.etunimi} {self.sukunimi} ")

class Tuntipalkkainen(Työntekijä):
    def __init__(self, etunimi, sukunimi, tuntipalkka):
        self.tuntipalkka = tuntipalkka
        super().__init__(etunimi, sukunimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"tuntipalkka: {self.tuntipalkka}")


class Kuukausipalkkainen(Työntekijä):
    def __init__(self, etuninimi, sukunimi, kuukausipalkka):
        self.kuukausipalkka = kuukausipalkka
        super().__init__(etuninimi, sukunimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kuukausi: {self.kuukausipalkka}")


työntekijät = []

työntekijät.append(Tuntipalkkainen("Juuso", "Kaukko", 1200))
työntekijät.append(Kuukausipalkkainen("Olli", "Jäntti", 3200))
työntekijät.append(Työntekijä("Mikko", "Karjula"))
työntekijät.append(Tuntipalkkainen("Rosa", "Piirinen", 4000))

for t in työntekijät:
    t.tulosta_tiedot()