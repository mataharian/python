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

def KonsLo(L,S) :
  return [L] + S

def Monster(X,S) :
  if S == [] :
    return S
  else :
    if IsList(FirstList(S)) :
      return KonsLo(Monster(X,FirstList(S)),Monster(X,TailList(S)))
    else :
      if FirstList(S) % X == 0 :
        return Monster(X,TailList(S))
      else :
        return KonsLo(FirstList(S),Monster(X,TailList(S)))

list_of_list = ast.literal_eval(input())
inp = int(input())

print(Monster(inp,list_of_list))