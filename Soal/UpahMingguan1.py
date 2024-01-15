# Nama file : UpahMingguan1.py
# Pembuat : Dzu Sunan Muhammad - 24060122120034
# Tanggal : 16 September 2022
# Deskripkisi : Menghitung upah karyawan suatu perusahaan.

# Definisi dan Spesifikasi
# UpahMingguan1 : 0<=Real<=168 --> Real
#   {UpahMingguan1 (jam) Menghitung upah suatu karyawan dalam 1 minggu dengan jam kerja maksimal 48 jam, jika lebih dari 48 jam maka dianggap sebagai lembur dan upah lembur dua kali lipat dari upah normal.}

# Realisasi
def UpahMingguan1 (jam) :
  if 0<=jam<=48 :
    return jam*20000
  elif 48<jam<=168 :
    return 48*20000+(jam-48)*20000*2

# Aplikasi
print(UpahMingguan1(40))
print(UpahMingguan1(128))