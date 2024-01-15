saham = input()
beli1,jual1 = [int(x) for x in input().split()]
beli2,jual2 = [int(x) for x in input().split()]
beli3,jual3 = [int(x) for x in input().split()]

unri = ((jual1-beli1)+(jual2-beli2)+(jual3-beli3))*100
print(unri)