# Library
def IsEmpty(L) :
  return L == []

def FirstElement(L) :
  if not IsEmpty(L) :
    return L[0]

def Tail(L) :
  if not IsEmpty(L) :
    return L[1:]

def IsMember(x,L) :
  if IsEmpty(L) : # Basis
    return False
  else :
    if FirstElement(L) == x :
      return True
    else : # Rekursif
      return IsMember(x,Tail(L))

def konso (elmnt,lst) :
  if lst == [] :
    return [elmnt]
  else :
    return [elmnt] + lst


#--------------------------------------------!!!------------------------------------------#

# MakeSet : List --> set
#   {MakeSet(L) Membuat set dari sebuah list L, yaitu membuang semua kemunculan element yang lebih dari satu kali, list kosong tetap menjadi list kosong}
def MakeSet(L) :
  if IsEmpty(L) :
    return []
  else :
    if IsMember(FirstElement(L),Tail(L)) :
      return MakeSet(Tail(L))
    else :
      return konso(FirstElement(L),MakeSet(Tail(L)))

print("MakeSet :")
print(MakeSet([1,2,2,3,3,4,5])) # [1,2,3,4,5]

#--------------------------------------------!!!------------------------------------------#

# IsSet : List --> Boolean
#   {IsSet(L) Benar jika list L adalah sebuah set}
def IsSet(L) :
    if IsEmpty(L) :
        return True
    else: #rekurens
        if IsMember(FirstElement(L),Tail(L)) :
            return False
        else:
            return IsSet(Tail(L))

print()
print("IsSet :")
print(IsSet([1,2,3,4,5])) # True

#--------------------------------------------!!!------------------------------------------#

# IsSubSet : Set, Set --> Boolean
#   {IsSubSet(H1,H2) Benar jika set H1 adalah subset dari set H2 : Semua element set H1 adalah juga merupakan element set H2}
def IsSubSet(H1,H2) :
    if IsEmpty(H1) :
        return True
    else: #rekurens
        if not IsMember(FirstElement(H1),H2) :
            return False
        else:
            return IsSubSet(Tail(H1),H2)

print()
print("IsSubSet :")
print(IsSubSet([1,3,5],[1,2,3,4,5])) # True

#--------------------------------------------!!!------------------------------------------#

# MakeIntersect : Set, Set --> Set
#   {MakeIntersect(H1,H2) Membuat interseksi atau irisan dari set H1 dan set H2 : yaitu set baru dengan anggota element yang merupakan anggota yg sama dari set H1 dan juga anggota dari set H2}
def MakeIntersect(H1,H2) :
  if IsEmpty(H1) and IsEmpty(H2) :
    return []
  elif IsEmpty(H1) or IsEmpty(H2) :
    return []
  else :
        if IsMember(FirstElement(H1),H2) :
            return konso(FirstElement(H1),MakeIntersect(Tail(H1),H2))
        else:
            return MakeIntersect(Tail(H1),H2)

print() 
print("MakeIntersect :")
print(MakeIntersect([1,3,5,6,7],[1,2,3,4,5])) # [1,3,5]

#--------------------------------------------!!!------------------------------------------#

# IsIntersect : Set, Set --> Boolean
#   {IsIntersect(H1,H2) True jika H1 berinterseksi dengan H2 : minimal ada satu anggota yang sama. Himpunan kosong bukan merupakan himpunan yang berinterseksi dengan himpunan apapun}
def IsIntersect(H1,H2) :
  if IsEmpty(H1) and IsEmpty(H2) :
    return False
  elif IsEmpty(H1) or IsEmpty(H2) :
    return False
  elif (not IsEmpty(H1)) and (not IsEmpty(H2)) :
    return IsMember(FirstElement(H1),H2) or IsIntersect(Tail(H1),H2)

print()
print("IsIntersect : ")
print(IsIntersect([1,2,3,4],[5,6]))

#--------------------------------------------!!!------------------------------------------#

# MakeUnion : Set, Set --> Set
#   {MakeUniin(H1,H2) Membuat union atau gabungan dari set H1 dan set H2 : yaitu set baru dengan semua anggota dari element set H1 dan set H2}
def MakeUnion(H1,H2) :
    if IsEmpty(H1) and IsEmpty(H2) :
        return []
    elif (not IsEmpty(H1)) and IsEmpty(H2) :
        return H1
    elif IsEmpty(H1) and (not IsEmpty(H2)) :
        return H2
    else :
        if IsMember(FirstElement(H1),H2) :
            return MakeUnion(Tail(H1),H2)
        else:
            return konso(FirstElement(H1),MakeUnion(Tail(H1),H2))

print()
print("MakeUnion :")
print(MakeUnion([1,2,3,4],[3,4,5,6])) # [1,2,3,4,5,6]

#--------------------------------------------!!!------------------------------------------#

# Rember : Element, List --> List
#   {Rember(x,L) Menghapus sebuah element bernilai x dari list L, list yang baru akan berkurang satu elementnya yaitu yang bernilai x, list kosong tetap menjadi list kosong}
def Rember(x,L) :
  if IsEmpty(L) :
    return L
  else:
    if FirstElement(L) == x :
      return Tail(L)
    else:
      return konso(FirstElement(L),Rember(x,Tail(L)))

print()
print("Rember :")
print(Rember(3,[1,2,3,3,4,5])) # [1,2,3,4,5]

#--------------------------------------------!!!------------------------------------------#

# MultiRember : Element, List --> List
#   {MultiRember(x,L) Menghapus semua element bernilai x dari list L, list yang baru tidak lagi mempunyai element dengan nilai x, list kosong tetap menjadi list kosong}
def MultiRember(x,L) :
  if IsEmpty(L) :
    return L
  else:
    if FirstElement(L) == x :
      return MultiRember(x,Tail(L))
    else:
      return konso(FirstElement(L),MultiRember(x,Tail(L)))

print()
print("MultiRember :")
print(MultiRember(3,[1,2,3,3,4,5])) # [1,2,4,5]
        
#--------------------------------------------!!!------------------------------------------#

# IsEqualSet : Set, Set --> Boolean
#   {IsEqualSet(H1,H2) Benar jika set H1 sama dengan set H2, yaitu jika semua element dari set H1 juga merupakan element dari set H2, tanpa peduli urutannya}
def IsEqualSet(H1,H2) :
  return IsSubSet(H1,H2) and IsSubSet(H2,H1)

print()
print("IsEqualSet :")
print(IsEqualSet([1,2,3],[2,3,1])) # True