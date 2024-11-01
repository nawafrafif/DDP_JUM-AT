# tugas nomor 1
print("=====profil pribadi=====")
nama, nim, kelas, notelp, alamat= "rafif", "0110124197", "SI08", "085691549775", """pondok tirta mandala 
jl. alhikmah raya2 rt004/17"""

print("nama mahasiswa: ",nama)
print("Nim", nim)
print("Kelas Mahasiswa: ", kelas)
print("Nomor Telepon Mahasiswa: ",notelp)
print("Alamat Mahasiswa:", alamat) 

# tugas nomor 2
print("=====profil teman=====")
nama, nim, kelas, notelp, alamat= "syamil", "0110124054", "SI07", "088219412242", """
Desa Banjarsari
Kecamatan Ciawi
Kabupaten Bogor
"""

print("nama mahasiswa: ",nama)
print("Nim", nim)
print("Kelas Mahasiswa: ", kelas)
print("Nomor Telepon Mahasiswa: ",notelp)
print("Alamat Mahasiswa:", alamat) 

# tugas nomor 3
print("=====berat badan ideal=====") 
tb = int(input("masukan tinggi badan"))

bbIdeal = (tb-100) - ((tb-100)*0.1)

print(bbIdeal)
 
# tugas nomor 4
print("=====nilai konversi dari celsius ke fahrenheit=====")
celsius = float(input("masukan nilai celcius"))
fahreinhet = (9/5*celsius)+32
print("fahreinhet = ",fahreinhet)

#tugas nomor 5
print("=====mencari luas dan keliling tabung=====")
r = int(input("masukan jari-jari tabung"))
t = int(input("masukan tinggi tabung"))
phi =3.14 
v = phi *r*r*t
l =2* phi *r*(r+t)
print("volume tabung = ",v)
print("luas tabung =",l)






