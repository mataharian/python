# Nama file : NextDay.py
# Pembuat : Dzu Sunan Muhammad - 24060122120034
# Tanggal : 16 September 2022
# Deskripkisi : Menyatakan hari, bulan, tahun pada 1 hari berikutnya dari tanggal tersebut.

# Definisi dan Spesifikasi
# NextDay :  1<=Integer<=31, 1<=Integer<=12, integer --> 1<=Integer<=31, 1<=Integer<=12, integer
#   {NextDay (hari,bulan,tahun)  Menerima suatu input hari, bulan, tahun yang menyatakan suatu tanggal dan menghasilkan output hari, bulan, tahun setelah 1 hari berikutnya dari hari tersebut.}

# Realisasi
def NextDay (hari,bulan,tahun) :
  if bulan == 1 :
    if hari+1 <= 31 :
      return hari+1,bulan,tahun
    elif hari+1 == 32 :
      return 1,bulan+1,tahun

  elif bulan == 2 :
    if ((tahun%400==0) or (tahun%4==0) and (tahun%100!=0)) :
      if hari+1 <= 29 :
        return hari+1,bulan,tahun
      elif hari+1 == 30 :
        return 1,bulan+1,tahun
    elif hari+1 <= 28 :
      return hari+1,bulan,tahun
    elif  hari+1 == 29 :
      return 1,bulan+1,tahun

  elif bulan == 3 :
    if hari+1 <= 31 :
      return hari+1,bulan,tahun
    elif hari+1 == 32 :
      return 1,bulan+1,tahun

  elif bulan == 4 :
    if hari+1 <= 30 :
      return hari+1,bulan,tahun
    elif hari+1 == 31 :
      return 1,bulan+1,tahun

  elif bulan == 5 :
    if hari+1 <= 31 :
      return hari+1,bulan,tahun
    elif hari+1 == 32 :
      return 1,bulan+1,tahun

  elif bulan == 6 :
    if hari+1 <= 30 :
      return hari+1,bulan,tahun
    elif hari+1 == 31 :
      return 1,bulan+1,tahun

  elif bulan == 7 :
    if hari+1 <= 31 :
      return hari+1,bulan,tahun
    elif hari+1 == 32 :
      return 1,bulan+1,tahun

  elif bulan == 8 :
    if hari+1 <= 31 :
      return hari+1,bulan,tahun
    elif hari+1 == 32 :
      return 1,bulan+1,tahun

  elif bulan == 9 :
    if hari+1 <= 30 :
      return hari+1,bulan,tahun
    elif hari+1 == 31 :
      return 1,bulan+1,tahun

  elif bulan == 10 :
    if hari+1 <= 31 :
      return hari+1,bulan,tahun
    elif hari+1 == 32 :
      return 1,bulan+1,tahun

  elif bulan == 11 :
    if hari+1 <= 30 :
      return hari+1,bulan,tahun
    elif hari+1 == 31 :
      return 1,bulan+1,tahun

  elif bulan == 12 :
    if hari+1 <= 31 :
      return hari+1,bulan,tahun
    elif hari+1 == 32 :
      return 1,1,tahun+1

print(NextDay(23,5,2022))
print(NextDay(29,2,2024))
print(NextDay(15,2,2024))
print(NextDay(28,2,2003))
print(NextDay(31,12,2012))