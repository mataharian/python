# Nama file : UpahMingguan2.py
# Pembuat : Dzu Sunan Muhammad - 24060122120034
# Tanggal : 16 September 2022
# Deskripkisi : Menghitung gaji seorang karyawan berdasarkan golongannya.

# Definisi dan Spesifikasi
# UpahMingguan2 : 1<=Integer<=4, 0<=Real<=168 --> Real
#   {UpahMingguan2 (Gol,jam) Menghitung upah suatu karyawan dalam 1 minggu dengan jam kerja maksimal 40 jam dan upah normal per jamnya serta upah lemburnya tergantung pada golongannya karyawan tersebut, jika lebih dari 40 jam maka dianggap sebagai lembur dan upah lembur dua kali lipat dari upah normal, golongan 1 = golongan A, golongan 2 = golongan B, golongan 3 = golongan C, dan golongan 4 = golongan D}

# Realisasi
def UpahMingguan2 (Golongan,jam) :
  if Golongan == 1 :
    if 0<=jam<=40 :
      return jam*40000
    elif 40<jam<=168 :
      return 40*40000+(jam-40)*40000*2
  elif Golongan == 2 :
    if 0<=jam<=40 :
      return jam*50000
    elif 40<jam<=168 :
      return 40*50000+(jam-40)*50000*2
  elif Golongan == 3 :
    if 0<=jam<=40 :
      return jam*60000
    elif 40<jam<=168 :
      return 40*60000+(jam-40)*60000*2
  elif Golongan == 4 :
    if 0<=jam<=40 :
      return jam*70000
    elif 40<jam<=168 :
      return 40*70000+(jam-40)*70000*2

# Aplikasi 
print(UpahMingguan2(1,23))
print(UpahMingguan2(1,42))
print(UpahMingguan2(2,40))
print(UpahMingguan2(2,61))
print(UpahMingguan2(3,24))
print(UpahMingguan2(3,128))
print(UpahMingguan2(4,12))
print(UpahMingguan2(4,88))