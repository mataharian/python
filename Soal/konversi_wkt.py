# Nama file : konversiwaktu.py 
# Pembuat : Dzu Sunan Muhammad - 24060122120034
# Tanggal : 1 September 2022
# Deskripkisi : Mengkonversi sebuah waktu ke dalam satuan detik

# Definisi dan Spesifikasi
# Wt : integer, integer, integer --> integer
#   {Wt (x,y,z) mengkonversikan x sebagai jam dengan 0<=x<=24, y sebagai menit dengan 0<=y<60, dan z sebagai detik dengan 0<=Z<60 ke dalam detik}

#Realisasi
def Wt (x,y,z) :
  return (x*3600+y*60+z)

# Aplikasi
Wt(14,7,35)
Wt(15,41,54)
Wt(16,15,2)

print(Wt(14,7,35))
print(Wt(15,41,54))
print(Wt(16,15,2))