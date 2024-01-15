def IsEmpty(L):
    if L==[]:
        return True
    else:
        return False

def FirstElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return L[0]

def tail(L):
    if IsEmpty(L):
        return 0
    else:
        return L[1:]

def IsMember(x,L):
    if IsEmpty(L):
        return False
    else:
        if(FirstElmt(L)==x):
            return True
        else:
            return IsMember(x,tail(L))

def Konso(E,L):
    if E==[]:
        return L
    elif L==[]:
        return [E]
    else:
        return [E]+L  

def make_set(L) :
  if IsEmpty(L) :
    return L
  else :
    if IsMember(tail(L),FirstElmt(L)) :
      return make_set(tail(L))
    else :
      return Konso(FirstElmt(L),make_set(tail(L)))

def Is_Set(L) :
  if IsEmpty(L) :
    return True
  else :
    if IsMember(tail(L),FirstElmt(L)) :
      return False
    else :
      return Is_Set(tail(L))

def is_subset(H1,H2) :
  if IsEmpty(H1) :
    return True
  else :
    if not (IsMember(H2,FirstElmt(H1))) :
      return False
    else :
      return is_subset(tail(H1),H2)

L3=[1,2,3,4,5]
L4=[1,2,3]
print(is_subset(L4,L3))
print(is_subset(L3,L4))

def is_eq_set(H1,H2) :
  return is_subset(H1,H2) and is_subset(H2,H1)