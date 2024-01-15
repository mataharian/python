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

def SumElement(L):
    if IsEmpty(L):
        return 0
    else:
        return FirstList(L) + SumElement(TailList(L))

def Permen(S) :
  if S == [] :
    return 0
  else :
    if IsAtom(FirstList(S)) :
      if FirstList(S) % 2 != 0 :
        return (FirstList(S)*3000) + Permen(TailList(S))
      elif FirstList(S) % 2 == 0 :
        return (FirstList(S)*4000) + Permen(TailList(S))
    else :
      if SumElement(FirstList(S)) % 2 == 0 :
        return SumElement(FirstList(S))*2000 + Permen(TailList(S))
      elif SumElement(FirstList(S)) % 2 != 0 :
        return SumElement(FirstList(S))*1000 + Permen(TailList(S))
      

list_of_list = ast.literal_eval(input())
print(Permen(list_of_list))