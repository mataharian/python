# Nama file : GanjilGenap.py
# Pembuat : Dzu Sunan Muhammad - 24060122120034
# Tanggal : 16 September 2022
# Deskripkisi : Menentukan ganjil dan genap dari suatu bilangan bulat.

# Definisi dan Spesifikasi
# GanjilGenap : integer --> String
#   {GanjilGenap : (x) Menentukan apakah suatu bilangan bulat bernilai ganjil atau genap, x merupakan suatu bilangan bulat}

# Realisasi
def GanjilGenap(x):
  if x % 2 == 0 :
    return "Genap"
  else :
    return "Ganjil"

# Aplikasi
print(GanjilGenap(15))
print(GanjilGenap(10))
print(GanjilGenap(-52))
print(GanjilGenap(-163))