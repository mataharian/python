# DEFINISI DAN SPESIFIKASI
# deret : integer --> integer
#   {deret(S) menghitung deret bilangan : 1+4+9+16+...}

# REALISASI
def deret(S) :
  if S == 0 :
    return 0
  else :
    return deret(S-1)+S**2

# APLIKASI
print(deret(0))
print(deret(1))
print(deret(2))
print(deret(3))