# Library
def IsEmpty(S) :
  return S == []

def FirstList(S) :
  if not IsEmpty(S) :
    return S[0]

def TailList(S) :
  if not IsEmpty(S) :
    return S[1:]

def LastList(L) :
  if not IsEmpty(L) :
    return L[-1]

def HeadList(L) :
  if not IsEmpty(L) :
    return L[:-1]

def NbElement(S):
    if IsEmpty(S):
        return 0
    else:
        return 1 + NbElement(TailList(S))

def IsMember(e,S) :
  if IsEmpty(S) :
    return False
  else :
    if FirstList(S) == e :
      return True
    else :
      return IsMember(e,TailList(S))

def IsOneElement(L):
    if IsEmpty(L):
        return False
    elif NbElement(L) == 1:
        return True
    else:
        return False

#--------------------------------------------!!!------------------------------------------#

# IsList : List of Lists --> Boolean
#   {IsList(S) Benar jika list of list S adalah sebuah list atau bukan atom}
def IsList(S) :
  if type(S) == list :
    return True
  else :
    return False

print()
print("IsList :")
print(IsList([1,2,3,[6,7],4,5])) # 1,2,3,4,5 --> Atom

#--------------------------------------------!!!------------------------------------------#

# IsAtom : List of List --> Boolean
#   {IsAtom(S) Benar jika sebuah list adalah atom, yaitu list yang terdiri dari satu buah elements}
def IsAtom(S) :
  if IsList(S):
    return NbElement(S) == 1
  else :
    return True

print()
print("IsAtom :")
print(IsAtom([1,2])) # False

#--------------------------------------------!!!------------------------------------------#

# KonsLo : List, List of List --> List of List
#   {KonsLo(L,S) Membentuk sebuah list baru dari list L dan list of list S dengan list L sebagai element pertaman dari list of list S}
def KonsLo(L,S) :
  return [L] + S

print()
print("KonsLo :")
print(KonsLo(10,[4,[5,6],7]))

#--------------------------------------------!!!------------------------------------------#

# KonsL : List, List of List --> List of List
#   {KonsL(L,S) Membentuk sebuah list baru dari list L dan list of list S dengan list L sebagai element terakhir dari list of list S}
def KonsL(L,S) :
  return S + [L]

print()
print("KonsL :")
print(KonsL([1,2,3],[4,5,6,7]))

#--------------------------------------------!!!------------------------------------------#

# IsEqualS : 2 List of List --> Boolean
#   {IsEqualS(S1,S2) Benar jika S1 identik dengan S2, yaitu semua elementnya sama dengan memperhatikan urutannya}
def IsEqualS(S1,S2) :
  if IsEmpty(S1) and IsEmpty(S2) :
    return True
  elif IsEmpty(S1) or IsEmpty(S2) :
    return False
  else :
    if IsAtom(FirstList(S1)) and IsAtom(FirstList(S2)) :
      return FirstList(S1) == FirstList(S2) and IsEqualS(TailList(S1),TailList(S2))
    elif IsList(FirstList(S1)) and IsList(FirstList(S2)) :
      return IsEqualS(FirstList(S1),FirstList(S2)) and IsEqualS(TailList(S1),TailList(S2))
    else :
      return False

print()
print("IsEqualS :")
print(IsEqualS([1,2,3,4,5],[1,[2,3],4,5])) # False

#--------------------------------------------!!!------------------------------------------#

# IsMemberS : Element, List of List --> Boolean
#   {IsMemberS(e,S) Benar jika e merupakan element dari sebuah list S}

def IsMemberS(e,S) :
  if IsEmpty(S) :
    return False
  else :
    if IsAtom(FirstList(S)) : 
      return e == FirstList(S) or IsMemberS(e,TailList(S))
    elif IsList(FirstList(S)) :
      return IsMember(e,FirstList(S)) or IsMemberS(e,TailList(S))
    else :
      return False

print()
print("IsMemberS :")
print(IsMemberS(3,[1,2,[3,4],5])) # True

#--------------------------------------------!!!------------------------------------------#

# IsMemberList : List, List of List --> Boolean
#   {IsMemberList(L,S) Benar jika list L merupakan anggota dari list of list S}
#   {Basis : L dan S list kosong --> True}
#   {Basis : L atau S list tidak kosong --> True}
def IsMemberList(L,S) :
  if IsEmpty(L) and IsEmpty(S) :
    return True
  elif IsEmpty(L) or IsEmpty(S) :
    return False
  else :
    if IsAtom(FirstList(S)) :
      return IsMemberList(L,TailList(S))
    else :
      if IsEqualS(L,FirstList(S)) :
        return True
      else :
        return IsMemberList(L,TailList(S))

print()
print("IsMemberList :")
print(IsMemberList([3],[1,2,[3,4],5])) # False

#--------------------------------------------!!!------------------------------------------#

# Rember : element, List of list --> List of List
#   {Rember(e,S) Menghapus sebuah element bernilai e dari semua list S}
def Rember(e,S) :
  if IsEmpty(S) :
    return S
  else :
    if IsList(FirstList(S)) :
      return KonsLo(Rember(e,FirstList(S)),Rember(e,TailList(S)))
    else :
      if e == FirstList(S) :
        return Rember(e,TailList(S))
      else :
        return KonsLo(FirstList(S),Rember(e,TailList(S)))

print()
print("Rember :")
print(Rember(3,[1,2,3,[3,4],5])) # [1,2,[4],5]

#--------------------------------------------!!!------------------------------------------#

# Max2 : 2 Integer --> Integer
#   {Max2(a,b) Menghasilkan nilai maksimum a dan b}
def Max2(a,b) :
  print(a,b)
  if a > b :
    return a
  else :
    return b

# Max : List of List tidak kosong --> Integer
#   {Max(S) Menghasilkan nilai element (atom) maksimum dari list of list S}
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

print()
print("Max :")
print(Max([2,6,[9,4],3,1]))