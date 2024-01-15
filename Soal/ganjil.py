import ast

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

def Ubah(L,S) :
  return L + S

def Ganjil(S) :
  if S == [] :
    return 0
  else :
    if IsList(FirstList(S)) :
      return Ganjil(Ubah(TailList(S),FirstList(S)))
    else :
      if FirstList(S) % 2 != 0 :
        return FirstList(S) + Ganjil(TailList(S))
      else :
        return Ganjil(TailList(S))

print(Ganjil([1,2,[3,4],[5,[6,7]],8]))