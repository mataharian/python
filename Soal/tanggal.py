# DEFINISI DAN SPESIFIKASI TYPE
# type Hr : integer [1...31]
#   {definisi ini hanyalah untuk “menamakan” type integer dengan nilai tertentu supaya
#   mewakili hari, sehingga jika dipunyai suatu nilai integer, kita dapat memeriksa apakah
#   nilai integer tersebut mewakili Hari yang absah }
# type Bln : integer [1...12]
#   {definisi ini hanyalah untuk “menamakan” type integer dengan daerah nilai tertentu
#   supaya mewakili Bulan }
# type Thn : integer > 0
#   {definisi ini hanyalah untuk “menamakan“ type integer dengan daerah nilai tertentu
#   supaya mewakili tahun }
# type date <d: Hr, m:Bln,y:Thn>
#   { <d,m,y> adalah tanggal d bulan m tahun y }

# Definisi dan Spesifikasi Konstuktor
# MakeDate : <Hr,Bln,Thn> --> date
#   {MakeDate<h,b,t>-> tgl pada hari,bulan,tahun yang bersangkutan}
# REALISASI
def MakeDate (Hr,Bln,Thn) :
  return [Hr,Bln,Thn]

# DEFINISI DAN SPESIFIKASI SELEKTOR
# Day : date --> Hr
#   {Day (D) memberikan hari d dari D yang terdiri dari <d,m,y> } 
# REALISASI
def Day(D) :
  if 0<D<=31 :
    return D[0]
def Month (D) :
  if 0<D<=12 : 
    return D[1]
def Year(D) :
  if D>0 : 
    return D[2]

# DEFINISI DAN SPESIFIKASI OPERATOR/FUNGSI LAIN TERHADAP DATE
# Nextday : date --> date
#  {NextDay(D): menghitung date yang merupakan keesokan hari dari date D yang diberikan}
# REALISASI
def Nextday(D) :
  if Month(D) == 1 or Month(D) == 3 or Month (D) == 5 or Month(D) == 7 or Month(D) == 8 or Month (D) == 10 :
    if Day(D)<31 :
      return MakeDate(Day(D)+1,Month(D),Year(D))
    elif Day(D)==31 :
      return MakeDate(1,Month(D)+1,Year(D))
  if Month(D) == 4 or Month(D) == 6 or Month (D) == 9 or Month(D) == 11 :
    if Day(D)<30 :
      return MakeDate(Day(D)+1,Month(D),Year(D))
    elif Day(D)==30 :
      return MakeDate(1,Month(D)+1,Year(D))
  if Month(D) == 2 :
    if IsKabisat(D) == True :
      if Day