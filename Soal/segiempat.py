# Nama file : segiempat.py
# Pembuat : Dzu Sunan Muhammad (24060122120034), Izazava Putri Asari (24060122120038), Nelvina Margery (24060122120002), Adzkiya Qarina Salsabila (24060122140138)
# Tanggal : 1 Oktober 2022
# Deskripkisi : Membuat tipe bentukan segi empat beserta selektor dan konstruktornya

# DEFINISI DAN SPESIFIKASI TYPE SEGI EMPAT
# Type point : <x : real, y : real>
#   {<x,y> adalah sebuah titik dengan x merupakan absis, dan y merupakan ordinat}
# Type persegi : <P1,P2,P3,P4>
#   {<P1,P2,P3,P4> adalah sebuah segi empat dengan P1 titik kiri atas, P2 titik kanan atas, P3 titik kiri bawah, dan P4 titik kanan bawah}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakePoint : 2 Real --> Point
#   {MakePoint(x,y) membentuk sebuah point dari x dan y, dengan x sebagai sebagai absis, dan y sebagai ordinat}
# MakeSegiEmpat : 4 Point --> Segi empat
#   {MakeSegiEmpat(P1,P2,P3,P4) membentuk sebuah segi empat dengan P1 sebagai titik kiri atas, P2 sebagai titik kanan atas, P3 sebagai titik kiri bawah, dan P4 sebagai titik kanan bawah}
# REALISASI
def MakePoint(x,y) :
  return [x,y]
def MakeSegiEmpat(P1,P2,P3,P4) :
  return [P1,P2,P3,P4]

# DEFINISI DAN SPESIFIKASI SELEKTOR
# x : Point --> Real
#   {x(P) memberikan absis x dari titik tersebut}
# y : Point --> Real
#   {y(P) memberikan ordinat y dari titik tersebut}
# P1 : Segi empat --> Point
#   {P1(G) memberikan titik kiri atas P1 dari segi empat tersebut}
# P2 : Segi empat --> Point
#   {P2(G) memberikan titik kanan atas P2 dari segi empat tersebut}
# P3 : Segi empat --> Point
#   {P3(G) memberikan titik kiri bawah P3 dari segi empat tersebut}
# P4 : Segi empat --> Point
#   {P4(G) memberikan titik kanan atas P4 dari segi empat tersebut}
# REALISASI
def x(P) :
  return P[0]
def y(P) :
  return P[1]
def P1(G) :
  return G[0]
def P2(G) :
  return G[1]
def P3(G) :
  return G[2]
def P4(G) :
  return G[3]

# DEFINISI DAN SPESIFIKASI OPERATOR TERHADAP SEGI EMPAT
# Panjang : Segi empat --> Integer
#   {Panjang(G) menghitung panjang dari segi empat G}
# Lebar : Segi empat --> Integer
#   {Panjang(G) menghitung lebar dari segi empat G}
# Luas : Segi empat --> Integer
#   {Panjang(G) menghitung luas dari segi empat G}
# Keliling : Segi empat --> Integer
#   {Panjang(G) menghitung keliling dari segi empat G}
def Panjang(G) :
  return (x(P2(G))-x(P1(G))) or (x(P4(G))-x(P3(G)))
def Lebar(G) :
  return (y(P1(G))-y(P3(G))) or (y(P2(G))-y(P4(G)))
def Luas(G) :
  return Panjang(G)*Lebar(G)
def Keliling(G) :
  return 2*(Panjang(G)+Lebar(G))

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsPersegi : Segi empat --> Boolean
#   {IsPersegi(G) true jika panjang sama dengan lebar. Membuktikan apakah sebuah segi empat merupakan persegi atau bukan}
# IsPersegiPanjang : Segi empat --> Boolean
#   {IsPersegiPanjang(G) true jika panjang tidak sama dengan lebar. Membuktikan apakah sebuah segi empat merupakan persegi panjang atau bukan}
def IsPersegi(G) :
  return Panjang(G) == Lebar(G)
def IsPersegiPanjang(G) :
  return Panjang(G) != Lebar(G)

print(Panjang(MakeSegiEmpat(MakePoint(1,6),MakePoint(4,6),MakePoint(1,3),MakePoint(4,3))))
print(Lebar(MakeSegiEmpat(MakePoint(1,6),MakePoint(4,6),MakePoint(1,3),MakePoint(4,3))))
print(Luas(MakeSegiEmpat(MakePoint(1,6),MakePoint(4,6),MakePoint(1,3),MakePoint(4,3))))
print(Keliling(MakeSegiEmpat(MakePoint(1,6),MakePoint(4,6),MakePoint(1,3),MakePoint(4,3))))
print(IsPersegi(MakeSegiEmpat(MakePoint(1,6),MakePoint(4,6),MakePoint(1,3),MakePoint(4,3))))
print(IsPersegiPanjang(MakeSegiEmpat(MakePoint(1,6),MakePoint(4,6),MakePoint(1,3),MakePoint(4,3))))