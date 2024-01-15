# DEFINISI DAN SPESIFIKASI
# perkalian3 : integer --> integer
#   {Perkalian3(n) menghitung perkalian dengan 3 atau f(n)=3*n}

# REALISASI
def perkalian3(x) :
  if x == 0 :
    return 0
  else :
    return perkalian3(x-1)+3

# APLIKASI
print(perkalian3(0))
print(perkalian3(1))
print(perkalian3(2))
print(perkalian3(3))