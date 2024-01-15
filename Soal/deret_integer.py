from tkinter import N


# DEFINISI DAN SPESIFIKASI
# deret_integer : integer --> integer
#   {deret_integer(S)) menghitung deret bilangan integer : 1+2+3+4+...}

# REALISASI
def deret_int(S) :
  if S == 0 :
    return 0
  else :
    return deret_int(S-1)+S

# APLIKASI
print(deret_int(0))
print(deret_int(1))
print(deret_int(2))
print(deret_int(3))