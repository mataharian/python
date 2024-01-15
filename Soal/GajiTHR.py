# Nama file : GajiTHR.py
# Pembuat : Dzu Sunan Muhammad - 24060122120034
# Tanggal : 16 September 2022
# Deskripkisi : Menghitung thr dan gaji seorang karyawan berdasarkan gaji dari golongannya.

# Definisi dan Spesfikasi
# GajiTHR : 1<=Integer<=4, Real>0 --> Real
#   {GajiTHR (Golongan,JamKerja) Menhitung gaji dan thr seorang karyawan berdasarkan dari gaji golongannya, golongan 1 = golongan A, golongan 2 = golongan B, golongan 3 = golongan C, dan golongan 4 = golongan D.}

# Realisasi
def GajiTHR (Golongan,MasaKerja) :
  if Golongan == 1 :
    if MasaKerja < 1 :
      return 300+300*5/100
    elif 1 <= MasaKerja < 5 :
      return 320+320*5/100
    elif 5 <= MasaKerja < 10 :
      return 350+350*5/100 
    elif MasaKerja >= 10 :
      return 375+375*5/100 
  elif Golongan == 2 :
    if MasaKerja < 1 :
      return 400+400*10/100
    elif 1 <= MasaKerja < 5 :
      return 425+425*10/100
    elif 5 <= MasaKerja < 10 :
      return 450+450*10/100
    elif MasaKerja >= 10 :
      return 480+480*10/100
  elif Golongan == 3 :
    if MasaKerja < 1 :
      return 500+500*15/100
    elif 1 <= MasaKerja < 5 :
      return 525+525*15/100
    elif 5 <= MasaKerja < 10 :
      return 560+560*15/100
    elif MasaKerja >= 10 :
      return 590+590*15/100
  elif Golongan == 4 :
    if MasaKerja < 1 :
      return 600+600*20/100
    elif 1 <= MasaKerja < 5 :
      return 630+630*20/100
    elif 5 <= MasaKerja < 10 :
      return 660+660*20/100
    elif MasaKerja >= 10 :
      return 700+700*20/100

print(GajiTHR(1,0.5))
print(GajiTHR(1,3))
print(GajiTHR(1,7))
print(GajiTHR(1,15))
print(GajiTHR(2,0.1))
print(GajiTHR(2,4))
print(GajiTHR(2,5))
print(GajiTHR(2,20))
print(GajiTHR(3,0.7))
print(GajiTHR(3,2))
print(GajiTHR(3,8))
print(GajiTHR(3,10))
print(GajiTHR(4,0.2))
print(GajiTHR(4,1))
print(GajiTHR(4,9))
print(GajiTHR(4,13))