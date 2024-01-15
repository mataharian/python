# DEFINISI DAN SPESIFIKASI
# deret_geo : integer --> integer
#   deret_geo(S) menghitung deret bilangan geometri : 1+3+9+27+...}

# REALSIASI
def deret_geo(S) :
  if S == 0 :
    return 0
  else :
    return deret_geo(S-1)+3**(S-1)

# APLIKASI
print(deret_geo(0))
print(deret_geo(1))
print(deret_geo(2))
print(deret_geo(3))