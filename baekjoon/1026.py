N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort(reverse=True)
B.sort()
sum = 0
for x, y in zip(A,B):
    sum += x * y
print(sum)