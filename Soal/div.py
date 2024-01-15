# DEFINISI DAN SPESIFIKASI
# div : 2 integer>=0 --> integer>=0
#   {div(x,y) membagi dua buah bilangan integer yaitu x dengan y dengan menghitung jumlah berapa kali x dikurangi y hingga x habis secara rekursif}

# REALISASI
def div(x,y) :
  if x == 0 or y == 0 :
    return 0
  elif x < y :
    return 0
  else :
    return 1+div(x-y,y)

# APLIKASI  
print(div(4,0))
print(div(0,4))  
print(div(4,1))
print(div(5,5))
print(div(9,3))