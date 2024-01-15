# Nama file : DayInMonth.py
# Pembuat : Dzu Sunan Muhammad - 24060122120034
# Tanggal : 16 September 2022
# Deskripkisi : Menghitung jumlah hari dalam sebulan.

# Definisi dan Spesifikasi
# DayInMonth : 1<=Integer<=12, integer --> 1<=Integer<=31
#   {DayInMonth (bulan,tahun) Menghitung jumlah hari dalam sebulan dengan memperhatikan tahun tersebut merupakan kabisat atau bukan.}

# Realisasi
def DayInMonth (bulan,tahun) :
    if bulan == 1 :
        return 31
    elif bulan == 2:
        if ((tahun%400==0) or (tahun%4==0) and (tahun%100!=0)) :
          return 29
        else :
          return 28
    elif bulan == 3:
        return 31
    elif bulan== 4:
        return 30
    elif bulan == 5:
        return 31
    elif bulan == 6:
        return 30
    elif bulan ==7:
        return 31
    elif bulan == 8:
        return 31
    elif bulan == 9:
        return 30
    elif bulan == 10:
        return 31
    elif bulan == 11:
        return 30
    elif bulan == 12:
        return 31

# Aplikasi
print(DayInMonth(2,2004))
print(DayInMonth(2,1995))
print(DayInMonth(6,2004))
print(DayInMonth(12,2019))