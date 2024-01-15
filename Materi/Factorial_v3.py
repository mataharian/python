# Nama file : Factorial_v3.py
# Deskripsi : Menghitung faktorial dari sebuah bilangan integer secara rekursif (contoh yang salah)
# Pembuat : Sunan
# Tanggal : 29 September 2022

# DEFINISI DAN SPESIFIKASI
# fac : integer>0 --> integer>0
#   {fac(n) = n! sesuai dengan definisi rekursif faktorial versi 3, yaitu RUMUS BENAR tetapi PROGRAM SALAH}

# REALISASI
# Realisasi dengan definisi faktorial fac(n)=n! dimana
# jika n = 1 : n! = 1
# jika n > 1 : n! = (n+1)!/(n+1)
def fac(n) :
  if n == 1 : #basis 1
    return 1
  else : #rekurens : definisi factorial
    return fac(n+1)/(n+1)

# APLIKASI
print(fac(1))
print(fac(3))
print(fac(6))