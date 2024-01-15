# DEFINISI DAN SPESIFIKASI
# deret_arit : integer --> integer
#   {deret_arit(S) menghitung deret bilangan arimatika : 3+6+9+12+...}

# REALISASI
def deret_arit(S) :
  if S == 0 :
    return 0
  else :
    return deret_arit(S-1)+S*3

# APLIKASI
print(deret_arit(0))
print(deret_arit(1))
print(deret_arit(2))
print(deret_arit(3))