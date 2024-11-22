# Meminta pengguna untuk memasukkan sebuah bilangan bulat
bilangan = int(input("Masukkan sebuah bilangan bulat: "))

# Menentukan apakah bilangan tersebut genap atau ganjil
if bilangan % 2 == 0:
    print(f"{bilangan} adalah bilangan genap.")
else:
    print(f"{bilangan} adalah bilangan ganjil.")


# Meminta pengguna untuk memasukkan nilai ujian
nilai = float(input("Masukkan nilai ujian: "))

# Menentukan apakah nilai tersebut lulus atau tidak
if nilai >= 75:
    print("Lulus")
else:
    print("Tidak Lulus")


# Meminta pengguna untuk memasukkan usia
usia = int(input("Masukkan usia: "))

# Menentukan kategori usia
if usia >= 18:
    print("Dewasa")
elif usia >= 13 and usia <= 17:
    print("Remaja")
else:
    print("Anak-anak")
10

# # Meminta pengguna untuk memasukkan status keanggotaan
# status = input("Masukkan status keanggotaan (gold, silver, bronze): ").lower()

# # Menentukan apakah pengguna mendapatkan diskon
# if status == "gold" or status == "silver":
#     print("Selamat! Anda mendapatkan diskon.")
# else:
#     print("Maaf, Anda tidak mendapatkan diskon.")

# # Meminta pengguna untuk memasukkan jumlah pembelian
# jumlah_pembelian = float(input("Masukkan jumlah pembelian: "))

# # Menghitung total harga setelah diskon jika berlaku
# total_harga = jumlah_pembelian * (0.9 if jumlah_pembelian > 100 else 1)

# # Mencetak total harga
# print(f"Total harga setelah diskon: {total_harga:.2f}")
