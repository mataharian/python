# Konso : Element, List --> List
#   {Konso(elmnt,lst) menghasilkan sebuah list dari elmnt dan lst, dengan e sebagai elemen pertama}
def konso (elmnt,lst) :
  if lst == [] :
    return [elmnt]
  else :
    return [elmnt] + lst

print("Konso :")
print(konso(10,[1,2,3,4,5])) #[10,1,2,3,4,5]

#--------------------------------------------!!!------------------------------------------#

# Konsi : Element, List --> List
#   {Konsi(elmnt,lst) menghasilkan sebuah list dari elmnt dan lst, dengan e sebagai elemen terakhir}
def konsi (elmnt,lst) :
  if lst == [] :
    return [elmnt]
  else :
    return lst + [elmnt]

print()
print("Konsi :")
print(konsi(10,[1,2,3,4,5])) # [1,2,3,4,5,10]
#--------------------------------------------!!!------------------------------------------#

# IsEmpty : List --> Boolean
#   {IsEmpty(L) Menentukan sebuah list L merupakan list kosong atau bukan, jika list kosong maka true, dan jika bukan list kosong maka false}
def IsEmpty(L) :
  if L == [] :
    return True
  else :
    return False

print()
print("IsEmpty :")
print(IsEmpty([1,2,3,4,5])) # False
print(IsEmpty([])) # True

#--------------------------------------------!!!------------------------------------------#

# FirstElement : List tidak kosong --> Element
#   {FirstElement(L) menghasilkan element pertama dari sebuah list L}
def FirstElement(L) :
  if not IsEmpty(L) :
    return L[0]

print()
print("FirstElement :")
print(FirstElement([1,2,3,4,5])) # 1

#--------------------------------------------!!!------------------------------------------#

# LastElement : List tidak kosong --> Element
#   {LastElement(L) menghasilkan element terakhir dari sebuah list L}
def LastElement(L) :
  if not IsEmpty(L) :
    return L[-1]

print()
print("LastElement :")
print(LastElement([1,2,3,4,5])) # 5

#--------------------------------------------!!!------------------------------------------#

# Tail : List tidak kosong --> List
#   {Tail(L) Menghasilkan sebuah list tanpa element pertama dari list L, mungkin kosong}
def Tail(L) :
  if not IsEmpty(L) :
    return L[1:]

print()
print("Tail :")
print(Tail([1,2,3,4,5]))

#--------------------------------------------!!!------------------------------------------#

# Head : List tidak kosong --> List
#   {Head(L) Menghasilkan sebuah list tanpa element terakhir dari list L, mungkin kosong}
def Head(L) :
  if not IsEmpty(L) :
    return L[:-1]

print()
print("Head :")
print(Head([1,2,3,4,5]))  #[1,2,3,4]

#--------------------------------------------!!!------------------------------------------#

# IsMember : Element, List --> Boolean
#   {IsMember(x,L) Benar jika sebuah element x merupakan element dari list L}

def IsMember(x,L) :
  if IsEmpty(L) :
    return False
  else :
    if FirstElement(L) == x :
      return True
    else :
      return IsMember(x,Tail(L))

# IsMember(3,[1,2,3])
# --> (3,[2,3])
# --> (3,[3])
# --> True

print()
print("IsMember :")
print(IsMember(3,[1,2,3])) #True

#--------------------------------------------!!!------------------------------------------#

# NbElement : List --> Integer
#   {NbElement(L) Menghasilkan banyaknya element list L, nol jika list L kosong}
def NbElement(L):
    if IsEmpty(L):
        return 0
    else:
        return 1 + NbElement(Tail(L))

print()
print("NBElement :")
print(NbElement([1,2,3,4,5])) # 5

#--------------------------------------------!!!------------------------------------------#

# IsOneElement : List --> Boolean
#   {IsOneElement(L) Benar jika sebuah list L hanya mempunyai 1 element}

def IsOneElement(L):
    if IsEmpty(L):
        return False
    elif NbElement(L) == 1:
        return True
    else:
        return False

print()
print("IsOneElement :")
print(IsOneElement([5])) # True

#--------------------------------------------!!!------------------------------------------#

# IsEqual : List, List --> Boolean
#   {IsEqual(L1,L2) Benar jika semua element L1 sama dengan semua element L2 : sama urutan dan nilainya}
def IsEqual(L1,L2):
    if IsEmpty(L1) and IsEmpty(L2):
        return True
    elif IsEmpty(L1) or IsEmpty(L2):
        return False
    else:
        if FirstElement(L1) == FirstElement(L2) :
            return IsEqual(Tail(L1),Tail(L2))
        else :
          return False

print()
print("IsEqual :")
print(IsEqual([1,2,3,4,5],[5,4,3,2,1])) # False

#--------------------------------------------!!!------------------------------------------#

# Copy : List --> List
#   {Copy(L) Menghasilkan salinan list L, artinya list lain yang identik dengan list L}
def Copy(L) :
  if IsEmpty(L) :
    return []
  else :
    return konso(FirstElement(L),Copy(Tail(L)))

print()
print("Copy :")
print(Copy([1,2,3,4,5])) # [1,2,3,4,5]

#--------------------------------------------!!!------------------------------------------#

# Inverse : List --> List
#   {Inverse(L) Menghasilkan salinan list L dengan urutan element terbalik}
def Inverse(L) :
  if IsEmpty(L) :
    return []
  else :
    return konsi(FirstElement(L), Inverse(Tail(L)))

print()
print("Inverse :")
print(Inverse([1,2,3,4,5])) # [5,4,3,2,1]

#--------------------------------------------!!!------------------------------------------#

# Konkat : List, List --> List
#   {Konkat(L1,L2) Menghasilkan konkatenasi 2 buah list dengan list L2 sesudah list L1}
def Konkat(L1,L2) :
  if IsEmpty(L1) :
    return L2
  else :
    return konso(FirstElement(L1),Konkat(Tail(L1),L2))

print()
print("Konkat :")
print(Konkat([1,2,3,4,5],[5,4,3,2,1])) # [1,2,3,4,5,5,4,3,2,1]

#--------------------------------------------!!!------------------------------------------#

# IsNbElement : Integer, List --> Boolean
#   {IsNbElement(N,L) Benar jika banyaknya element list L sama dengan N}
def IsNbElementN (N,L) :
  return NbElement(L) == N

print()
print("IsNbElementN :")
print(IsNbElementN(5,[1,2,3,4,5])) # True

#--------------------------------------------!!!------------------------------------------#

# IsInverse : List, List --> Boolean
#   {IsInverse(L1,L2) Benar jika list L2 adalah list dengan urutan element terbalik dari list L1}
def IsInverse(L1,L2) :
  return L1 == Inverse(L2)

print()
print("IsInverse :")
print(IsInverse([1,2,3,4,5],[5,4,3,2,1])) # True

#--------------------------------------------!!!------------------------------------------#
# ElementKeN : Integer, List --> Integer
#   {ElementKeN(N,L) Menghasilkan element list yang ke-N}
def ElementKeN(N,L) :
  if N == 1 :
    return FirstElement(L)
  else:
    return ElementKeN(N-1,Tail(L))

print()
print("ElementKeN :")
print(ElementKeN(2,[1,2,3,4,5])) # 3

#--------------------------------------------!!!------------------------------------------#

# IsXElementKeN : Integer, Integer, List --> Boolean
#   {IsXElementKeN(N,X,L) Benar jika X adalah element dari list L yang ke-N}
def IsXElementKeN(N,X,L) :
  return X == ElementKeN(N,L)

print()
print("IsXElementKeN :")
print(IsXElementKeN(2,3,[1,2,3,4,5]))

#--------------------------------------------!!!------------------------------------------#

# Inseret : Integer, List --> List
#   {Inser(x,L) Melakukan insert atau memasukkan x ke list L dengan menghasilkan list x sesuai dengan urutan list L}
def Insert(x,L) :
  if IsEmpty(L) :
    return [x]
  else :
    if x < FirstElement(L) :
      return konso(x,L)
    else :
      return konso(FirstElement(L),Insert(x,Tail(L)))

print()
print("Insert : ")
print(Insert(5,[10,12,6,7,18]))

#--------------------------------------------!!!------------------------------------------#

# Insort : List --> List
#   {Insort(L) Menghasilkan sebuah list dengan urutan terkecil ke terbesar}
def Insort(L) :
  if IsEmpty(L) :
    return []
  else :
    return Insert(FirstElement(L),Insort(Tail(L)))

print()
print("Insort : ")
print(Insort([5,12,6,124,2,51]))

#--------------------------------------------!!!------------------------------------------#

def MaxList(L) :
  if IsEmpty(L) :
    return 0
  else :
    if FirstElement(L) > MaxList(Tail(L)) :
      return FirstElement(L)
    else :
      return MaxList(Tail(L))

print()
print("MaxList : ")
print(MaxList([19, 21, 25, 11,14, -13, 10, -19, 10]))

#--------------------------------------------!!!------------------------------------------#

def MinList(L) :
  if IsEmpty(L) :
    return 0
  else :
    if FirstElement(L) < MinList(Tail(L)) :
      return FirstElement(L)
    else :
      return MinList(Tail(L))

print()
print("MinList : ")
print(MinList([19, 21, 25, 11,14, -13, 10, -19, 10]))