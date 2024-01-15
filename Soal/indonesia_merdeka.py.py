def IsEmpty(S) :
  return S == []

def FirstList(S) :
  if not IsEmpty(S) :
    return S[0]

def TailList(S) :
  if not IsEmpty(S) :
    return S[1:]

def NbElement(S):
    if IsEmpty(S):
        return 0
    else:
        return 1 + NbElement(TailList(S))

def IsAtom(S) :
  if IsList(S):
    return NbElement(S) == 1
  else :
    return True

def IsList(S) :
  if type(S) == list :
    return True
  else :
    return False

def Max2(a,b) :
  if a > b :
    return a
  else :
    return b

def IsOneElement(L):
    if IsEmpty(L):
        return False
    elif NbElement(L) == 1:
        return True
    else:
        return False

def Max(S) :
  if IsOneElement(S) :
    if IsAtom(FirstList(S)) :
      return FirstList(S)
    else :
      return Max(FirstList(S))
  else :
    if IsAtom(FirstList(S)) :
      return Max2(FirstList(S), Max(TailList(S)))
    else:
      return Max2(Max(FirstList(S)), Max(TailList(S)))

def biaya(LOL,prajurit,ninja) :
  if len(LOL) == 0 :
    return (prajurit+ninja)*1000000
  elif IsAtom(FirstList(LOL)) :
    return biaya(TailList(LOL), Max2(FirstList(LOL),prajurit),ninja)
  elif IsList(FirstList(LOL)) :
    return biaya(TailList(LOL),prajurit,ninja + Max(FirstList(LOL)))

print(biaya([[2,3,4,6],[1,1,3,9,2,7],3,1,[2,1],7,2,[4,4,6],1,[3,3]],0,0))