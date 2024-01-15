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

def kartu(L) :
  if IsEmpty(L) :
    return 0
  else :
    if IsAtom(FirstList(L)) :
      return 1 + kartu(TailList(L))
    elif IsList(FirstList(L)) :
      return kartu(Ubah(TailList(L),FirstList(L)))

list_of_list = ast.literal_eval(input())
print(kartu(list_of_list))