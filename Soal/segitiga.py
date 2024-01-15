# Nama file : cek_kabisat.py 
# Pembuat : Dzu Sunan Muhammad - 24060122120034
# Tanggal : 1 September 2022
# Deskripkisi : Mencari tahu tipe segitiga

# Definisi dan Spesifikasi
# Ts : real, real, real --> Boolean
#   {Ts (p,q,r) menentukan sebuah segitiga merupakan segitiga sama sisi atau bukan dengan p,q,r sebagai sisi dan p,q,r > 0 . Apabila true maka merupakan segitiga sama sisi, dan apabila false maka bukan merupakan segitiga sama sisi}

# Realisasi
def Ts (p,q,r) :
  return p==q==r

# Aplikasi
Ts(3,3,3)
Ts(5,5,9)
Ts(12,10,12)
Ts(5.5,5.5,5.5)

print(Ts(3,3,3))
print(Ts(5,5,9))
print(Ts(12,10,12))
print(Ts(5.5,5.5,5.5))