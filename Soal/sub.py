# DEFINISI DAN SPESIFIKASI
# sub : integer, integer>=0 --> integer
#   {sub(x,y) mengurangkan dua buah bilangan integer x dan y}

# REALISASI
def sub(x,y) :
  if y == 0 :
    return x
  else :
    return sub(x,y-1)-1

# APLIKASI
print(sub(4,0))
print(sub(4,1))
print(sub(0,5))
print(sub(6,2))