from ANIMAL import animal
class Burung(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, paruh, warna_bulu):
        super().__init__(nama, makanan, hidup, berkembang_biak), 
        self.paruh = paruh
        self.warna_bulu = warna_bulu


    def info_burung(self):
        super().info_animal(),
        print("paruh\t\t:", self.paruh,
              "\nWarna Bulu\t:", self.warna_bulu)

burung_beo = Burung("Beo", "jagung", "Darat", "bertelur","melengkung", "abu-abu")
burung_beo.info_burung()
print("===========================================================================")
burung_merpati = Burung("Merpati", "Beras", "Darat", "bertelur","Lurus", "putih")
burung_merpati.info_burung()