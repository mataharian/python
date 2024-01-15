# Nama file : cek_kabisat.py 
# Pembuat : Dzu Sunan Muhammad - 24060122120034
# Tanggal : 1 September 2022
# Deskripkisi : mengecek apakah sebuah tahun merupakan tahun kabisat atau bukan.

# Definisi dan Spesifikasi
# kbst : Integer --> Boolean
#   {kbst (thn) Menenetukan apakah sebuah tahun merupakan tahun kabisat atau bukan dengan cara angka tahun tersebut habis dibagi 400 atau 4 tetapi tidak habis dibagi 100. Apabila true maka merupakan tahun kabisat, dan apabila false maka bukan merupakan tahun kabisat}

# Realisasi
def kbst (thn) :
    return thn%400==0 or thn%4==0 and thn%100!=0

# Aplikasi
kbst(2024)
kbst(1945)

print(kbst(2024))
print(kbst(1945))
