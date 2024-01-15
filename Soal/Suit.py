a = int(input())
b = int(input())
c = int(input())

def Suit():
  total=a+b+c
  if total % 2 == 0 :
    return "Budi"
  else :
    return "Dani"

print(Suit())