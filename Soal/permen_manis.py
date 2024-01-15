x = int(input())
budi = list(map(int,input().strip().split()))[:x]
anto = list(map(int,input().strip().split()))[:x]

def permen(a,L1,L2):
    result = 0
    
    for i in range(a):
        if L2[i] > L1[i]:
            result += 1
    return result

print(permen(x,budi,anto))