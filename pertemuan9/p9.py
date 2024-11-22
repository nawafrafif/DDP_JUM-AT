def celsius_ke_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    print(fahrenheit)
    
celsius_ke_fahrenheit(0)
celsius_ke_fahrenheit(100)

def is_genap(bilangan):

    return bilangan % 2 == 0

print(is_genap(4))
print(is_genap(7))

def cek_lulus(nilai):
    if nilai >= 70:
        return ("lulus")

    else:
        return ("gagal")

print(cek_lulus(80))
print(cek_lulus(60))

def bilangan_ganjil(n):
    return[i for i in range(1, n+1) if i % 2 != 0]
print(bilangan_ganjil(20))