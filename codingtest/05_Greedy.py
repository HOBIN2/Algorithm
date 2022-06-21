M ,N = map(int,input().split())
ball = list(map(int,input().split()))
count = 0
for x in range(M-1):
    for y in range(x+1,M):
        if ball[x] != ball[y]:
            count += 1
print(count)
