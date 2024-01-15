A = [0,1,2,3]
s = 10

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

p = input("")
if p == "konso(s,A)" :
  print(konso(s,A))
elif p == "konsi(s,A)" :
  print(konsi(s,A))
else :
  print ("wrong input")