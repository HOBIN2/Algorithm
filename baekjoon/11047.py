N, K = map(int,input().split())
S = []
count = 0
for i in range(N):
    S.append(int(input()))
for x in reversed(S):
    if K == 0:
        break
    elif K // x >= 1:
        count += K // x
        K =  K % x
print(count)