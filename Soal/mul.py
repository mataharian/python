# DEFINISI DAN SPESIFIKASI
# mul : integer, integer>=0 --> integer
#   {mul(x,y) megnalikan dua buah bilangan integer x dengan y dengan menjumlahkan x terhadap x sebanyak b kali secara rekursif}

# REALISASI
def mul(x,y) :
  if x == 0 or y == 0 :
    return 0
  else :
    return x+mul(x,y-1)
  
# APLIKASI 
print(mul(4,0))
print(mul(0,9))
print(mul(-4,1))
print(mul(5,5))