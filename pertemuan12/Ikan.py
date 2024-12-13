from ANIMAL import animal

class ikan(animal):
     def __init__(self, nama, makanan, hidup, berkembang_biak, corak_tubuh, warna_tubuh):
        super().__init__(nama, makanan, hidup, berkembang_biak), 
        self.corak_tubuh = corak_tubuh
        self.warna_tubuh = warna_tubuh

     def info_ikan(self):
        super().info_animal(),
        print("Corak Tubuh\t:", self.corak_tubuh,
              "\nBesar Tubuh\t:", self.warna_tubuh)

ikan_hiu = ikan("Hiu", "Daging", "Air", "Melahirkan","Tutul", "abu-abu")
ikan_hiu.info_ikan()
print("===========================================================================")
ikan_koi = ikan("Koi", "Pelet", "Air", "bertelur","Kohaku", "hitam putih oren")
ikan_koi.info_ikan()