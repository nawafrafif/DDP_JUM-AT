class Gempa:
    lokasi = ' '
    skala = ' '

    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if self.skala <2 :
            ket = 'Gempa tidak berasa'
        elif self.skala >2 and self.skala <4:
            ket = 'Bangunan retak retak'
        elif self.skala >=4 and self.skala <6:
            ket = 'Bangunan roboh'
        else:
            ket = 'Bangunan roboh dan berpotensi stunami'

        print('Lokasi Gempa', self.lokasi, 
              '\nSkala Gempa', self.skala,
              '\nDampak Gempa',ket)

