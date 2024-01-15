# Nama file : data_ipk_mhsw.py 
# Pembuat : Dzu Sunan Muhammad - 24060122120034
# Tanggal : 1 September 2022
# Deskripkisi : Mengecek IPK mahasiswa apakah mahasiswa tersebut cumlaude atau tidak

# Definisi dan Spesifikasi
# ms : integer --> real
#   {ms (bulan) menrubah satuan tahun ke dalam satuan bulan}
# cum : real, real --> Boolean
#   {cum (ms,ipk) menentukan apakah mahasiswa cumlaude atau tidak berdasarkan masa studi yang diwakilkan dengan ms dalam satuan bulan dan ms <= 4.5, serta berdasarkan ipk dengan ipk >= 3.5. Apabila true maka mahasiswa cumlaude, dan apabila false maka mahasiswa tidak cumlaude }

# Realisasi
def ms (bulan) :
  return bulan/12

def cum (ms,ipk) :
  return ms<=4.5 and ipk>=3.5
  

#Aplikasi
cum(ms(60), 3.6)
cum(ms(48), 3.5)
cum(ms(54), 4.0)
cum(ms(42), 2.9)

print(cum(ms(60), 3.6))
print(cum(ms(48), 3.5))
print(cum(ms(54), 4.0))
print(cum(ms(42), 2.9))