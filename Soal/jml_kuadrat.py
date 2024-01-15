# Nama file : Menghitungkuadrat.py 
# Pembuat : Dzu Sunan Muhammad - 24060122120034
# Tanggal : 1 September 2022
# Deskripkisi : Menhitung penjumlahan kuadrat dari akar-akar persamaan kuadrat

# Definisi dan Spesifikasi
# fx : Real, Real, Real --> Real
#   {fx (a,b,c) menghitung jumlahan kuadrat dari akar-akar persamaan kuadrat (x1**2 + x2**2) dari persamaan ax**2 + bx + c = 0}

# Realisasi
def fx(a,b,c):
  return ((-b/a)**2-2*c/a)

#Aplikasi
fx(1,-8,15)
fx(2,12,8)
fx(1,-9,18)

print(fx(1,-8,15))
print(fx(2,12,8))
print(fx(1,-9,18))