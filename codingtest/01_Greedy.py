N = int(input())
P = list(map(int,input().split()))
P.sort()
count = 0
number = 0
for i in P:
    count += 1
    if count >= i:
        number += 1
        count = 0
print(number)
    

