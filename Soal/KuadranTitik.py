# Nama file : KuadranTitik.py
# Pembuat : Dzu Sunan Muhammad - 24060122120034
# Tanggal : 16 September 2022
# Deskripkisi : Menentukan kuadran suatu koordinat titik.

# Definisi dan Spesifikasi
# KuadranTitik : 2 Real --> String
#   {KuadranTitik (x,y) Menentukan letak kuadran suatu koordinat titik dalam koordinat cartecian.}

# Realisasi
def KuadranTitik (x,y) :
  if (x>0) and (y>0) :
    return "Kuadran I"
  elif (x<0) and (y>0) :
    return "Kuadran II"
  elif (x<0) and (y<0) :
    return "Kuadran III"
  elif (x>0) and (y<0) :
    return "Kuadran IV"

# Aplikasi
print (KuadranTitik(7,15))
print (KuadranTitik(-4,2))
print (KuadranTitik(-9,-9))
print (KuadranTitik(3,-5))