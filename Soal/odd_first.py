User_input = [int(x) for x in input().split()]
odd = []
even = []
    
for n in User_input:
    if n % 2 != 0 :
        odd.append(n)
    else:
        even.append(n)
            
even.sort(reverse = True)
odd.sort(reverse = True)
    
for genap in even :
    odd.append(genap)

print(odd)