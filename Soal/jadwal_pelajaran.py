s = str(input())
n = float(input())

sen = ["0","0","0","0","0","0","0","Matematika Peminatan","0","Fisika","0","0","Kimia","Biologi"]
sel = ["0","0","0","0","0","0","0","Olahraga","0","Agama","0","0","PKN","Sejarah"]
rab = ["0","0","0","0","0","0","0","Seni Budaya","0","Bahasa Indonesia","0","0","Bahasa Inggris","Matematika Wajib"]

if s == "Senin" :
  print(sen[int(n)])
elif s == "Selasa" :
  print(sel[int(n)])
elif s == "Rabu" :
  print(rab[int(n)])
else :
  print("Tidak ada jadwal")