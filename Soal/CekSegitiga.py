a = int(input())
b = int(input())
c = int(input())

def segitiga():
  if c**2 < a**2 + b**2 :
    return "Segitiga Lancip"
  elif c**2 > a**2 + b**2 :
    return "Segitiga Tumpul"
  else :
    return "Segitiga Siku-Siku"

print(segitiga())