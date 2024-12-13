from Person import *
class Dosen(person):
    pass
    gelar = ""
    Jabatan = ""
    gaji = 0

    def __init__(self, nama, gender,umur , gelar, jabatan,):
        super().__init__(nama,  gender, umur)
        self.gelar =  gelar
        self.jabatan = jabatan
    def setGaji(self,Uang):
        self.gaji += Uang 
    def cetak(self):
        super().cetak()
        print("Gelar \t\t :", self.gender,
              "\nJabatan \t :", self.jabatan,
              "\nGaji \t\t :", self.gaji,
              "\n-------------------------")
        

        