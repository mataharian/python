# Akar : PohonBiner tidak kosong --> Element
#   {Akar(Tree) adalah akar dari tree. Jika tree adalah /L,A,R\ maka Akar(Tree) adalah A}
def Akar(tree) :
  return tree.A

# Left : PohnBiner tidak kosong --> PohonBiner
#   {Left(tree) adalah sub pohon kiri dari tree. Jika tree adalah /L,A,R\ maka Left(tree) adalah L}
def Left(tree) :
  return tree.L

# Right : PohnBiner tidak kosong --> PohonBiner
#   {Right(tree) adalah sub pohon kanan dari tree. Jika tree adalah /L,A,R\ maka Right(tree) adalah R}
def Right(tree) :
  return tree.R

# IsTreeEmpty : PohonBiner -- > Boolean
#   {IsTreeEmpty(Tree) True jika Tree adalah pohon biner kosong : (/\)}
def IsTreeEmpty(Tree) :
  if Tree == None :
    return True
  else :
    return False

# NbElementTree : PohonBiner --> Integer >= 0
#   {NbElementTree(Tree) memberikan banyaknya element dari pohon Tree}
def NbElementTree(Tree) :
  if IsTreeEmpty(Tree) :
    return 0 
  else :
    return (NbElementTree(Left(Tree)) + 1 + (NbElementTree(Right(Tree))))

# IsOneElementTree : Tree --> Boolean
#   {IsOneElementTree(Tree) True jika sebuah pohon Tree hanya memiliki akar}
def IsOneElementTree(Tree) :
  if NbElementTree(Tree) == 1 :
    return True
  else :
    return False

# NbDaun : PohonBiner --> Integer >= 0
#   {NbDaun(Tree) memberikan banyaknya daun dari pohon Tree}
def NbDaun(Tree) :
  if IsTreeEmpty(Tree) :
    return 0
  else :
    if IsOneElementTree(Tree) :
      return 1
    else :
      return NbDaun(Left(Tree)) + NbDaun(Right(Tree))


# IsUnerLeft : PohonBiner --> Boolean
#   {IsUnerLeft(Tree) Benar jika Tree hanya mengandung sub pohon kiri tidak kosong (//LA\\)}
def IsUnerLeft(Tree) :
  if not IsTreeEmpty(Tree) and not IsTreeEmpty(Left(Tree)) and IsTreeEmpty(Right(Tree)) :
    return True
  else :
    return False

# IsUnerRight : PohonBiner --> Boolean
#   {IsUnerRight(Tree) Benar jika Tree hanya mengandung sub pohon kanan tidak kosong (//AR\\)}
def IsUnerRight(Tree) :
  if not IsTreeEmpty(Tree) and IsTreeEmpty(Left(Tree)) and not IsTreeEmpty(Right(Tree)) :
    return True
  else :
    return False

# IsBiner : PohonBiner --> Boolean
#   {IsBiner(Tree) Benar jika Tree mengandung sub pohon kiri dan sub pohon kanan kanan (//LAR\\)}
def IsBiner(Tree) :
  if not IsTreeEmpty(Tree) and not IsTreeEmpty(Left(Tree)) and not IsTreeEmpty(Right(Tree)) :
    return True
  else :
    return False

# RepPrefix : PohonBiner --> List of Element
#   {RepPrefix(Tree) Memberikan representasi linier(dalam bentuk list), dengan urutan element list sesuai dengan urutan penulisan pohon secara prefix}
def RepPrefix(Tree) :
  if IsOneElementTree(Tree) :
    return [Akar(Tree)]
  else :
    if IsBiner(Tree) :
      return[Akar(Tree)] + [RepPrefix(Left(Tree))] + [RepPrefix(Right(Tree))]
    elif IsUnerLeft(Tree) :
      return [Akar(Tree)] + [RepPrefix(Left(Tree))]
    elif IsUnerRight(Tree) :
      return [Akar(Tree)] + [RepPrefix(Right(Tree))]

class PohonBiner :
  def __init__(self,L,A,R) :
    self.A = A
    self.L = L
    self.R = R

def MakeTree(L,A,R) :
  return PohonBiner(L,A,R)

Tree1 = MakeTree(
  MakeTree(
    MakeTree(
      None,
      4,
      MakeTree(
        None,
        8,
        None
      )
    ),
    1,
    None
  ),
  2,
  MakeTree(
    MakeTree(
      None,
      5,
      None
    ),
    3,
    MakeTree(
      MakeTree(
       None,
       7,
       None
      ),
      6,
      None)))
#               2
#         1           3
#      4           5     6 
#        8             7   
print("Element Pohon :")
print(Akar(Tree1)) # 2 
print(Akar(Left(Tree1))) # 1
print(Akar(Right(Tree1))) # 3
print(Akar(Left(Left(Tree1)))) # 4
print(Akar(Right(Right(Tree1)))) # 6
print(Akar(Left(Right(Tree1)))) # 5
print(Akar(Right(Left(Left(Tree1))))) # 8
print(Akar(Left(Right(Right(Tree1))))) # 7

print()
print("IsTreeEmpty :")
print(IsTreeEmpty(Tree1))

print()
print("NbElementTree :")
print(NbElementTree(Tree1))

print()
print("IsOneElementTree :")
print(IsOneElementTree(Tree1))

print()
print("NbDaun :")
print(NbDaun(Tree1))

print()
print("IsUnerLeft :")
print(IsUnerLeft(Tree1))

print()
print("IsUnerRight :")
print(IsUnerRight(Tree1))

print()
print("IsBiner :")
print(IsBiner(Tree1))

print()
print("RepRefix :")
print(RepPrefix(Tree1))