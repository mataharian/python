def IsMember(x,L) :
  if L == [] :
    return False
  else :
    head,*tail = L
    if (L[0] == x) :
      return True
    else :
      return IsMember(x, tail)

L = [0,1,2,3,4,5,6,7]
x = int(input())
print(IsMember(x,L))