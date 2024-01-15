# Nama file : Factorial_v3.py
# Deskripsi : Menghitung faktorial dari sebuah bilangan integer secara rekursif (contoh yang salah)
# Pembuat : Sunan
# Tanggal : 29 September 2022

# DEFINISI DAN SPESIFIKASI
# faciter : 3 integer>0 --> integer>0
#   {faciter(n,count,hasil) menghitung n! sesuai dengan definisi : fac(n)=1*2*3*...*n = hasil. Ketika sudah mencapai n, dengan 1*2*3*...*(n-1) adalah hasil sebelumnya.}
# jika n = count : hasil (sebelumnya)*count
# jika n < count : faciter(n,count+1,hasil*count)
# fac : integer>0 --> integer>0
#   {fac(n) = n! sesuai dengan definisi rekursif faktorial versi 3, yaitu RUMUS BENAR tetapi PROGRAM SALAH}

# REALISASI
def faciter(n,count,hasil) :
  if n == count :
    return hasil*count
  else :
    return faciter(n,count+1,hasil*count)

def fac(n) :
  return faciter(n,1,1)

# APLIKASI
print(fac(1))
print(fac(3))