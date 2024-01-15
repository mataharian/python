# Nama file : IsVocal.py
# Pembuat : Dzu Sunan Muhammad - 24060122120034
# Tanggal : 16 September 2022
# Deskripkisi : Menentukan suatu karakter merupakan huruf vokal atau bukan.

# Definisi dan Spesifikasi
# IsVocal : Character --> Boolean
#   {IsVocal (Vcl) menentukan sebuah karakter merupakan sebuah huruf vocal atau bukan jika benar akan menghasilkan keluaran true dan jika bukan akan menghasilkan keluaran false.}

# Realisasi
def IsVocal(Vcl) :
  if Vcl=='a' or Vcl=='i' or Vcl=='u' or Vcl=='e' or Vcl=='o' :
    return "True"
  else :
    return "False"

# Aplikasi
print(IsVocal('a'))
print(IsVocal('i'))
print(IsVocal('u'))
print(IsVocal('e'))
print(IsVocal('o'))
print(IsVocal('A'))
print(IsVocal('s'))