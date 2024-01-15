# DEFINISI DAN SPESIFIKASI
# pangkat : 2 integer --> integer
#   {pangkat(x,y) memangkatkan dua buah bilangan yaitu x dengan y dengan mengalikan x terhadap x sebanyak y kali secara rekursif}

# REALISASI
def pangkat(x, y):
    if y == 0:
        return 1
    else:
        return pangkat(x, y-1)*x

# APLIKASI
print(pangkat(2,2))
print(pangkat(4,2))
print(pangkat(2,4))