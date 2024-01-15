# Nama file : WujudAir.py
# Pembuat : Dzu Sunan Muhammad - 24060122120034
# Tanggal : 16 September 2022
# Deskripkisi : Menentukan wujud air

# Definisi dan Spesifikasi
# WujudAir : Real --> String
#   {WujudAir (x) Menentukan wujud air apakah merupakan bentuk padat, cair, atau uap berdasarkan temperatur air dalam derajat celcius, x merupakan derajat air dalam celcius.}

# Realisasi
def WujudAir (x) :
  if x > 0 :
    if x < 100 :
      return "Cair"
    else :
      return "Uap"
  else :
    return "Padat"

# Aplikasi
print(WujudAir(-10))
print(WujudAir(120))
print(WujudAir(50.7))