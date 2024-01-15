 # Nama file : NextTime.py
# Pembuat : Dzu Sunan Muhammad - 24060122120034
# Tanggal : 16 September 2022
# Deskripkisi : Menyatakan jam, menit, detik setelah 1 detik berikutnya dari waktu tersebut.

# Definisi dan Spesifikasi
# NextTime : 0<=Integer<=24, 0<=Integer<=60, 0<=Integer<=60 --> 0<=Integer<=24, 0<=Integer<=60, 0<=Integer<=60
#   {NextTime (jam,menit,detik) Menerima suatu input jam, menit, detik yang menyatakan suatu waktu dan menghasilkan output jam, menit, detik setelah 1 detik berikutnya dari waktu tersebut}

# Realisasi
def NextTime (jam,menit,detik) :
  if 0<=jam+1<24 and 0<=menit+1<60 and detik+1==60 :
    return jam,menit+1,0
  elif 0<=jam+1<24 and menit+1==60 and detik+1==60 :
    return jam+1,0,0
  elif jam+1==24 and menit+1==60 and detik+1==60 :
    return 0,0,0
  else :
    return jam,menit,detik+1

# Aplikasi
print(NextTime(5,41,29))
print(NextTime(12,34,59))
print(NextTime(10,59,28))
print(NextTime(15,59,59))
print(NextTime(23,59,59))