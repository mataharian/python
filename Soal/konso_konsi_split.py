def konso (inp,lst) :
  if lst == [] :
    return [inp]
  else :
    return [inp] + lst

def konsi (inp,lst) :
  if inp == [] :
    return [inp]
  else :
    return lst + [inp]

statement = input()
s = input()
input_list_awal = input()
J = input_list_awal.split()

if statement == "konso" :
  print(konso(s,J))
elif statement == "konsi" :
  print(konsi(s,J))
else :
  print ("wrong input")