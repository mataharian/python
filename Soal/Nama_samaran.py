nama = input()
nama1,nama2 = nama.split()

def nama_depan1(x) : #Nama Depan First Element
  return x[0]

def nama_depan2(x) : #Nama Depan Tail
  return x[1:]

def nama_blkng1(x) : #Nama Belakang First Element
  return x[0]

def nama_blkng2(x) : #Nama Belakang Tail
  return x[1:]

print(nama_blkng1(nama2)+nama_depan2(nama1)+" "+nama_depan1(nama1)+nama_blkng2(nama2))