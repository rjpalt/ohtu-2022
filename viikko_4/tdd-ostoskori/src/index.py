from ostoskori import Ostoskori
from tuote import Tuote

kori = Ostoskori()

kori.lisaa_tuote(Tuote("Maito", 3))
kori.lisaa_tuote(Tuote("Maito", 3))

print(kori._tuotteet[0]._lukumaara, kori._tuotteet[0].tuotteen_nimi())
print(kori.tavaroita_korissa())