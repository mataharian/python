# Nama file : pecahanc.py
# Pembuat : Dzu Sunan Muhammad (24060122120034), Izazava Putri Asari (24060122120038), Nelvina Margery (24060122120002), Adzkiya Qarina Salsabila (24060122140138)
# Tanggal : 1 Oktober 2022
# Deskripkisi : Membuat tipe bentukan pecahan campuran beserta selektor dan konstruktornya

# DEFINISI DAN SPESIFIKASI TYPE PECAHAN CAMPURAN
#  type pecahan : <pemb : integer>=0, peny : integer>0>
#   {<pemb,peny> adalah sebuah pecahan dengan pemb adalah numerator (pembilang) dan peny adalah denumerator (penyebut), penyebut sebuah pecahan tidak boleh nol}
# type pecahanc : <bil : integer, n : integer>=0, d : integer>0>
#   {<bil,n,d> adalah sebuah pecahan dengan bil merupakan bilangan bulat pecahan dapat bernilai positif, nol, maupun negatif. n adalah numerator (pembilang) hanya dapat bernilai integer positif atau nol. d adalah denumerator (penyebut) hanya dapat bernilai positif lebih dari nol. Pembilang selalu lebih kecil dari penyebut (n<d)}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakeP : Integer>=0, Integer>0 --> Pecahan
#   {MakeP(pemb,peny)) membentuk sebuah pecahan dari pembilang pemb dan penyebut peny, dengan pemb integer positif atau nol dan pemb integer positif lebih dari nol}
# MakePC : Integer, Integer>=0, Integer>0 --> Pecahan campuran
#   {MakePC(bil,n,d)) membentuk sebuah pecahan campuran dari bilangan bulat pecahan bil, pembilang n, dan penyebut d, dengan bil merupakan integer bernilai positif, nol, maupun negatif.  n merupakan bilangan integer positif atau nol. d merupakan integer positif lebih dari nol}
# REALISASI
def MakeP(pemb,peny) :
  return [pemb,peny]
def MakePC(bil,n,d) :
  return [bil,n,d]

# DEFINISI DAN SPESIFIKASI SELEKTOR DENGAN FUNGSI
# Pemb : Pecahan --> integer>=0
#   {Pemb(P) memberikan numerator pembilang pemb dari pecahan campuran tersebut}
# Peny : Pecahan --> integer>0
#   {Peny(P) memberikan denumerator penyebut peny dari pecahan campuran tersebut}
# Bil : Pecahan campuran --> Integer
#   {Bil(P) memberikan bilangan bulat pecahan bil dari pecahan campuran tersebut}
# n : Pecahan campuran --> Integer>=0
#   {n(P) memberikan numerator pembilang n dari pecahan campuran tersebut}
# d : Pecahan campuran --> integer>0
#   {d(p) memberikan denumerator penyebut d dari pecahan campuran tersebut}
# REALISASI
def Pemb(P) :
  return P[0]
def Peny(P) :
  return P[1]
def bil(P) :
  return P[0]
def n(P) :
  return P[1]
def d(P) :
  return P[2]

# DEFINISI DAN SPESIFIKASI OPERATOR TERHADAP PECAHAN CAMPURAN
# KonversiPecahan : Pecahan campuran --> Pecahan
#   {KonversiPecahan(P) mengubah pecahan campuran P ke tipe pecahan biasa, jika pecahan bernilai negatif maka nilai negatif diletakkan pada pembilang}
# KonversiReal : Pecahan campuran --> Real
#   {KonveriReal(P) mengubah pecahan campuran P menjadi nilai real}
# KonversiCampuran : Pecahan --> Pecahan campuran
#   {KonversiCampuran(P) mengubah pecahan biasa P ke tipe pecahan campuran}
# AddPB : 2 Pecahan --> Pecahan
#   {AddP(P1,P2) Menambahkan dua buah pecahan biasa P1 dan P2}
# SubPB : 2 Pecahan --> Pecahan
#   {SubP(P1,P2) Mengurangkan dua buah pecahan biasa P1 dan P2}
# MulPB : 2 Pecahan --> Pecahan
#   {MulP(P1,P2) Mengalikan dua buah pecahan biasa P1 dan P2}
# DivPB : 2 Pecahan --> Pecahan
#   {DivP(P1,P2) Membagi dua buah pecahan biasa P1 dan P2}
# AddP : 2 Pecahan campuran --> Pecahan campuran
#   {AddP(P1,P2) Menambahkan dua buah pecahan campuran P1 dan P2}
# SubP : 2 Pecahan campuran --> Pecahan campuran
#   {SubP(P1,P2) Mengurangkan dua buah pecahan campuran P1 dan P2}
# MulP : 2 Pecahan campuran --> Pecahan campuran
#   {MulP(P1,P2) Mengalikan dua buah pecahan campuran P1 dan P2}
# DivP : 2 Pecahan campuran --> Pecahan campuran
#   {DivP(P1,P2) Membagi dua buah pecahan campuran P1 dan P2}
# REALISASI
def KonversiPecahan(P) :
  if bil(P)>=0 :
    return MakeP(bil(P)*d(P)+n(P),d(P))
  else :
    return MakeP(bil(P)*d(P)-n(P),d(P))
def KonversiReal(P) :
  if bil(P)>=0 :
    return (bil(P)*d(P)+n(P))/d(P)
  else :
    return (bil(P)*d(P)-n(P))/d(P)
def KonversiCampuran(P) :
  if (Pemb(P)>=0 and Peny(P)>0) or (Pemb(P)<0 and Peny(P)<0) :
    return MakePC(Pemb(P)//Peny(P),Pemb(P)%Peny(P),Peny(P))
  elif abs(Pemb(P))<abs(Peny(P)) :
    return MakePC(Pemb(P)//Peny(P)+1,-(abs(Pemb(P))%abs(Peny(P))),abs(Peny(P)))
  else :
    return MakePC(Pemb(P)//Peny(P)+1,abs(Pemb(P))%abs(Peny(P)),abs(Peny(P)))
def AddPB(P1,P2) :
  return MakeP(Pemb(P1)*Peny(P2) + Pemb(P2)*Peny(P1),Peny(P1)*Peny(P2))
def SubPB(P1,P2) :
  return MakeP(Pemb(P1)*Peny(P2) - Pemb(P2)*Peny(P1),Peny(P1)*Peny(P2))
def MulPB(P1,P2) :
  return MakeP(Pemb(P1)*Pemb(P2),Peny(P1)*Peny(P2))
def DivPB(P1,P2) :
  return MakeP(Pemb(P1)*Peny(P2),Pemb(P2)*Peny(P1))
def AddP(P1,P2) :
  return KonversiCampuran(AddPB(KonversiPecahan(P1),KonversiPecahan(P2)))
def SubP(P1,P2) :
  return KonversiCampuran(SubPB(KonversiPecahan(P1),KonversiPecahan(P2)))
def MulP(P1,P2) :
  return KonversiCampuran(MulPB(KonversiPecahan(P1),KonversiPecahan(P2)))
def DivP(P1,P2) :
  return KonversiCampuran(DivPB(KonversiPecahan(P1),KonversiPecahan(P2)))

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEqP? : 2 Pecahan campuran --> Boolean
#   {IsEqP?(P1,P2) true jika P1 = P2. Membandingkan dua buah pecahan campuran apakah P1 sama nilainya dengan P2}
# IsLtP? : 2 Pecahan campuran --> Boolean
#   {IsLtP?(P1,P2) true jika P1<P2. Membandingkan dua buah pecahan campuran apakah P1 lebih kecil nilainya dari P2}
# IsGtP? : 2 Pecahan campuran --> Boolean
#  {IsGtP?(P1,P2) true jika P1>P2. Membandingkan dua buah pecahan campuran apakah P1 lebih besar nilainya dari P2}
# REALISASI
def IsEqP(P1,P2) :
  return KonversiReal(P1) == KonversiReal(P2)
def IsLtP(P1,P2) :
   return KonversiReal(P1) < KonversiReal(P2)
def IsGtP(P1,P2) :
   return KonversiReal(P1) > KonversiReal(P2)

# APLIKASI
print(KonversiPecahan(MakePC(1,1,2)))
print(KonversiPecahan(MakePC(-2,1,3)))
print(KonversiReal(MakePC(3,2,4)))
print(KonversiReal(MakePC(-1,1,5)))
print(AddP(MakePC(4,1,2),MakePC(2,1,4)))
print(KonversiReal(AddP(MakePC(4,1,2),MakePC(-2,1,4))))
print(SubP(MakePC(4,1,2),MakePC(2,1,4)))
print(KonversiReal(SubP(MakePC(4,1,2),MakePC(-2,1,4))))
print(MulP(MakePC(4,1,2),MakePC(2,1,4)))
print(KonversiReal(MulP(MakePC(4,1,2),MakePC(-2,1,4))))
print(DivP(MakePC(4,1,2),MakePC(2,1,4)))
print(KonversiReal(DivP(MakePC(4,1,2),MakePC(2,1,4))))
print(IsEqP(MakePC(1,1,8),MakePC(1,1,8)))
print(IsLtP(MakePC(1,3,4),MakePC(2,2,6)))
print(IsGtP(MakePC(5,3,4),MakePC(4,2,2)))