a = int(input())
inp = list(map(int, input().split(' ')))
inp.sort()

def List_Terbesar(x) :
  return x[-1]

def List_Terkecil(x) :
  return x[0]

def seleksi_akatsuki(x,input) :
  if x > List_Terbesar(input) :
    return 0
  elif x <= List_Terkecil(input) :
    return len(input)
  elif x <= List_Terbesar(input) :
    return 1 + seleksi_akatsuki(x,input[:-1])

print(seleksi_akatsuki(a,inp))