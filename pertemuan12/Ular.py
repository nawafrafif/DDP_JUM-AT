from ANIMAL import animal

class Ular(animal):

     def __init__(self, nama, makanan, hidup, berkembang_biak, cara_bergerak, jenis_racun):
        super().__init__(nama, makanan, hidup, berkembang_biak), 
        self.cara_bergerak = cara_bergerak
        self.jenis_racun = jenis_racun

     def info_Ular(self):
        super().info_animal(),
        print("Corak Tubuh\t:", self.cara_bergerak,
              "\nBesar Tubuh\t:", self.jenis_racun)

Ular_python = Ular("python", "Daging", "Darat", "bertelur","meliuk", "Tidak berbisa")
Ular_python.info_Ular()
print("===========================================================================")
Ular_mamba = Ular("mamba", "Daging", "Darat", "bertelur","meliuk", "Berbisa")
Ular_mamba.info_Ular()