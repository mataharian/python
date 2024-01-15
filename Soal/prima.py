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

def IsPrima(n,i=2) :
  if n < 2 :
    return False
  elif n == 2 :
    return True
  elif n % i == 0 :
    return False
  elif i*i > n :
    return True
  else :
    return IsPrima(n,i+1)

def Prima(S) :
  if S == [] :
    return 0
  else :
    if IsList(FirstList(S)) :
      return Prima(Ubah(TailList(S),FirstList(S)))
    else :
      if IsPrima(FirstList(S)) :
        return FirstList(S) + Prima(TailList(S))
      else :
        return Prima(TailList(S))
      
list_of_list = ast.literal_eval(input())
print(Prima(list_of_list))