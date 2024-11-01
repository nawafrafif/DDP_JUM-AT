# Tugas no1
# List kendaraan dengan contoh data nyata
kendaraan = ['Toyota', 'SUV', '2000cc', 'Hitam', '4 roda']

# Menambahkan harga dan tipe kendaraan
kendaraan.append(['350 juta', 'Automatic'])

# Menyisipkan merk kendaraan setelah jenis kendaraan
kendaraan.insert(kendaraan.index('SUV') + 1, 'Fortuner')

# Tampilkan list kendaraan yang sudah lengkap
print(kendaraan)

