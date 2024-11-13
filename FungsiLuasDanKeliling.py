#Fungsi mencari Keliling persegi panjang
def KelilingPersegiPanjang (panjang, lebar):
    return 2*(panjang*lebar)

# Fungsi Mencari Luas Persegi Panjang
def LuasPersegiPanjang (panjang, lebar):
    return panjang*lebar

#NIlai luas jika panjang=10, dari lebar=5
p = int(input("masukkan niai panjang persegi : "))
l = int(input("masukkan nilai lebar persegi : "))

hasil_keliling = KelilingPersegiPanjang(p,l)
hasil_luas = LuasPersegiPanjang(p,l)

print("kelilingnya adalah ", hasil_keliling)
print("Luasnya adalah ", hasil_luas)
