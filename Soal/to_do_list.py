Kegiatan = []
Banyak_Kegiatan = int(input())
for i in range (Banyak_Kegiatan) :
  list = str(input())
  Kegiatan.append(list)

def ToDoList(x,L) :
  if x <= 0 :
    return "Tobi tidak ingin bermalas-malsan!"
  elif x > 50 :
    return "Tobi tidak bisa bekerja terlalu keras"
  else :
    if x == 1:
      return L
    else :
      return ToDoList(x-1,L)

print(ToDoList(Banyak_Kegiatan,Kegiatan))