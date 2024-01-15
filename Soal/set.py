def isEmpty(L) :
  return L == []

def FirstElement(L) :
  if not isEmpty(L) :
    return L[0]

def Tail(L) :
  if not isEmpty(L) :
    return L[1:]

def isMember(x,L) :
  if isEmpty(L) :
    return False
  else :
    if FirstElement(L) == x :
      return True
    else :
      return isMember(x,Tail(L))

def konso (inp,lst) :
  if lst == [] :
    return [inp]
  else :
    return [inp] + lst

def make_set(lst) :
  if isEmpty(lst) :
    return lst
  else :
    if isMember(Tail(lst),FirstElement(lst)) :
      return make_set(Tail(lst))
    else :
      return konso(FirstElement(lst),make_set(Tail(lst)))

lst1 = [1,1,1,1,2,2,2,3,3,3,4]
lst3 = make_set(lst1)
print(make_set(lst3))