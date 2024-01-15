# Nama file : pecahan.py
# Pembuat : Dzu Sunan Muhammad - 24060122120034
# Tanggal : 27 September 2022
# Deskripsi : Membuat tipe bentukan pecahan beserta konstruktor dan selektornya

# DEFINISI TYPE
# type pecahan : <n : integer>=0, d : integer>0>
#   {<n,d> adalah sebuah pecahan dengan n adalah numerator (pembilang) dan d adalah denumerator (penyebut), penyebut sebuah pecahan tidak boleh nol.}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakeP : Integer>=0, Integer>0 --> Pecahan
#   {MakeP(x,y)) membentuk sebuah pecahan dari pembilang x dan penyebut y, dengan x dan y integer.}
# REALISASI
def MakeP (x,y) :
  return [x,y]

# DEFINISI DAN SPESIFIKASI SELEKTOR DENGAN FUNGSI
# Pembagi : Pecahan --> integer>=0
#   {Pemb(p) memberikan numerator pembilang n dari pecahan tersebut.}
# Penyebut : Pecahan --> integer>0
#   {Peny(p) memberikan denumerator penyebut d dari pecahan tersebut.}
# REALISASI
def Pemb(P) :
  return P[0]
def Peny(P) :
  return P[1]

# DEFINISI DAN SPESIFIKASI OPERATOR TERHADAP PECAHAN
# {Operator Aritmatika Pecahan}
# AddP : 2 Pecahan --> Pecahan
#   {AddP(P1,P2) Menambahkan dua buah pecahan P1 dan P2 : n1/d1+n2/d2 = (n1*d2+n2*d1)/d1*d2}
# SubP : 2 Pecahan --> Pecahan
#   {SubP(P1,P2) Mengurangkan dua buah pecahan P1 dan P2 : n1/d1-n2/d2 = (n1*d2-n2*d1)/d1*d2}
# MulP : 2 Pecahan --> Pecahan
#   {MulP(P1,P2) Mengalikan dua buah pecahan P1 dan P2 : n1/d1*n2/d2 = n1*n2/d1*d2}
# DivP : 2 Pecahan --> Pecahan
#   {DivP(P1,P2) Membagi dua buah pecahan P1 dan P2 : (n1/d1)/(n2/d2) = n1*d2/d1*n2}
# RealP : 2 Pecahan --> Real
#   {RealP(P1,P2) Menuliskan bilangan pecahan dalam notasi desimal}
# REALISASI
def AddP (P1,P2) : 
  return ((Pemb(P1)*Peny(P2)+Pemb(P2)*Peny(P1))/(Peny(P1)*Peny(P2)))
def SubP (P1,P2) : 
  return ((Pemb(P1)*Peny(P2)-Pemb(P2)*Peny(P1))/(Peny(P1)*Peny(P2)))
def MulP (P1,P2) : 
  return ((Pemb(P1)*Pemb(P2))/(Peny(P1)*Peny(P2)))
def DivP (P1,P2) : 
  return ((Pemb(P1)*Peny(P2))/(Peny(P1)*Pemb(P2)))
def RealP (P) : 
  return ((Pemb(P))/(Peny(P)))

# DEFINISI DAN SPESIFIKASI PREDIKAT
# {Operator Relasional Pecahan}
# IsEqP? : 2 Pecahan --> Boolean
#   {IsEqP?(P1,P2) true jika p1=p2. 
#   Membandingkan dua buah pecahan sama nilainya : n1/d1 = n2/d2 jika dan hanya jika n1*d2 = n2*d1}
# IsLtP? : 2 Pecahan --> Boolean
#   {IsLtP?(P1,P2) true jika p1<p2. 
#   Membandingkan dua buah pecahan apakah p1 lebih kecil nilainya dari p2 : n1/d1 < n2/d2 jika dan hanya jika n1*d2 < n2*d1}
# IsGtP? : 2 Pecahan --> Boolean
#  {IsGtP?(P1,P2) true jika p1>p2. 
#   Membandingkan dua buah pecahan apakah p1 lebih besar nilainya dari p2 : n1/d1 > n2/d2 jika dan hanya jika n1*d2 > n2*d1}
# REALISASI
def IsEqP(P1,P2) :
  return Pemb(P1)*Peny(P2) == Pemb(P2)*Peny(P1)
def IsLtP(P1,P2) :
  return Pemb(P1)*Peny(P2) < Pemb(P2)*Peny(P1)
def IsGtP(P1,P2) :
  return Pemb(P1)*Peny(P2) > Pemb(P2)*Peny(P1)

# APLIKASI
print(AddP(MakeP(4,4),MakeP(4,4)))
print(SubP(MakeP(8,4),MakeP(4,4)))
print(MulP(MakeP(4,2),MakeP(6,2)))
print(DivP(MakeP(8,2),MakeP(6,3)))
print(RealP(MakeP(10,5)))
print(IsEqP(MakeP(5,5),MakeP(5,5)))
print(IsLtP(MakeP(4,2),MakeP(8,2)))
print(IsGtP(MakeP(4,2),MakeP(2,2)))