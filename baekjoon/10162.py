N = int(input())
button = [300,60,10]
A = 0
B = 0
C = 0
for i in button:
    if i == 300:
        A = N // 300
        N = N % 300
    elif i == 60:
        B = N // 60
        N = N % 60
    elif i == 10:
        C = N // 10
        N = N % 10

if N % 10 > 0:
        print(-1)
else:
    print(A,B,C)
print(N)