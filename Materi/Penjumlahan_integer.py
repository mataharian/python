def plus(x,y) :
  if y == 0 : #basis 0
    return x
  else : #rekurens
    return 1+plus(x,y-1)

print(plus(4,0))
print(plus(4,1))
print(plus(5,2))